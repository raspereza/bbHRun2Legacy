#include "CombineHarvester/bbHRun2Legacy/interface/HttSystematics_bbH.h"
#include "CombineHarvester/CombineTools/interface/Process.h"
#include "CombineHarvester/CombineTools/interface/Systematics.h"
#include "CombineHarvester/CombineTools/interface/Utilities.h"
#include <string>
#include <vector>
#include <fstream>
#include "CombineHarvester/CombineTools/interface/JsonTools.h"

using namespace std;

namespace ch {

using ch::syst::SystMap;
using ch::syst::SystMapAsymm;
using ch::syst::era;
using ch::syst::channel;
using ch::syst::bin_id;
using ch::syst::mass;
using ch::syst::process;
using ch::syst::bin;
using ch::JoinStr;
  
void AddbbHRun2Systematics(CombineHarvester &cb, bool embedding, bool ttbar_rate, int era) {
    
  // ##########################################################################
  // Define groups of signal processes
  // ##########################################################################
  std::vector<std::string> signals_bbH = {
    "bbH"
  };
  std::vector<std::string> signals_ggHbb = {
    "ggHbb","ggHbb125"
  };
  std::vector<std::string> signals_ggH = {
    "ggH125",
  };
  std::vector<std::string> signals_qqH = {
    "qqH125"
  };
  std::vector<std::string> signals_VH = {
    "WH125", "ZH125"
  };
  std::vector<std::string> signals_ggHbbToWW = {
    "ggHbbWW","ggHbbWW125"
  };
  std::vector<std::string> signals_bbHToWW = {
    "bbHWW"
  };
  std::vector<std::string> signals_ggHToWW = {
    "ggHWW125"
  };
  std::vector<std::string> signals_qqHToWW = {
    "qqHWW125"
  };
  std::vector<std::string> signals_VHToWW = {
    "WHWW125", "ZHWW125"
  };
  std::vector<std::string> signals = JoinStr({signals_ggH,signals_qqH,signals_VH});
  std::vector<std::string> signals_HWW = JoinStr({signals_ggHToWW, signals_qqHToWW, signals_VHToWW});

  // All processes being taken from simulation
  std::vector<std::string> mc_processes =
      JoinStr({
	signals_bbH,
	signals_ggHbb,
	signals_bbHToWW,
	signals_ggHbbToWW,  
	signals,
	signals_HWW,
	{"ZTT", "TT", "TTT", "TTL", "TTJ", "W", "ZJ", "ZL", "VV", "VVT", "VVL", "VVJ", "ST"}
              });

  std::vector<int> mva_categories = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // mva categories
  std::vector<int> nobtag_categories = {12,13,14,15}; // no-btag categories
  std::vector<int> btag_categories = {22,23,24,25}; // single-btag categories
  std::vector<int> double_btag_categories = {32,33,34,35}; // double-btag categories
  std::vector<int> all_btag_categories = {22,23,24,25,32,33,34,35}; // single or double btag
  // unreliable estimate of the QCD background in high dzeta btag categories (em channel)
  // TODO : FIX problem analysis-wise 
  std::vector<int> btag_categories_no_high_dzeta = {23,24,25,33,34,35};

  // ##########################################################################
  // Uncertainty: b tagging acceptance uncertainties for pdf and scale and hdamp variations.
  // References:
  // - "Talk in MSSM HTT Meeting by Danny"
  //   (https://indico.cern.ch/event/990440/contributions/4167707/attachments/2167087/3659678/MSSM_signal.pdf)
  //   (file source: https://cernbox.cern.ch/index.php/s/9cgjdpaTeqYEaFZ
  // Notes:
  // ##########################################################################

  cb.cp().process(JoinStr({signals_bbH,signals_bbHToWW})).AddSyst(cb, "pdf_bbH_ACCEPT", "lnN",
	   SystMap<channel,ch::syst::era,bin_id>::init
	   ({"em","et","mt","tt"}, {"2016"}, nobtag_categories, 0.996)
	   ({"em","et","mt","tt"}, {"2017"}, nobtag_categories, 0.995)
	   ({"em","et","mt","tt"}, {"2018"}, nobtag_categories, 0.995)
	   ({"et","mt","tt","em"}, {"2016"}, btag_categories, 1.015)
	   ({"et","mt","tt","em"}, {"2017"}, btag_categories, 1.016)
	   ({"et","mt","tt","em"}, {"2018"}, btag_categories, 1.016)
	   ({"et","mt","tt","em"}, {"2016"}, double_btag_categories, 1.030)
	   ({"et","mt","tt","em"}, {"2017"}, double_btag_categories, 1.031)
	   ({"et","mt","tt","em"}, {"2018"}, double_btag_categories, 1.030));

  cb.cp().process(JoinStr({signals_bbH,signals_bbHToWW})).AddSyst(cb, "QCDscaleAndHdamp_bbH_ACCEPT", "lnN", 
	   SystMapAsymm<channel,ch::syst::era,bin_id>::init
	   ({"em","et","mt","tt"}, {"2016"}, nobtag_categories, 1.007, 0.993)
	   ({"em","et","mt","tt"}, {"2017"}, nobtag_categories, 1.008, 0.992)
	   ({"em","et","mt","tt"}, {"2018"}, nobtag_categories, 1.009, 0.992)
	   ({"et","mt","tt","em"}, {"2016"}, btag_categories, 0.974, 1.026)
	   ({"et","mt","tt","em"}, {"2017"}, btag_categories, 0.972, 1.025)
	   ({"et","mt","tt","em"}, {"2018"}, btag_categories, 0.972, 1.026)
	   ({"et","mt","tt","em"}, {"2016"}, double_btag_categories, 0.974, 1.052)
	   ({"et","mt","tt","em"}, {"2017"}, double_btag_categories, 0.972, 1.050)
	   ({"et","mt","tt","em"}, {"2018"}, double_btag_categories, 0.972, 1.052));

  // ##########################################################################
  // Uncertainty: Lumi
  // References:
  // - "CMS Luminosity Measurements for the 2016 Data Taking Period"
  //   (PAS, https://cds.cern.ch/record/2257069)
  // - Recommendation twiki
  //    https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#LumiComb  
  // Notes:
  // - FIXME: Adapt for fake factor and embedding
  // ##########################################################################

  float lumi_unc = 1.0;
  float lumi_unc_corr = 1.0;
  float lumi_unc_1718 = 1.0;
  if (era == 2016) {
      lumi_unc = 1.010;
      lumi_unc_corr = 1.006;
  } else if (era == 2017) {
      lumi_unc = 1.020;
      lumi_unc_corr = 1.009;
      lumi_unc_1718 = 1.006;
  } else if (era == 2018) {
      lumi_unc = 1.015;
      lumi_unc_corr = 1.020;
      lumi_unc_1718 = 1.002;
  }
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(mc_processes)
      .AddSyst(cb, "lumi_13TeV_$ERA", "lnN", SystMap<>::init(lumi_unc));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(mc_processes)
      .AddSyst(cb, "lumi_13TeV_correlated", "lnN", SystMap<>::init(lumi_unc_corr));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(mc_processes)
      .AddSyst(cb, "lumi_13TeV_1718", "lnN", SystMap<>::init(lumi_unc_1718));

  // ##########################################################################
  // Uncertainty: Prefiring
  // References:
  // - "https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1ECALPrefiringWeightRecipe"
  // Notes:
  // - FIXME: assumed as uncorrelated accross the years for now, what is the recommendation?
  // ##########################################################################
  if (era != 2018) {
    cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(mc_processes)
      .AddSyst(cb, "CMS_prefiring", "shape", SystMap<>::init(1.00));
  }

  // ##########################################################################
  // Uncertainty: Trigger efficiency
  // References:
  // Notes:
  // - FIXME: References?
  // ##########################################################################

  cb.cp()
    .channel({"et"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_trigger_et_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
    .channel({"et"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_xtrigger_l_et_$ERA", "shape", SystMap<>::init(1.00));
  // 100% uncorrelated for embedded
  cb.cp()
    .channel({"et"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_trigger_emb_et_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
    .channel({"et"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_xtrigger_l_emb_et_$ERA", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"mt"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_trigger_mt_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
    .channel({"mt"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_xtrigger_l_mt_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_trigger_em_$ERA", "lnN", SystMap<>::init(1.02));

  // 100% uncorrelated for embedded
  cb.cp()
    .channel({"mt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_trigger_emb_mt_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
    .channel({"mt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_xtrigger_l_emb_mt_$ERA", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"em"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_trigger_emb_em_$ERA", "lnN", SystMap<>::init(1.02));
  
  // Tau trigger efficiencies implemented as shape uncertainties in all channels.
  std::string tauTriggerdmbins[4] = {"0", "1", "10", "11"};
  for (auto tauTriggerbin: tauTriggerdmbins) {
      // lt cross trigger
      cb.cp()
          .channel({"mt", "et"})
          .process(mc_processes)
          .AddSyst(cb, "CMS_eff_xtrigger_t_$CHANNEL_dm"+tauTriggerbin+"_$ERA", "shape", SystMap<>::init(1.00));
          
      cb.cp()
          .channel({"mt", "et"})
          .process({"EMB"})
          .AddSyst(cb, "CMS_eff_xtrigger_t_emb_$CHANNEL_dm"+tauTriggerbin+"_$ERA", "shape", SystMap<>::init(0.866));

      // Correlated component acting on Embedded
      cb.cp()
          .channel({"mt", "et"})
          .process({"EMB"})
          .AddSyst(cb, "CMS_eff_xtrigger_t_$CHANNEL_dm"+tauTriggerbin+"_$ERA", "shape", SystMap<>::init(0.5));
      

      // di-tau trigger
      cb.cp()
          .channel({"tt"})
          .process(mc_processes)
          .AddSyst(cb, "CMS_eff_xtrigger_t_tt_dm"+tauTriggerbin+"_$ERA", "shape", SystMap<>::init(1.00));

      cb.cp()
          .channel({"tt"})
          .process({"EMB"})
          .AddSyst(cb, "CMS_eff_xtrigger_t_emb_tt_dm"+tauTriggerbin+"_$ERA", "shape", SystMap<>::init(0.866));

      // Correlated component acting on Embedded
      cb.cp()
          .channel({"tt"})
          .process({"EMB"})
          .AddSyst(cb, "CMS_eff_xtrigger_t_tt_dm"+tauTriggerbin+"_$ERA", "shape", SystMap<>::init(0.5));

  }
  // ##########################################################################
  // Uncertainty: Electron, muon and tau ID efficiency
  // References:
  // Notes:
  // - FIXME: Adapt for fake factor and embedding
  // - FIXME: Handling of ZL in fully-hadronic channel?
  // - FIXME: References?
  // ##########################################################################

  // 3% in Tau ID SF with different anti-l fake WP
  cb.cp()
    .channel({"mt"})
    .process(JoinStr({signals_bbH, signals_ggHbb, signals, {"EMB", "ZTT", "TTT", "TTL", "VVT", "VVL"}}))
    .AddSyst(cb, "CMS_eff_t_wp_$ERA", "lnN", SystMap<>::init(1.03));
  // tt with double genuine hadronic taus 
  cb.cp()
    .channel({"tt"})
    .process(JoinStr({signals_bbH, signals_ggHbb, signals, {"EMB","ZTT","TTT","VVT"}}))
    .AddSyst(cb, "CMS_eff_t_wp_$ERA", "lnN", SystMap<>::init(1.06));
  // tt with single genuine hadronic tau
  cb.cp()
    .channel({"tt"})
    .process({"TTL","VVL"})
    .AddSyst(cb, "CMS_eff_t_wp_$ERA", "lnN", SystMap<>::init(1.03));

  std::string tauIDdmbins[4] = {"0", "1", "10", "11"};
  // Common component acting on MC
  
  // Electron ID
  cb.cp()
    .channel({"et", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_e", "lnN", SystMap<>::init(1.02));
  
  // Muon ID
  cb.cp()
    .channel({"mt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_eff_m", "lnN", SystMap<>::init(1.02));
  
  // Tau ID: et and mt with 1 real tau
  for (auto tauIDbin : tauIDdmbins){ //first part correlated between channels for IDvsJets
    cb.cp()
      .channel({"et", "mt"})
      .process(JoinStr({signals, signals_bbH, signals_ggHbb, {"ZTT", "TTT", "TTL", "VVT", "VVL"}}))
      .AddSyst(cb, "CMS_eff_t_dm"+tauIDbin+"_$ERA", "shape", SystMap<>::init(1.0));
  }
  cb.cp() //second part uncorrelated between channels for IDvsLep
    .channel({"et", "mt"})
    .process(JoinStr({signals, signals_bbH, signals_ggHbb, {"ZTT", "TTT", "TTL", "VVT", "VVL"}}))
    .AddSyst(cb, "CMS_eff_t_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.01));
  
  // Tau ID: tt with 2 real taus
  for (auto tauIDbin : tauIDdmbins){
    cb.cp()
      .channel({"tt"})
      .process(JoinStr({signals, signals_bbH, signals_ggHbb, {"ZTT", "TTT", "TTL", "VVT", "VVL"}}))
      .AddSyst(cb, "CMS_eff_t_dm"+tauIDbin+"_$ERA", "shape", SystMap<>::init(1.0));
  }
  cb.cp()
    .channel({"tt"})
    .process(JoinStr({signals, signals_bbH, signals_ggHbb, {"ZTT", "TTT", "TTL", "VVT", "VVL"}}))
    .AddSyst(cb, "CMS_eff_t_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.014));
  
  // Component for EMB only
  
  // Electron ID
  cb.cp()
    .channel({"et", "em"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_e_emb", "lnN", SystMap<>::init(1.017));
  
  // Muon ID
  cb.cp()
    .channel({"mt", "em"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_m_emb", "lnN", SystMap<>::init(1.017));

  // Tau ID: et and mt with 1 real tau
  for (auto tauIDbin : tauIDdmbins){
    cb.cp()
      .channel({"et", "mt"})
      .process({"EMB"})
      .AddSyst(cb, "CMS_eff_t_emb_dm"+tauIDbin+"_$ERA", "shape", SystMap<>::init(0.866));
  }
  cb.cp()
    .channel({"et", "mt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_t_emb_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.0087));
  
  // Tau ID: tt with 2 real taus
  for (auto tauIDbin : tauIDdmbins){
    cb.cp()
      .channel({"tt"})
      .process({"EMB"})
      .AddSyst(cb, "CMS_eff_t_emb_dm"+tauIDbin+"_$ERA", "shape", SystMap<>::init(0.866));
  }
  cb.cp()
    .channel({"tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_t_emb_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.012));
  
  
  // Electron ID
  cb.cp()
    .channel({"et", "em"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_e", "lnN", SystMap<>::init(1.01));
  
  // Muon ID
  cb.cp()
    .channel({"mt", "em"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_m", "lnN", SystMap<>::init(1.01));
  
  // Tau ID: et and mt with 1 real tau
  for (auto tauIDbin : tauIDdmbins){
    cb.cp()
      .channel({"et", "mt"})
      .process({"EMB"})
      .AddSyst(cb, "CMS_eff_t_dm"+tauIDbin+"_$ERA", "shape", SystMap<>::init(0.5));
  }
  cb.cp()
    .channel({"et", "mt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_t_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.005));
  
  // Tau ID: tt with 2 real taus
  for (auto tauIDbin : tauIDdmbins){
    cb.cp()
      .channel({"tt"})
      .process({"EMB"})
      .AddSyst(cb, "CMS_eff_t_dm"+tauIDbin+"_$ERA", "shape", SystMap<>::init(0.5));
  }
  cb.cp()
    .channel({"tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_eff_t_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.007));
  
  // ##########################################################################
  // Uncertainty: b-tag and mistag efficiency
  // References:
  // Notes:
  // - FIXME: References?
  // ##########################################################################
  
  // uncertainties as shape systematic (can be optionally converted to lnN
  /*
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_htt_eff_b_$ERA", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_htt_mistag_b_$ERA", "shape", SystMap<>::init(1.00));  
  */
  // ##########################################################################
  // Uncertainty: Electron energy scale
  // References:
  // - MC: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaRunIIRecommendations#E_gamma_Energy_Corrections
  // - Embedding: ?
  // Notes:
  // - FIXME: References for embedding missing, need proper correlation accross years for mc, see here: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaRunIIRecommendations#Recommendations_on_Combining_Sys
  // ##########################################################################
  
  // MC uncorrelated uncertainty
  
  cb.cp()
    .channel({"em", "et"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_e", "shape", SystMap<>::init(1.00));

  // Embedded uncorrelated uncertainty

  cb.cp()
    .channel({"em", "et"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_scale_e_emb", "shape", SystMap<>::init(1.00));
  

  // ##########################################################################
  // Uncertainty: Tau energy scale
  // References:
  // Notes:
  // - Tau energy scale is split by decay mode.
  // - FIXME: References?
  // - FIXME: Need it for H->WW in mt, et, (and tt)?
  // ##########################################################################


  // Common component acting on MC
  std::vector<std::string> tau_es_processes = JoinStr({{"ZTT", "TTT", "TTL", "VVT", "VVL"}, signals, signals_bbH, signals_ggHbb});
  std::vector<std::string> tau_es_processes_emb = {"EMB"};
  
  /*
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes)
    .AddSyst(cb, "CMS_scale_t_1prong_$ERA","shape", SystMap<>::init(1.0));
  
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes)
    .AddSyst(cb, "CMS_scale_t_1prong1pizero_$ERA","shape", SystMap<>::init(1.0));
  
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes)
    .AddSyst(cb, "CMS_scale_t_3prong_$ERA", "shape", SystMap<>::init(1.0));

  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes)
    .AddSyst(cb, "CMS_scale_t_3prong1pizero_$ERA", "shape", SystMap<>::init(1.0));

  // Component for EMB only
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes_emb)
    .AddSyst(cb, "CMS_scale_t_emb_1prong_$ERA", "shape", SystMap<>::init(0.866));

  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes_emb)
    .AddSyst(cb, "CMS_scale_t_emb_1prong1pizero_$ERA", "shape", SystMap<>::init(0.866));
  
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes_emb)
    .AddSyst(cb, "CMS_scale_t_emb_3prong_$ERA", "shape", SystMap<>::init(0.866));
  
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process(tau_es_processes_emb)
    .AddSyst(cb, "CMS_scale_t_emb_3prong1pizero_$ERA", "shape", SystMap<>::init(0.866));
  
  // Common component acting on EMB
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_scale_t_1prong_$ERA", "shape", SystMap<>::init(0.5));

  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_scale_t_1prong1pizero_$ERA", "shape", SystMap<>::init(0.5));
  
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_scale_t_3prong_$ERA", "shape", SystMap<>::init(0.5));
  
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_scale_t_3prong1pizero_$ERA", "shape", SystMap<>::init(0.5));
  */
  // ##########################################################################
  // Uncertainty: Jet energy scale
  // References:
  // - Talk in CMS Htt meeting by Daniel Winterbottom about regional JES splits:
  //   https://indico.cern.ch/event/740094/contributions/3055870/
  // Notes:
  // ##########################################################################

  /*
  // Regional JES
  // uncorrelated between eras
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_Absolute_$ERA", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_BBEC1_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_EC2_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_HF_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_RelativeSample_$ERA", "shape", SystMap<>::init(1.00));
  // correlated between eras
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_Absolute", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_BBEC1", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_EC2", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_HF", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_FlavorQCD", "shape", SystMap<>::init(1.00));
  
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_scale_j_RelativeBal", "shape", SystMap<>::init(1.00));
  
  // JER
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(mc_processes)
    .AddSyst(cb, "CMS_res_j_$ERA", "shape", SystMap<>::init(1.00));
  */  

  // ##########################################################################
  // Uncertainty: MET energy scale and Recoil
  // References:
  // Notes:
  // - FIXME: Clustered vs unclustered MET? Inclusion of JES splitting?
  // - FIXME: References?
  // ##########################################################################
  /*
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({"TT", "TTT", "TTL", "TTJ", "VV", "VVT", "VVL", "VVJ", "ST"})
    .AddSyst(cb, "CMS_scale_met_unclustered_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(JoinStr({signals, signals_bbH, signals_ggHbb, signals_HWW, signals_bbHToWW, signals_ggHbbToWW, {"ZTT", "ZL", "ZJ", "W"}}))
    .AddSyst(cb, "CMS_htt_boson_scale_met_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(JoinStr({signals, signals_bbH, signals_ggHbb, signals_HWW, signals_bbHToWW, signals_ggHbbToWW, {"ZTT", "ZL", "ZJ", "W"}}))
    .AddSyst(cb, "CMS_htt_boson_res_met_$ERA", "shape", SystMap<>::init(1.00));

  // met uncertainty templates are included from taking 100% variation in the correction
  // these are scaled here to take the correct 1-sigma ranges
  
  // small uncertainty decorrelated by channel to account for statistical uncertainties on corrections, enlarged to cover differences observed between corrections for et and mt channels 
  // comment for now
  /*
  cb.cp()
    .process({"EMB"})
    .channel({"et", "mt", "tt"})
    .AddSyst(cb, "scale_embed_met_$CHANNEL_$ERA", "shape", SystMap<>::init(0.25)); 
  */
  // the other component of the uncertainty is systematic and correlated between channels (but decorrelated by era) 
  // comment for now
  /*
  cb.cp()
    .process({"EMB"})
    .channel({"tt","mt","et"})
    .era({"2016"})
    .AddSyst(cb, "scale_embed_met_$ERA", "shape", SystMap<>::init(0.36));
  cb.cp()
    .process({"EMB"})
    .bin_id(mssm_categories)
    .channel({"tt","mt","et"})
    .era({"2017"})
    .AddSyst(cb, "scale_embed_met_$ERA", "shape", SystMap<>::init(0.64));
  cb.cp()
    .process({"EMB"})
    .bin_id(mssm_categories)
    .channel({"tt","mt","et"})
    .era({"2018"})
    .AddSyst(cb, "scale_embed_met_$ERA", "shape", SystMap<>::init(0.14));
  */

  // ##########################################################################
  // Uncertainty: Background normalizations
  // References:
  // Notes:
  // - FIXME: Remeasure QCD extrapolation factors for SS and ABCD methods?
  //          Current values are measured by KIT.
  // - FIXME: Adapt for fake factor and embedding
  // - FIXME: W uncertainties: Do we need lnN uncertainties based on the Ersatz
  //          study in Run1 (found in HIG-16043 uncertainty model)
  // - FIXME: References?
  // ##########################################################################

  // VV
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"VVT", "VVJ", "VVL", "VV", "ST"})
      .AddSyst(cb, "CMS_htt_vvXsec", "lnN", SystMap<>::init(1.05));
  if (ttbar_rate){
    // use unconstrained rate parameter for ttbar yield
    // We don't need above uncertainty on cross section if using the rate parameter
    cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"TTT", "TTL", "TTJ", "TT"})
      .AddSyst(cb, "rate_ttbar","rateParam",SystMap<>::init(1.0));
    cb.GetParameter("rate_ttbar")->set_range(0.5,1.5);
    
    // We can also remove the lumi and em trigger uncertainties for ttbar if using the rate parameter
    cb.FilterSysts([](ch::Systematic *syst) {
        return (syst->name().find("lumi") != string::npos || syst->name().find("CMS_eff_trigger_em") != string::npos) &&
	  (syst->process() == "TT" || syst->process() == "TTT" || syst->process() == "TTL" || syst->process() == "TTJ");
      });
  }
  else {
    // TT
    cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"TTT", "TTL", "TTJ", "TT"})
      .AddSyst(cb, "CMS_htt_tjXsec", "lnN", SystMap<>::init(1.06));
  }
  // W
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({"W"})
    .AddSyst(cb, "CMS_htt_wjXsec", "lnN", SystMap<>::init(1.04));

  // Z
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"ZTT", "ZL", "ZJ"})
      .AddSyst(cb, "CMS_htt_zjXsec", "lnN", SystMap<>::init(1.02));

  cb.cp()
      .channel({"em"})
      .process({"QCD"})
      .AddSyst(cb, "CMS_htt_qcd_0jet_rate_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
      .channel({"em"})
      .process({"QCD"})
      .AddSyst(cb, "CMS_htt_qcd_0jet_shape_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
      .channel({"em"})
      .process({"QCD"})
      .AddSyst(cb, "CMS_htt_qcd_0jet_shape2_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
      .channel({"em"})
      .process({"QCD"})
      .AddSyst(cb, "CMS_htt_qcd_1jet_rate_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
      .channel({"em"})
      .process({"QCD"})
      .AddSyst(cb, "CMS_htt_qcd_1jet_shape_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
      .channel({"em"})
      .process({"QCD"})
      .AddSyst(cb, "CMS_htt_qcd_1jet_shape2_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
     .channel({"em"})
     .process({"QCD"})
     .AddSyst(cb, "CMS_htt_qcd_2jet_rate_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
     .channel({"em"})
     .process({"QCD"})
     .AddSyst(cb, "CMS_htt_qcd_2jet_shape_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
     .channel({"em"})
     .process({"QCD"})
     .AddSyst(cb, "CMS_htt_qcd_2jet_shape2_$ERA", "shape", SystMap<>::init(1.00));
  cb.cp()
     .channel({"em"})
     .process({"QCD"})
     .AddSyst(cb, "CMS_htt_qcd_iso", "shape", SystMap<>::init(1.00));
  cb.cp()
    .channel({"em"})
    .process({"QCD"})
    .AddSyst(cb, "CMS_htt_qcd_nonClosure", "shape", SystMap<bin_id>::init(btag_categories_no_high_dzeta,1.00));
  cb.cp()
    .channel({"em"})
    .process({"QCD"})
    .AddSyst(cb, "CMS_htt_qcd_extrap", "lnN", SystMap<>::init(1.15));

    // em closure correction uncertainties in btag categories.
    // from https://indico.cern.ch/event/999841/contributions/4199219/attachments/2176453/3675294/MSSM_HTT_20210122.pdf
  cb.cp()
    .channel({"em"})
    .process({"QCD"})
    .AddSyst(cb, "CMS_htt_qcd_nbtag_closure_stat_$ERA", "lnN", SystMap<bin_id>::init
	     (all_btag_categories, 1.07));
  cb.cp()
    .channel({"em"})
    .process({"QCD"})
    .AddSyst(cb, "CMS_htt_qcd_nbtag_closure_syst", "lnN", SystMap<bin_id>::init
	     (all_btag_categories, 1.05));
  cb.cp()
    .channel({"em"})
    .bin_id({22},false)
    .process({"QCD"})
    .AddSyst(cb, "subtrMC", "shape", SystMap<bin_id>::init(btag_categories_no_high_dzeta,1.00));

  cb.cp()
    .channel({"em"})
    .process({"W"})
    .AddSyst(cb, "CMS_htt_fake_em_$ERA", "lnN", SystMap<>::init(1.15));
  
  cb.cp()
    .channel({"em"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_htt_ZL_fake_em_$ERA", "lnN", SystMap<>::init(1.2));

  // ##########################################################################
  // Uncertainty: Drell-Yan LO->NLO reweighting
  // References:
  // Notes:
  // - FIXME: References?
  // ##########################################################################

  if (era == 2016) {
      cb.cp()
	.channel({"et", "mt", "tt", "em"})
	.process({"ZTT", "ZL", "ZJ"})
	.AddSyst(cb, "CMS_htt_dyShape_$ERA", "shape", SystMap<>::init(0.10));
  } else {
    cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"ZTT", "ZL", "ZJ"})
      .AddSyst(cb, "CMS_htt_dyShape", "shape", SystMap<>::init(0.10));
  }

  // ##########################################################################
  // Uncertainty: TT shape reweighting
  // References:
  // Notes:
  // - FIXME: References?
  // ##########################################################################

  if (ttbar_rate) {
    cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"TTT", "TTL", "TTJ", "TT"})
      .AddSyst(cb, "CMS_htt_ttbarShape", "shapeU", SystMap<>::init(1.00));
    cb.GetParameter("CMS_htt_ttbarShape")->set_range(-1.0,1.0);
  }  
  else {
    cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"TTT", "TTL", "TTJ", "TT"})
      .AddSyst(cb, "CMS_htt_ttbarShape", "shape", SystMap<>::init(1.00));
  }

  // ##########################################################################
  // Uncertainty: Electron/muon to tau fakes and ZL energy scale
  // References:
  // Notes:
  // - FIXME: References?
  // ##########################################################################

  // ZL energy scale split by decay mode
  cb.cp()
    .channel({"mt"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong_$ERA", "shape",
	     SystMap<>::init(1.00));

  cb.cp()
    .channel({"mt"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong1pizero_$ERA", "shape",
	     SystMap<>::init(1.00));
  /*
  cb.cp()
      .channel({"et"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong_barrel_$ERA", "shape",
               SystMap<>::init(1.00));

  cb.cp()
      .channel({"et"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong1pizero_barrel_$ERA", "shape",
               SystMap<>::init(1.00));
  cb.cp()
      .channel({"et"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong_endcap_$ERA", "shape",
               SystMap<>::init(1.00));

  cb.cp()
      .channel({"et"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong1pizero_endcap_$ERA", "shape",
               SystMap<>::init(1.00));
  */
  //single eta bin for now: 
  cb.cp()
    .channel({"et"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong_$ERA", "shape",
	     SystMap<>::init(1.00));

  cb.cp()
    .channel({"et"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_ZLShape_$CHANNEL_1prong1pizero_$ERA", "shape",
	     SystMap<>::init(1.00));
  

  // Lepton fake rate uncertainties are kept as shape uncertainties for SM categories to match HIG-19-010 but converted to lnN uncertainties for MSSM categories

  // Electron fakes
  cb.cp()
    .channel({"et"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_fake_e_BA_$ERA", "shape",
	     SystMap<>::init(1.00));
  cb.cp()
    .channel({"et"})
    .process({"ZL"})
    .AddSyst(cb, "CMS_fake_e_EC_$ERA", "shape",
	     SystMap<>::init(1.00));

  // Muon fakes
  cb.cp()
      .channel({"mt"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_fake_m_WH1_$ERA", "shape",
               SystMap<>::init(1.00));
  cb.cp()
      .channel({"mt"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_fake_m_WH2_$ERA", "shape",
               SystMap<>::init(1.00));
  cb.cp()
      .channel({"mt"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_fake_m_WH3_$ERA", "shape",
               SystMap<>::init(1.00));
  cb.cp()
      .channel({"mt"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_fake_m_WH4_$ERA", "shape",
               SystMap<>::init(1.00));
  cb.cp()
      .channel({"mt"})
      .process({"ZL"})
      .AddSyst(cb, "CMS_fake_m_WH5_$ERA", "shape",
               SystMap<>::init(1.00));

  // ##########################################################################
  // Uncertainty: Theory uncertainties
  // References:
  // - Gluon-fusion WG1 uncertainty scheme:
  //   https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWG/SignalModelingTools
  // Notes:
  // - FIXME: WG1 scheme currently NOT applied to ggHWW -> on purpose?
  // - FIXME: Add TopMassTreatment from HIG-16043 uncertainty model
  // - FIXME: Compare to HIG-16043 uncertainty model:
  //           - PDF uncertainties split by category?
  //           - QCDUnc uncertainties?
  //           - UEPS uncertainties?
  // - FIXME: Check VH QCD scale uncertainty
  // - FIXME: References?
  // ##########################################################################
  //

  // Uncertainty on branching ratio for HTT at 125 GeV
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(JoinStr({signals, signals_bbH, signals_ggHbb}))
      .AddSyst(cb, "BR_htt_THU", "lnN", SystMap<>::init(1.017));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(JoinStr({signals, signals_bbH, signals_ggHbb}))
      .AddSyst(cb, "BR_htt_PU_mq", "lnN", SystMap<>::init(1.0099));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(JoinStr({signals, signals_bbH, signals_ggHbb}))
      .AddSyst(cb, "BR_htt_PU_alphas", "lnN", SystMap<>::init(1.0062));

  // Uncertainty on branching ratio for HWW at 125 GeV
  cb.cp()
     .channel({"et", "mt", "tt", "em"})
     .process(JoinStr({signals_HWW, signals_bbHToWW, signals_ggHbbToWW}))
     .AddSyst(cb, "BR_hww_THU", "lnN", SystMap<>::init(1.0099));
  cb.cp()
     .channel({"et", "mt", "tt", "em"})
     .process(JoinStr({signals_HWW, signals_bbHToWW, signals_ggHbbToWW}))
     .AddSyst(cb, "BR_hww_PU_mq", "lnN", SystMap<>::init(1.0099));
  cb.cp()
     .channel({"et", "mt", "tt", "em"})
     .process(JoinStr({signals_HWW, signals_bbHToWW, signals_ggHbbToWW}))
     .AddSyst(cb, "BR_hww_PU_alphas", "lnN", SystMap<>::init(1.0066));

  // theory uncertainty in gg->H+bb (for now use symmetric unc.)
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process(JoinStr({signals_ggHbb,signals_ggHbbToWW}))
      .AddSyst(cb, "QCDScale_ggHbb", "lnN", SystMap<>::init(1.40));


  // QCD scale (no ggH & qqH signals for tautau decay channel) for 125 GeV Higgs
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"ZH125", "Zh", "ZH", "ZH1", "ZHWW125"})
      .AddSyst(cb, "QCDScale_VH", "lnN", SystMap<>::init(1.009));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"WH125", "Wh", "WH", "WH1", "WHWW125"})
      .AddSyst(cb, "QCDScale_VH", "lnN", SystMap<>::init(1.008));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"ttH125"})
      .AddSyst(cb, "QCDScale_ttH", "lnN", SystMap<>::init(1.08));
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"bbH","bbHWW"})
      .AddSyst(cb, "QCDScale_bbH", "lnN", SystMap<>::init(1.22));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({signals_ggHToWW})
    .AddSyst(cb, "QCDScale_ggH", "lnN", SystMap<>::init(1.039));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({signals_qqHToWW})
    .AddSyst(cb, "QCDScale_qqH", "lnN", SystMap<>::init(1.005));

  // PDF for 125 GeV Higgs
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(JoinStr({signals_ggH,signals_ggHToWW,signals_ggHbb,signals_ggHbbToWW}))
    .AddSyst(cb, "pdf_Higgs_gg", "lnN", SystMap<>::init(1.032));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process(JoinStr({signals_qqH,signals_qqHToWW}))
    .AddSyst(cb, "pdf_Higgs_qqbar", "lnN", SystMap<>::init(1.021));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({"ZH125", "Zh", "ZH", "ZH1", "ZHWW125"})
    .AddSyst(cb, "pdf_Higgs_VH", "lnN", SystMap<>::init(1.013));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({"WH125", "Wh", "WH", "WH1", "WHWW125"})
    .AddSyst(cb, "pdf_Higgs_VH", "lnN", SystMap<>::init(1.018));
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({"ttH125"})
    .AddSyst(cb, "pdf_Higgs_ttH", "lnN", SystMap<>::init(1.036));

  // No pdf uncertainty for bbH125 available from LHCHWG file

  // ##########################################################################
  // Uncertainty: Embedded events
  // References:
  // - https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauTauEmbeddingSamples2016
  // Notes:
  // ##########################################################################

  // Embedded Normalization: No Lumi, Zjxsec information used, instead derived from data using dimuon selection efficiency
  cb.cp()
      .channel({"et", "mt", "tt", "em"})
      .process({"EMB"})
      .AddSyst(cb, "CMS_htt_doublemutrg_$ERA", "lnN", SystMap<>::init(1.04));

  // TTbar contamination in embedded events: 10% shape uncertainty of assumed ttbar->tautau event shape
  cb.cp()
    .channel({"et", "mt", "tt", "em"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_htt_emb_ttbar_$ERA", "shape", SystMap<>::init(1.00));

  // Uncertainty of hadronic tau track efficiency correction
  // uncorrelated between eras (should be added later)
  /*
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_3ProngEff_$ERA", "shape", SystMap<>::init(1.0));

  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"EMB"})
    .AddSyst(cb, "CMS_1ProngPi0Eff_$ERA", "shape", SystMap<>::init(1.0));
  */

  // ##########################################################################
  // Uncertainty: Jet fakes
  // from CP H->tautau analysis
  // ##########################################################################
  std::string jet_bins[3] = {"njets0", "njets1","njets2"};
  //  std::string dm_bins[4] = {"dm0", "dm1","dm10","dm11"};
  std::string dm_bins[3] = {"dm0", "dm1","dm10"};
  std::string qcd_uncs[2] = {"unc1", "unc2"};
  std::string wjets_uncs[2] = {"unc1", "unc2"}; 
  std::string ttbar_uncs[2] = {"unc1", "unc2"}; 
  
  // QCD shape stat.
  for (auto njet: jet_bins) {
    for (auto unc: qcd_uncs) {
      for (auto dm : dm_bins) {
	cb.cp()
	  .channel({"et", "mt", "tt"})
	  .process({"jetFakes"})
	  .AddSyst(cb, "CMS_ff_total_qcd_stat_"+unc+"_"+njet+"_"+dm+"_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));
      }
    }
  }

  // W shape stat.
  for (auto njet: jet_bins) {
    for (auto unc: wjets_uncs) {
      for (auto dm : dm_bins) {
	cb.cp()
	  .channel({"et", "mt"})
	  .process({"jetFakes"})
	  .AddSyst(cb, "CMS_ff_total_wjets_stat_"+unc+"_"+njet+"_"+dm+"_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));
      }
    }
  }

  // TT shape stat.
  for (auto njet: jet_bins) {
    for (auto unc: ttbar_uncs) {
      for (auto dm : dm_bins) {
	cb.cp()
	  .channel({"et", "mt"})
	  .process({"jetFakes"})
	  .AddSyst(cb, "CMS_ff_total_ttbar_stat_"+unc+"_"+njet+"_"+dm+"_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));
      }
    }
  }
  
  // MET non-closure unc.
  cb.cp()
    .channel({"et", "mt", "tt"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_qcd_met_closure_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"et", "mt"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_wjets_met_closure_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"et", "mt"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_ttbar_met_closure_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  // subleading tau pt non-closure unc.
  cb.cp()
    .channel({"tt"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_qcd_pt2_closure_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  // lepton (e,mu) pt non-closure unc.
  cb.cp()
    .channel({"mt","et"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_qcd_l_pt_closure_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"mt","et"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_wjets_l_pt_closure_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));
  
  // unc. related to extrapolation from SS (DR) to OS (AR)
  cb.cp()
    .channel({"mt","et","tt"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_qcd_osss_extrap_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"mt","et"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_wjets_osss_extrap_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"mt","et"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_ttbar_osss_extrap_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  // unc. related to subtraction of l->fake and genuine tau contribution
  cb.cp()
    .channel({"mt","et","tt"})
    .process({"jetFakes"})
    .AddSyst(cb, "CMS_ff_total_subtr_syst_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  // single fakes for tt channel
  cb.cp()
    .channel({"tt"})
    .process({"wFakes"})
    .AddSyst(cb, "CMS_ff_wfakes_syst_$CHANNEL_$ERA", "lnN", SystMap<>::init(1.20));

  // l->tau fakes for tt channel
  cb.cp()
    .channel({"tt"})
    .process({"TTL","VVL","ZL"})
    .AddSyst(cb, "CMS_htt_fake_m_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

  cb.cp()
    .channel({"tt"})
    .process({"TTL","VVL","ZL"})
    .AddSyst(cb, "CMS_htt_fake_e_$CHANNEL_$ERA", "shape", SystMap<>::init(1.00));

}
} // namespace ch
