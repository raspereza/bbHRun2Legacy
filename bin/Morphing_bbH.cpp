#include "CombineHarvester/CombinePdfs/interface/MorphFunctions.h"
#include "CombineHarvester/CombinePdfs/interface/CMSHistFuncFactory.h"
#include "CombineHarvester/CombineTools/interface/Algorithm.h"
#include "CombineHarvester/CombineTools/interface/AutoRebin.h"
#include "CombineHarvester/CombineTools/interface/BinByBin.h"
#include "CombineHarvester/CombineTools/interface/CardWriter.h"
#include "CombineHarvester/CombineTools/interface/CombineHarvester.h"
#include "CombineHarvester/CombineTools/interface/Observation.h"
#include "CombineHarvester/CombineTools/interface/Process.h"
#include "CombineHarvester/CombineTools/interface/Systematics.h"
#include "CombineHarvester/CombineTools/interface/Utilities.h"
#include "CombineHarvester/bbHRun2Legacy/interface/HttSystematics_bbH.h"
#include "CombineHarvester/bbHRun2Legacy/interface/dout_tools.h"
#include "RooRealVar.h"
#include "RooWorkspace.h"
#include "TF1.h"
#include "TH2.h"
#include "boost/algorithm/string/predicate.hpp"
#include "boost/algorithm/string/split.hpp"
#include "boost/lexical_cast.hpp"
#include "boost/program_options.hpp"
#include "boost/regex.hpp"
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <math.h>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>

using namespace std;
using boost::starts_with;
namespace po = boost::program_options;

template<typename T>
void update_vector_by_byparser(T& parameter, const T& parser, const string name="") {
    if (parser.size() > 0)
    {
        const std::string lower_str = boost::algorithm::to_lower_copy(parser[0]);
        doutnonl("WARNING: The", name, "are set manually:");

        if (parser.size() == 1 && (lower_str == "none" || lower_str == "null" || lower_str == "pass"))
          parameter = {};
        else
          parameter = parser;

        dprintVector(parameter);
    }
}

std::vector<double> binning_from_map(std::map<unsigned int, std::vector<double>> binning_map) {
    std::vector <double> binning = {};
    if(binning_map.begin() != binning_map.end())
    {
        for (auto it = binning_map.begin(); it != binning_map.end(); ++it)
            for (double first = it->second[0]; first < it->second[1]; first+=it->second[2])
            {
                binning.push_back(first);
            }
        auto last = --binning_map.end();
        binning.push_back(last->second[1]);
    }
    return binning;
}

void ConvertShapesToLnN (ch::CombineHarvester& cb, string name) {
  auto cb_syst = cb.cp().syst_name({name});
  cb_syst.ForEachSyst([&](ch::Systematic *syst) {
    if (syst->type() == "shape") {
      std::cout << "Converting systematic " << syst->name() << " for process " << syst->process() << " in bin " << syst->bin() << " to lnN." <<std::endl;
      syst->set_type("lnN");
      return;
    }
  }); 
}

int main(int argc, char **argv) {
  typedef vector<string> VString;
  typedef vector<pair<int, string>> Categories;
  using ch::syst::bin_id;
  using ch::JoinStr;
  using ch::syst::SystMap;

  // Define program options
  string output_folder = "output_bbH_Run2";
  string base_path = string(getenv("CMSSW_BASE")) + "/src/CombineHarvester/bbHRun2Legacy/shapes/";
  //  string sm_gg_fractions = string(getenv("CMSSW_BASE")) + "/src/CombineHarvester/MSSMvsSMRun2Legacy/data/higgs_pt_reweighting_fullRun2_v2.root";
  //  string sm_predictions = string(getenv("CMSSW_BASE")) + "/src/CombineHarvester/MSSMvsSMRun2Legacy/input/sm_predictions_13TeV.json";
  string chan = "tt";
  string category = "tt_Nbtag0";

  bool auto_rebin = false;
  bool manual_rebin = true;
  bool verbose = true;
  bool use_automc = true;
  bool no_emb(false);
  bool no_shape_systs = false;
  bool ttbar_rate = false;
  bool test_mode = false;

  string analysis = "inclusive_bbH"; 
  std::vector<string> analysis_choices = {"sm", "bbH", "inclusive_bbH"};
  string categorization = "btag";
  std::vector<string> categorization_choices = {"mva", "btag", "btag_fine"};
  int era = 2016; // 2016, 2017 or 2018
  std::vector<int> era_choices = {2016, 2017, 2018};

  vector<string> parser_bkgs({}), parser_bkgs_em({});

  po::variables_map vm;
  po::options_description config("configuration");
  config.add_options()
      ("base-path,base_path", po::value<string>(&base_path)->default_value(base_path), "inputs, expected to contain a subdirectory <era>/<channel>")
      ("channel", po::value<string>(&chan)->default_value(chan), "single channel to process")
      ("category", po::value<string>(&category)->default_value(category))
    //      ("do-morph", po::value<bool>(&do_morph)->default_value(do_morph))
      ("auto_rebin", po::value<bool>(&auto_rebin)->default_value(auto_rebin))
      ("manual_rebin", po::value<bool>(&manual_rebin)->default_value(manual_rebin))
      ("ttbar_rate", po::value<bool>(&ttbar_rate)->default_value(ttbar_rate))
      ("use_automc", po::value<bool>(&use_automc)->default_value(use_automc))
      ("verbose", po::value<bool>(&verbose)->default_value(verbose))
      ("output_folder", po::value<string>(&output_folder)->default_value(output_folder))
      ("analysis", po::value<string>(&analysis)->default_value(analysis))
      ("categorization", po::value<string>(&categorization)->default_value(categorization))
      ("era", po::value<int>(&era)->default_value(era))
      ("no-emb,no-emb,no_emb", po::bool_switch(&no_emb), "use MC samples instead of embedding")
      ("debug,d", po::bool_switch(&debug), "debug printout")
      ("bkgs", po::value<vector<string>>(&parser_bkgs)->multitoken(), "backgrounds")
      ("bkgs_em", po::value<vector<string>>(&parser_bkgs_em)->multitoken(), "backgrounds-em")
      ("no_shape_systs", po::value<bool>(&no_shape_systs)->default_value(no_shape_systs))
      ("test_mode", po::value<bool>(&test_mode)->default_value(test_mode),"override deprecation warning when running")
      ("help", "produce help message");
  po::store(po::command_line_parser(argc, argv).options(config).run(), vm);
  po::notify(vm);
  if (vm.count("help"))
    {
      cout << config << "\n";
      return 0;
    }
  
  if(!test_mode){
    std::cout<<" DEPRECATED - USE THE PYTHON SETUP INSTEAD "<<std::endl;
    exit(1);
  }
  // Sanity check for options with choices
  // analysis option
  if(std::find(analysis_choices.begin(), analysis_choices.end(), analysis) == analysis_choices.end()){
    std::cout << "ERROR: wrong choice of 'analysis' option. Please choose from:\n\t";
    for(auto choice : analysis_choices){
      std::cout << choice << " ";
    }
    std::cout << std::endl;
    exit(1);
  }
  // categorization option
  if(std::find(categorization_choices.begin(), categorization_choices.end(), categorization) == categorization_choices.end()){
    std::cout << "ERROR: wrong choice of 'categorization' option. Please choose from:\n\t";
    for(auto choice : categorization_choices){
      std::cout << choice << " ";
    }
    std::cout << std::endl;
    exit(1);
  }
  // era option
  if(std::find(era_choices.begin(), era_choices.end(), era) == era_choices.end()){
    std::cout << "ERROR: wrong choice of 'era' option. Please choose from:\n\t";
    for(auto choice : era_choices){
      std::cout << choice << " ";
    }
    std::cout << std::endl;
    exit(1);
  }

  // Define the location of the "auxiliaries" directory where we can
  // source the input files containing the datacard shapes
  std::string era_tag;
  if (era == 2016) era_tag = "2016";
  else if (era == 2017) era_tag = "2017";
  else if (era == 2018) era_tag = "2018";
  else std::runtime_error("Given era is not implemented.");

  output_folder = output_folder + "_" + analysis + "_" + categorization;
  std::map<string, string> input_dir;
  if (base_path.back() != '/' ) base_path += "/";
  if (!boost::filesystem::exists(output_folder)) boost::filesystem::create_directories(output_folder);
  input_dir["mt"] = base_path + "/" +era_tag + "/mt/";
  input_dir["et"] = base_path + "/" +era_tag + "/et/";
  input_dir["tt"] = base_path + "/" +era_tag + "/tt/";
  input_dir["em"] = base_path + "/" +era_tag + "/em/";

  // Define channels
  VString chns;
  if (chan.find("mt") != std::string::npos)
    chns.push_back("mt");
  if (chan.find("et") != std::string::npos)
    chns.push_back("et");
  if (chan.find("tt") != std::string::npos)
    chns.push_back("tt");
  if (chan.find("em") != std::string::npos)
    chns.push_back("em");

  // Define restriction to the channel defined by '--category' option
  if(category != "all"){
    std::vector<std::string> category_split;
    boost::split(category_split, category, boost::is_any_of("_"));
    chns = {category_split.at(0)};
  }
  //  doutnonl("Channels:\n\t");
  //  dprintVector(chns);

  // Define background and signal processes
  map<string, VString> bkg_procs;
  map<string, VString> sig_procs;
  VString bkgs, bkgs_em, bkgs_tt, bkgs_em_noCR; 
  VString bkgs_HWW, bkgs_HTT, signals_HTT, signals_HWW;
  VString bkgs_HWW_nomass, bkgs_HTT_nomass, signals_HTT_nomass, signals_HWW_nomass;

  bkgs_HWW = {"ggHWW125","qqHWW125"};
  bkgs_HTT = {"ggH125","qqH125"};
  signals_HTT = {"bbH125","ggHbb125"};
  signals_HWW = {"bbHWW125","ggHbbWW125"};

  bkgs_HWW_nomass = {"ggHWW","qqHWW"};
  bkgs_HTT_nomass = {"ggH","qqH"};
  signals_HTT_nomass = {"bbH","ggHbb"};
  signals_HWW_nomass = {"bbHWW","ggHbbWW"};

  if (analysis == "bbH") {
    std::cout << "Considering bbH as signal : removing ggHbb from list of signal processes" << std::endl;
    bkgs_HTT.push_back("ggHbb125");
    bkgs_HWW.push_back("ggHbbWW125");
    bkgs_HTT_nomass.push_back("ggHbb");
    bkgs_HWW_nomass.push_back("ggHbbWW");
    signals_HTT.erase(std::remove(signals_HTT.begin(), signals_HTT.end(), "ggHbb125"), signals_HTT.end());
    signals_HWW.erase(std::remove(signals_HWW.begin(), signals_HWW.end(), "ggHbbWW125"), signals_HWW.end());    
    signals_HTT_nomass.erase(std::remove(signals_HTT_nomass.begin(), signals_HTT_nomass.end(), "ggHbb"), signals_HTT_nomass.end());
    signals_HWW_nomass.erase(std::remove(signals_HWW_nomass.begin(), signals_HWW_nomass.end(), "ggHbbWW"), signals_HWW_nomass.end());    
  }

  std::cout << "HTT signals            : ";
  for(auto proc : signals_HTT){
    std::cout << proc << " ";
  }
  std::cout << std::endl;
  std::cout << "HWW signals (em channel): ";
  for(auto proc : signals_HWW){
    std::cout << proc << " ";
  }
  std::cout << std::endl;

  bkgs = {"EMB", "ZL", "TTL", "VVL", "jetFakes"};
  bkgs_tt = {"EMB", "ZL", "TTL", "VVL", "jetFakes", "wFakes"};
  bkgs_em = {"EMB", "W", "ZL", "TTL", "VVL"};
  bkgs_em_noCR = {"QCD"};

  update_vector_by_byparser(bkgs, parser_bkgs, "bkgs");
  update_vector_by_byparser(bkgs_tt, parser_bkgs, "bkgs_tt");
  update_vector_by_byparser(bkgs_em, parser_bkgs_em, "bkgs_em");

  if (no_emb) {
    dout("WARNING: the EMB process is removed from backgrounds and ZTT, TTT and VVT templates are added");
    bkgs.erase(std::remove(bkgs.begin(), bkgs.end(), "EMB"), bkgs.end());
    bkgs_em.erase(std::remove(bkgs_em.begin(), bkgs_em.end(), "EMB"), bkgs_em.end());
    bkgs_tt.erase(std::remove(bkgs_tt.begin(), bkgs_tt.end(), "EMB"), bkgs_tt.end());
    bkgs.push_back("ZTT"); bkgs.push_back("TTT"); bkgs.push_back("VVT");
    bkgs_em.push_back("ZTT"); bkgs_em.push_back("TTT"); bkgs_em.push_back("VVT");
    bkgs_tt.push_back("ZTT"); bkgs_tt.push_back("TTT"); bkgs_tt.push_back("VVT");   
  }

  std::cout << "[INFO] Considering the following processes as main backgrounds:\n";

  if (chan.find("em") != std::string::npos || chan.find("all") != std::string::npos) {
    std::cout << "For em channel : \n\t";
    printVector(bkgs_em);
  }
  if (chan.find("tt") != std::string::npos || chan.find("all") != std::string::npos) {
    std::cout << "For tt channels : \n\t";
    printVector(bkgs_tt);
  }
  if (chan.find("mt") != std::string::npos || chan.find("et") != std::string::npos || chan.find("all") != std::string::npos) {
    std::cout << "For et,mt channels : \n\t";
    printVector(bkgs);
  }

  bkg_procs["et"] = bkgs;
  bkg_procs["mt"] = bkgs;
  bkg_procs["tt"] = bkgs_tt;
  bkg_procs["em"] = bkgs_em;

  sig_procs["et"] = signals_HTT_nomass;
  sig_procs["mt"] = signals_HTT_nomass;
  sig_procs["tt"] = signals_HTT_nomass;
  sig_procs["em"] = signals_HTT_nomass;

  for(auto chn : chns){
    if (analysis == "sm")
      sig_procs[chn] = JoinStr({sig_procs[chn],bkgs_HTT_nomass});
    else 
      bkg_procs[chn] = JoinStr({bkg_procs[chn],bkgs_HTT});      
    if (chn == "em") { 
      sig_procs[chn] = JoinStr({sig_procs[chn],signals_HWW_nomass});
      if (analysis == "sm")
	sig_procs[chn] = JoinStr({sig_procs[chn],bkgs_HWW_nomass});
      else
	bkg_procs[chn] = JoinStr({bkg_procs[chn],bkgs_HWW});
    }
  }

  vector<int> mva_cat_bins = {1,2,3,4,5,6,7,8,9,10};
  vector<int> btag_cat_bins = {12,13,14,15,22,23,24,25,32,33,34,35};

  // Define categories
  map<string, Categories> cats;
  if (categorization == "btag") {
    cats["et"] = {
        {12, "et_Nbtag0_MTLt40"},
        {13, "et_Nbtag0_MT40To70"},
        {22, "et_NbtagGe1_MTLt40"},
        {23, "et_NbtagGe1_MT40To70"},
    };
    cats["mt"] = {
        {12, "mt_Nbtag0_MTLt40"},
        {13, "mt_Nbtag0_MT40To70"},
        {22, "mt_NbtagGe1_MTLt40"},
        {23, "mt_NbtagGe1_MT40To70"},
    };
    cats["tt"] = {
        {12, "tt_Nbtag0"},
        {22, "tt_NbtagGe1"},
    };
    cats["em"] = {
      {12, "em_Nbtag0_DZetaGt30"},
      {13, "em_Nbtag0_DZetam10To30"},
      {14, "em_Nbtag0_DZetam35Tom10"},
      {15, "em_Nbtag0_DZetaLtm35"},
	
      {22, "em_NbtagGe1_DZetaGt30"},
      {23, "em_NbtagGe1_DZetam10To30"},
      {24, "em_NbtagGe1_DZetam35Tom10"},
      {25, "em_NbtagGe1_DZetaLtm35"},
    };
  }
  else if(categorization == "btag_fine"){

    cats["et"] = {
        {12, "et_Nbtag0_MTLt40"},
        {13, "et_Nbtag0_MT40To70"},
        {22, "et_Nbtag1_MTLt40"},
        {23, "et_Nbtag1_MT40To70"},
        {32, "et_Nbtag2_MTLt40"},
        {33, "et_Nbtag2_MT40To70"},
    };

    cats["mt"] = {
        {12, "mt_Nbtag0_MTLt40"},
        {13, "mt_Nbtag0_MT40To70"},
        {22, "mt_Nbtag1_MTLt40"},
        {23, "mt_Nbtag1_MT40To70"},
        {32, "mt_Nbtag2_MTLt40"},
        {33, "mt_Nbtag2_MT40To70"},
    };

    cats["tt"] = {
        {12, "tt_Nbtag0"},
        {22, "tt_Nbtag1"},
	{32, "tt_Nbtag2"},
    };
    cats["em"] = {

      {12, "em_Nbtag0_DZetaGt30"},
      {13, "em_Nbtag0_DZetam10To30"},
      {14, "em_Nbtag0_DZetam35Tom10"},
      {15, "em_Nbtag0_DZetaLtm35"},
      
      {22, "em_Nbtag1_DZetaGt30"},
      {23, "em_Nbtag1_DZetam10To30"},
      {24, "em_Nbtag1_DZetam35Tom10"},
      {25, "em_Nbtag1_DZetaLtm35"},
      
      {32, "em_Nbtag2_DZetaGt30"},
      {33, "em_Nbtag2_DZetam10To30"},
      {34, "em_Nbtag2_DZetam35Tom10"},
      {35, "em_Nbtag2_DZetaLtm35"},
    };
  }
  else if(categorization == "mva"){
    cats["et"] = {
      { 1, "et_xxh"}, 

      { 4, "et_ttbar"},
      { 5, "et_zll"},
      { 6, "et_misc"},
      { 7, "et_emb"},
      { 8, "et_ff"}
    };

    cats["mt"] = {
      { 1, "mt_xxh"}, 

      { 4, "mt_ttbar"},
      { 5, "mt_zll"},
      { 6, "mt_misc"},
      { 7, "mt_emb"},
      { 8, "mt_ff"}
    };

    cats["tt"] = {
      { 1, "tt_cat0_NbtagGt1"}, 
      { 2, "tt_cat1_NbtagGt1"},
      { 3, "tt_cat2_NbtagGt1"},
      { 4, "tt_cat3_NbtagGt1"},
    };

    cats["em"] = {
      { 1, "em_xxh"}, 

      { 4, "em_ttbar"},
      { 6, "em_misc"},
      { 7, "em_emb"},
      { 8, "em_ss"},
    };
  }
  else throw std::runtime_error("Given categorization is not known.");

  // Create combine harverster object
  ch::CombineHarvester cb;
  cb.SetFlag("workspaces-use-clone", true);

  // Introduce ordering of categories for the final discriminator in MSSM
  std::vector<int> mva_categories = {4,5,6,7,8}; // Control regions for MVA HTT analysis
  std::vector<int> em_ttbar_categories = {15,25,35}; // tt control regions for em channel
  std::vector<int> no_btag_categories = {12,13,14,15}; // 0-btag 
  std::vector<int> btag_categories = {22,23,24,25}; // 1-btag or >=1 
  std::vector<int> doublebtag_categories = {32,33,34,35}; // 2-btag
  std::vector<int> all_btag_categories = {22,23,24,25,32,33,34,35};  

  std::vector<int> main_mva_signal_category = {1}; // category for the bbH SM signal
  std::vector<int> mva_signal_category = {2,3}; // category for the bbHWW and main SM signals

  for (auto chn : chns) {
    Categories exclude_em_ttbar = cats[chn]; // contain all except 15,25,35

    for (auto catit = exclude_em_ttbar.begin(); catit != exclude_em_ttbar.end(); ++catit)
    {
      if(std::find(em_ttbar_categories.begin(), em_ttbar_categories.end(), (*catit).first) != em_ttbar_categories.end()){
        exclude_em_ttbar.erase(catit);
        --catit;
      }
    }

    std::cout << "[INFO] Using the following categories:" << std::endl;
    for (const auto i: cats[chn]) 
      std::cout << "      " << i.first << ' ' << i.second << std::endl;
    /*
    std::cout << "   sm_and_btag_cats:" << std::endl;
    for (const auto i: sm_and_btag_cats)
      std::cout << "      " << i.first << ' ' << i.second << std::endl;
    std::cout  << std::endl;
    std::cout << "    mssm_cats:" << std::endl;
    for (const auto i: mssm_cats)
      std::cout << "      " << i.first << ' ' << i.second << std::endl;
    std::cout  << std::endl;
    std::cout << "    mssm_btag_cats:" << std::endl;
    for (const auto i: mssm_btag_cats)
      std::cout << "      " << i.first << ' ' << i.second << std::endl;
    std::cout  << std::endl;
    std::cout << "    sm_signal_cat:" << std::endl;
    for (const auto i: sm_signal_cat)
      std::cout << "      " << i.first << ' ' << i.second << std::endl;
    std::cout  << std::endl;
    */

    // Adding obervations 
    cb.AddObservations({"*"}, {"htt"}, {era_tag}, {chn}, cats[chn]);

    // Adding background processes. 
    cb.AddProcesses({"*"}, {"htt"}, {era_tag}, {chn}, bkg_procs[chn], cats[chn], false);
    // Include QCD process in em channel for all categories except for CR
    if (chn == "em") {
        cb.AddProcesses({"*"}, {"htt"}, {era_tag}, {chn}, bkgs_em_noCR, exclude_em_ttbar, false);
        //cb.AddProcesses({"*"}, {"htt"}, {era_tag}, {chn}, bkgs_em_noCR, cats[chn], false); // adding back QCD for tests
    }

    cb.AddProcesses({"125"}, {"htt"}, {era_tag}, {chn}, sig_procs[chn], cats[chn], true); // These are signals
  }

  dout("[INFO] Add systematics AddMSSMvsSMRun2Systematics, embedding:", ! no_emb, "  ttbar_rate:", ttbar_rate);
  ch::AddbbHRun2Systematics(cb, ! no_emb, ttbar_rate, era);
  dout("[INFO] Systematics added");
  // Define restriction to the desired category
  if(category != "all"){
    cb = cb.bin({category});
  }

  if(no_shape_systs){
    cb.FilterSysts([&](ch::Systematic *s){
      return s->type().find("shape") != std::string::npos;
    });
  }

  for (string chn : chns) {
    string input_file_base = input_dir[chn] + "htt_bbH.Run" + era_tag + ".root";

    dout("[INFO] Extracting shapes from ", input_file_base);

    // Adding background templates to processes. 
    cb.cp().channel({chn}).backgrounds().ExtractShapes(
      input_file_base, "$BIN/$PROCESS", "$BIN/$PROCESS_$SYSTEMATIC");

    // Adding signal templates to process.
    cb.cp().channel({chn}).process(sig_procs[chn]).ExtractShapes(
      input_file_base, "$BIN/$PROCESS$MASS", "$BIN/$PROCESS$MASS_$SYSTEMATIC");
    

  }

  // Manual rebinning for histograms
  if(manual_rebin && categorization != "mva")
  {
    std::map<std::string, std::map<unsigned int, std::map<unsigned int, std::vector<double> > > >binning_map;
    binning_map["em"] = {};
    binning_map["et"] = {};
    binning_map["mt"] = {};
    binning_map["tt"] = {};

    std::map<unsigned int, std::vector<double> >  binning_map_btag0;
    std::map<unsigned int, std::vector<double> >  binning_map_btagGe1;

    // re-binning (needs to be adjusted later...)
    // start binning from 40 GeV for m_sv 
    // (poor description of data below 40 GeV)
    binning_map_btag0[0]   = { 40., 160., 10.};
    binning_map_btag0[1]   = {160., 200., 20.};
    binning_map_btag0[2]   = {200., 300., 25.};

    binning_map_btagGe1[0] = { 40., 180., 20.};
    binning_map_btagGe1[1] = {180., 300., 40.};

    if ( categorization != "mva" ) {

      binning_map["mt"][12] = binning_map_btag0;
      binning_map["mt"][13] = binning_map_btag0;
      binning_map["mt"][22] = binning_map_btagGe1;
      binning_map["mt"][23] = binning_map_btagGe1;

      binning_map["et"][12] = binning_map_btag0;
      binning_map["et"][13] = binning_map_btag0;
      binning_map["et"][22] = binning_map_btagGe1;
      binning_map["et"][23] = binning_map_btagGe1;

      binning_map["em"][12] = binning_map_btag0;
      binning_map["em"][13] = binning_map_btag0;
      binning_map["em"][14] = binning_map_btag0;
      binning_map["em"][15] = binning_map_btag0;

      binning_map["em"][22] = binning_map_btagGe1;
      binning_map["em"][23] = binning_map_btagGe1;
      binning_map["em"][24] = binning_map_btagGe1;
      binning_map["em"][25] = binning_map_btagGe1;      

      binning_map["tt"][11] = binning_map_btag0;
      binning_map["tt"][21] = binning_map_btagGe1;

      if (categorization == "btag-fine") {

	binning_map["mt"][32] = binning_map_btagGe1;
	binning_map["mt"][33] = binning_map_btagGe1;

	binning_map["et"][32] = binning_map_btagGe1;
	binning_map["et"][33] = binning_map_btagGe1;

	binning_map["em"][32] = binning_map_btagGe1;
	binning_map["em"][33] = binning_map_btagGe1;
	binning_map["em"][34] = binning_map_btagGe1;
	binning_map["em"][35] = binning_map_btagGe1;
	  
	binning_map["tt"][32] = binning_map_btagGe1;

      }
    }

    for(auto chn : chns)
    {
      for(auto b : cb.cp().channel({chn}).bin_id_set())
      {
        std::vector<double> binning = binning_from_map(binning_map[chn][b]);
        if(binning.size() > 0)
        {
            std::cout << "[INFO] Rebinning by hand for discriminator for bin: " << b << " in channel: " << chn << std::endl;
            cb.cp().channel({chn}).bin_id({b}).VariableRebin(binning);
        }
      }
    }
  }

  // Delete processes with 0 yield
  std::cout << "[INFO] Filtering processes with null yield: \n";
  cb.FilterProcs([&](ch::Process *p) {
      bool null_yield = !(p->rate() > 0.0);
      if (null_yield) {
      std::cout << "[WARNING] Removing process with null yield: \n ";
      std::cout << ch::Process::PrintHeader << *p << "\n";
      cb.FilterSysts([&](ch::Systematic *s) {
	  bool remove_syst = (MatchingProcess(*p, *s));
	  return remove_syst;
	});
      }
      return null_yield;
    });

  // Modify systematic variations with yield <= 0
  cb.FilterSysts([&](ch::Systematic *s) {
      // Delete systematics since these result in a bogus norm error in combine for the remaining
      if (s->type() == "shape") {
	if (s->shape_u()->Integral() <= 0.0) {
	  std::cout << "[WARNING] Removing systematic with null yield in up shift:" << std::endl;
	  std::cout << ch::Systematic::PrintHeader << *s << "\n";
	  return true;
	}
	if (s->shape_d()->Integral() <= 0.0) {
	  std::cout << "[WARNING] Removing systematic with null yield in down shift:" << std::endl;
	  std::cout << ch::Systematic::PrintHeader << *s << "\n";
	  return true;
	}
      }
      return false;
    });

  std::cout << "[Info] Summary of process yields: \n ";
  cb.cp().ForEachProc([&](ch::Process *p) {
    std::cout << ch::Process::PrintHeader << *p << "\n";
  });

  // turn all JES+JER+met-unclustered uncertainties into lnN for nbtag categories - should check the met recoil uncertainties as well for small processes
  /*
  std::vector<std::string> jetmet_systs = {
    "CMS_scale_j_Absolute",
    "CMS_scale_j_BBEC1",
    "CMS_scale_j_EC2",
    "CMS_scale_j_FlavorQCD",          
    "CMS_scale_j_HF",
    "CMS_scale_j_RelativeBal",
    "CMS_scale_j_Absolute_2016",
    "CMS_scale_j_Absolute_2017",
    "CMS_scale_j_Absolute_2018",
    "CMS_scale_j_BBEC1_2016",
    "CMS_scale_j_BBEC1_2017",
    "CMS_scale_j_BBEC1_2018",
    "CMS_scale_j_EC2_2016",
    "CMS_scale_j_EC2_2017",
    "CMS_scale_j_EC2_2018",
    "CMS_scale_j_HF_2016", 
    "CMS_scale_j_HF_2017", 
    "CMS_scale_j_HF_2018", 
    "CMS_scale_j_RelativeSample_2016",
    "CMS_scale_j_RelativeSample_2017",
    "CMS_scale_j_RelativeSample_2018",
    "CMS_res_j_2016",
    "CMS_res_j_2017",
    "CMS_res_j_2018",
    "CMS_scale_met_unclustered_2016",
    "CMS_scale_met_unclustered_2017",
    "CMS_scale_met_unclustered_2018",
  };

  // Convert all JES ,JER, and MET uncertainties to lnN except for the ttbar uncertainties in the em, et and mt channels
  // These uncertainties affect MET for the ttbar and diboson so we need to include them as shapes (diboson is small enough to be converted to lnN, and is ttbar in the tt channel)
  // convert all processes except ttbar
  // also convert ttbar in the tt channel
  for(auto u : jetmet_systs) ConvertShapesToLnN (cb.cp().bin_id(btag_cat_bins).channel({"tt","em"}).process({"TTL","TTT","VVL","VVT"}), u);

  // rename MC subtraction uncertainty in the em channel to decorrelate between years and ttbar fraction.
  for (std::string y: {"2016", "2017", "2018"}) {
      cb.cp().channel({"em"}).era({y}).RenameSystematic(cb, "CMS_htt_qcd_iso", "CMS_htt_qcd_iso_"+y);
      cb.cp().channel({"em"}).era({y}).RenameSystematic(cb, "CMS_htt_qcd_extrap", "CMS_htt_qcd_extrap_"+y);
      cb.cp().channel({"em"}).era({y}).RenameSystematic(cb, "CMS_htt_qcd_nonClosure", "CMS_htt_qcd_nonClosure_"+y);

      cb.cp().bin_id(btag_cat_bins).channel({"em"}).era({y}).RenameSystematic(cb, "subtrMC", "subtrMC_lowttbar_"+y);
      cb.cp().bin_id(btag_cat_bins).channel({"em"}).era({y}).RenameSystematic(cb, "subtrMC", "subtrMC_highttbar_"+y);
  }

  std::vector<std::string> met_uncerts = {
    "CMS_htt_boson_scale_met_2016",
    "CMS_htt_boson_res_met_2016",
    "CMS_htt_boson_scale_met_2017",
    "CMS_htt_boson_res_met_2017",
    "CMS_htt_boson_scale_met_2018",
    "CMS_htt_boson_res_met_2018",
  };

  for(auto u : met_uncerts) ConvertShapesToLnN (cb.cp().bin_id(btag_cat_bins).process({"ZTT"}, false), u);
  */
  // fix the negative bins for the remaining processes
  std::cout << "[INFO] Fixing negative bins.\n";
  cb.cp().ForEachProc([](ch::Process *p) {
      if (ch::HasNegativeBins(p->shape())) {
	std::cout << "[WARNING] Fixing negative bins for process: \n ";
	std::cout << ch::Process::PrintHeader << *p << "\n";
	auto newhist = p->ClonedShape();
	ch::ZeroNegativeBins(newhist.get());
	p->set_shape(std::move(newhist), false);
      }
    });

  cb.cp().ForEachSyst([](ch::Systematic *s) {
      if (s->type().find("shape") == std::string::npos)
	return;
      if (ch::HasNegativeBins(s->shape_u()) ||
	  ch::HasNegativeBins(s->shape_d())) {
	std::cout << "[WARNING] Fixing negative bins for systematic: \n ";
	std::cout << ch::Systematic::PrintHeader << *s << "\n";
	auto newhist_u = s->ClonedShapeU();
	auto newhist_d = s->ClonedShapeD();
	ch::ZeroNegativeBins(newhist_u.get());
	ch::ZeroNegativeBins(newhist_d.get());
	s->set_shapes(std::move(newhist_u), std::move(newhist_d), nullptr);
      }
    });

  if (auto_rebin) {
    std::cout << "[INFO] Performing auto-rebinning.\n";
    auto rebin = ch::AutoRebin().SetBinThreshold(0.2).SetBinUncertFraction(0.9).SetRebinMode(1).SetPerformRebin(true).SetVerbosity(1);
    rebin.Rebin(cb, cb);
  }

  // This function modifies every entry to have a standardised bin name of
  // the form: {analysis}_{channel}_{bin_id}_{era}
  ch::SetStandardBinNames(cb, "$ANALYSIS_$CHANNEL_$BINID_$ERA");
  ch::CombineHarvester cb_obs = cb.deep().backgrounds();

  // Adding bin-by-bin uncertainties
  if (use_automc) {
    std::cout << "[INFO] Adding bin-by-bin uncertainties.\n";
    cb.SetAutoMCStats(cb, 0.);
  }

  std::cout << "[INFO] Writing datacards to " << output_folder << std::endl;
    // We need to do this to make sure the ttbarShape uncertainty is added properly when we use a shapeU
  if (ttbar_rate) {
    cb.GetParameter("CMS_htt_ttbarShape")->set_err_d(-1.);
    cb.GetParameter("CMS_htt_ttbarShape")->set_err_u(1.);
  }
  // Decide, how to write out the datacards depending on --category option
  if(category == "all") {
      // Write out datacards. Naming convention important for rest of workflow. We
      // make one directory per chn-cat, one per chn and cmb. In this code we only
      // store the individual datacards for each directory to be combined later.
      ch::CardWriter writer(output_folder + "/" + era_tag + "/$TAG/$BIN.txt",
                            output_folder + "/" + era_tag + "/$TAG/common/htt_input_" + era_tag + ".root");

      // We're not using mass as an identifier - which we need to tell the
      // CardWriter
      // otherwise it will see "*" as the mass value for every object and skip it
      writer.SetWildcardMasses({});

      // Set verbosity
      if (verbose)
        writer.SetVerbosity(1);

      // Write datacards combined and per channel
      writer.WriteCards("cmb", cb);

      for (auto chn : chns) {
        writer.WriteCards(chn, cb.cp().channel({chn}));
      }
  }
  else {
      // Write out datacards. Naming convention important for rest of workflow. We
      // make one directory per chn-cat, one per chn and cmb. In this code we only
      // store the individual datacards for each directory to be combined later.
      ch::CardWriter writer(output_folder + "/" + era_tag + "/$BIN/$BIN.txt",
                            output_folder + "/" + era_tag + "/$BIN/common/$BIN_input.root");

      // We're not using mass as an identifier - which we need to tell the
      // CardWriter
      // otherwise it will see "*" as the mass value for every object and skip it
      writer.SetWildcardMasses({});

      // Set verbosity
      if (verbose)
        writer.SetVerbosity(1);

      writer.WriteCards("", cb);

      ch::CardWriter writer_restore(output_folder + "/restore_binning/$BIN.txt",
                                    output_folder + "/restore_binning/common/$BIN_input.root");

      // We're not using mass as an identifier - which we need to tell the
      // CardWriter
      // otherwise it will see "*" as the mass value for every object and skip it
      writer_restore.SetWildcardMasses({});

      // Set verbosity
      if (verbose)
        writer_restore.SetVerbosity(1);

      writer_restore.WriteCards("", cb_obs);
  }

  if (verbose)
    cb.PrintAll();

  std::cout << "[INFO] Done producing datacards.\n";
}
