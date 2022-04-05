import CombineHarvester.CombineTools.ch as ch

def AddCommonSystematics(cb, year):
  backgrounds = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  bbhsignals = ['bbH','bbH125','bbHWW125']
  mc_processes = ['bbH','bbH125','bbHWW125','JJH','jjH','jjH_inc','ggjjH','ggH','ggH125','ZL','TTL','VVL','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF']
  nojetfakes = ['bbH','bbH125','bbHWW125','JJH','ggH','ggH125','ZL','TTL','VVL','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','EMB']
  httprocs = ['bbH','bbH125','JJH','ggH','ggH125','ZH','VBF','qqH125']
  hwwprocs = ['bbHWW125','ggHWW125','qqHWW125']


  #Signal theory uncertainties
  cb.cp().process(bbhsignals).AddSyst(cb,'QCDscale_bbH','lnN', ch.SystMap()((0.76,1.201)))
  cb.cp().process(['JJH','ggH125','ggHbbWW125','ggHbb125','ggH']).AddSyst(cb,'QCDscale_ggH','lnN', ch.SystMap()((0.93,1.046)))
  cb.cp().process(['JJH','ggH125','ggHbbWW125','ggHbb125','ggH']).AddSyst(cb,'pdf_Higgs_ggH','lnN', ch.SystMap()(1.032))
  #Additional uncertainty for ggH+2b 
  cb.cp().process(['ggH','ggHbb125','ggHbbWW125']).AddSyst(cb,'QCDscale_ggHbb','lnN',ch.SystMap()(1.40))

  #Need to double check these ones 
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_THU','lnN', ch.SystMap()(1.017))
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_PU_mq','lnN', ch.SystMap()(1.0099))
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_PU_alphas','lnN', ch.SystMap()(1.0062))

  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_THU','lnN', ch.SystMap()(1.0099))
  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_PU_mq','lnN', ch.SystMap()(1.0099))
  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_PU_alphas','lnN', ch.SystMap()(1.0066))

  cb.cp().process(['ZH125','ZH','ZH1','ZHWW125']).AddSyst(cb,'QCDscale_VH','lnN',ch.SystMap()(1.009))
  cb.cp().process(['ZH125','ZH','ZH1','ZHWW125']).AddSyst(cb,'pdf_Higgs_VH','lnN',ch.SystMap()(1.013))
  cb.cp().process(['WH125','WH','WH1','WHWW125']).AddSyst(cb,'QCDscale_VH','lnN',ch.SystMap()(1.008))
  cb.cp().process(['WH125','WH','WH1','WHWW125']).AddSyst(cb,'pdf_Higgs_VH','lnN',ch.SystMap()(1.018))
  cb.cp().process(['ttH125']).AddSyst(cb,'QCDscale_ttH','lnN',ch.SystMap()(1.08))
  cb.cp().process(['ttH125']).AddSyst(cb,'pdf_Higgs_ttH','lnN',ch.SystMap()(1.036))
  cb.cp().process(['VBF','qqH125','qqHWW125']).AddSyst(cb,'QCDscale_qqH','lnN',ch.SystMap()(1.005))
  cb.cp().process(['VBF','qqH125','qqHWW125']).AddSyst(cb,'pdf_Higgs_qqbar','lnN',ch.SystMap()(1.021))


  #Tau trigger efficiency 
  tautriggerdmbins = ["0","1","10","11"]
  for taubin in tautriggerdmbins:
     cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))
     cb.cp().process(["EMB"]).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_emb_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))
     cb.cp().process(["EMB"]).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))

  #Tau ID
  cb.cp().process(nojetfakes).channel(['mt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))
  cb.cp().process(['bbH','bbH125','bbHWW125','JJH','ggH','ggH125','EMB','ZTT','TTT','VVT']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.06))
  cb.cp().process(['TTL','VVL']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))

  #Electron ID
  cb.cp().process(mc_processes).channel(['et','em']).AddSyst(cb,"CMS_eff_e","lnN",ch.SystMap()(1.02))

  #Muon ID
  cb.cp().process(mc_processes).channel(['mt','em']).AddSyst(cb,"CMS_eff_m","lnN",ch.SystMap()(1.02))
  
  for taubin in tautriggerdmbins:
    #cb.cp().process(mc_processes).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+"_"+year,'shape',ch.SystMap()(1.0))
    cb.cp().process(mc_processes).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year,'lnN',ch.SystMap()(1.01))
    cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+'_'+year, 'shape', ch.SystMap()(1.0))
    cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year, 'lnN', ch.SystMap()(1.014))
  
  #EMB lepton ID
  cb.cp().process(['EMB']).channel(['et','em']).AddSyst(cb,'CMS_eff_e_emb','lnN',ch.SystMap()(1.017))
  cb.cp().process(['EMB']).channel(['et','em']).AddSyst(cb,'CMS_eff_e','lnN',ch.SystMap()(1.01))
  cb.cp().process(['EMB']).channel(['mt','em']).AddSyst(cb,'CMS_eff_m_emb', 'lnN',ch.SystMap()(1.017))
  cb.cp().process(['EMB']).channel(['mt','em']).AddSyst(cb,'CMS_eff_m', 'lnN',ch.SystMap()(1.01))
  for taubin in tautriggerdmbins:
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_emb_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.866))
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.5))
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_emb_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.0087))
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.005))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_emb_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.866))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.5))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_emb_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.012))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.007))
  
  #Ele ES  
  cb.cp().channel(['em']).process(mc_processes).AddSyst(cb,'CMS_scale_e','shape',ch.SystMap()(1.0)) #Maybe also apply to et but don't have it at the moment
  cb.cp().channel(['em','et']).process('EMB').AddSyst(cb,'CMS_scale_e_emb','shape',ch.SystMap()(1.0)) #Maybe also apply to et but don't have it at the moment

  #Missing: btag, JES, MET, etc.

  #Bkg normalisations
  cb.cp().channel(['et','mt','tt','em']).process(['VVT','VVJ','VVL','VV','ST']).AddSyst(cb,'CMS_htt_vvXsec','lnN',ch.SystMap()(1.05))
  cb.cp().channel(['et','mt','tt','em']).process(['TTT','TTL','TTJ','TT']).AddSyst(cb,'CMS_htt_tjXsec','lnN',ch.SystMap()(1.06))
  cb.cp().channel(['et','mt','tt','em']).process(['W','WJets']).AddSyst(cb,'CMS_htt_wjXsec','lnN',ch.SystMap()(1.04))
  cb.cp().channel(['et','mt','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'CMS_htt_zjXsec','lnN',ch.SystMap()(1.02))

  #emu QCD  
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_0jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_0jet_shape_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_0jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_1jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_1jet_shape_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_1jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_2jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_2jet_shape_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_2jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_iso','shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_qcd_extrap','lnN',ch.SystMap()(1.15)) 
  cb.cp().channel(['em']).process(['W']).AddSyst(cb,'CMS_htt_fake_em_'+year,'lnN',ch.SystMap()(1.15)) 
  cb.cp().channel(['em']).process(['ZL']).AddSyst(cb,'CMS_htt_ZL_fake_em_'+year,'lnN',ch.SystMap()(1.2)) 

   
  cb.cp().channel(['tt','em']).process(['TTT','TTL','TTJ','TT']).AddSyst(cb,'CMS_htt_ttbarShape','shape',ch.SystMap()(1.0))  #Not present in et,mt

  #cb.cp().channel(['mt']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['mt']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong1pizero_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong_barrel_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong1pizero_barrel_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong_endcap_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong1pizero_endcap_'+year,'shape',ch.SystMap()(1.0)) 


  cb.cp().process(['EMB']).AddSyst(cb,'CMS_htt_doublemutrg_'+year,'lnN',ch.SystMap()(1.04)) 
  cb.cp().process(['EMB']).AddSyst(cb,'CMS_htt_emb_ttbar_'+year,'shape',ch.SystMap()(1.00)) 
  #cb.cp().channel(['et','mt','tt']).process(['EMB']).AddSyst(cb,'CMS_3ProngEff_'+year,'shape',ch.SystMap()(1.00)) 
  #cb.cp().channel(['et','mt','tt']).process(['EMB']).AddSyst(cb,'CMS_1ProngPi0Eff_'+year,'shape',ch.SystMap()(1.00)) 

  #jetFake uncs
  jetbins = ['njets0','njets1','njets2']
  dmbins = ['dm0','dm1','dm10']
  qcduncs = ['unc1','unc2']

  for jbin in jetbins:
    for unc in qcduncs:
      for dm in dmbins:
        cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_ff_total_qcd_stat_'+unc+'_'+jbin+'_'+dm+'_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))

  

  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_ff_total_qcd_met_closure_syst_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_ff_total_qcd_pt2_closure_syst_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_ff_total_qcd_osss_extrap_syst_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_ff_total_subtr_syst_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  #cb.cp().channel(['tt']).process(['wFakes']).AddSyst(cb,'CMS_ff_wfakes_syst_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['TTL','VVL','ZL']).AddSyst(cb,'CMS_htt_fake_m_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['TTL','VVL','ZL']).AddSyst(cb,'CMS_htt_fake_e_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  

def AddSystematics2018(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  bbhsignals = ['bbH','bbH125','bbHWW125']
  mc_processes = ['bbH','bbH125','bbHWW125','JJH','jjH','jjH_inc','ggjjH','ggH','ggH125','ZL','TTL','VVL','wFakes','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','JJH',"W","WH125","WHWW125","ZH125","ZHWW125"]

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2018','lnN', ch.SystMap()(1.015))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.02))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.002))

  cb.cp().process(['ZTT','ZL','ZJ']).channel(["tt","em"]).AddSyst(cb, 'CMS_htt_dyShape', 'shape', ch.SystMap()(0.10)) #FIXME not present in mt,et

def AddSystematics2017(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  bbhsignals = ['bbH','bbH125','bbHWW125']
  mc_processes = ['bbH','bbH125','bbHWW125','JJH','jjH','jjH_inc','ggjjH','ggH','ggH125','ZL','TTL','VVL','wFakes','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','JJH',"W","WH125","WHWW125","ZH125","ZHWW125"]
  mc_processes_nowfakes = ['bbH','bbH125','bbHWW125','JJH','jjH','jjH_inc','ggjjH','ggH','ggH125','ZL','TTL','VVL','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','JJH',"W","WH125","WHWW125","ZH125","ZHWW125"]

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2017','lnN', ch.SystMap()(1.020))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.009))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))

  cb.cp().process(mc_processes_nowfakes).channel(["tt","em"]).AddSyst(cb, 'CMS_prefiring', 'shape', ch.SystMap()(1.0))

  cb.cp().process(['ZTT','ZL','ZJ']).channel(["tt","em"]).AddSyst(cb, 'CMS_htt_dyShape', 'shape', ch.SystMap()(0.10)) #FIXME not present in mt,et
  


def AddSystematics2016(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  bbhsignals = ['bbH','bbH125','bbHWW125']
  mc_processes = ['bbH','bbH125','bbHWW125','JJH','jjH','jjH_inc','ggjjH','ggH','ggH125','ggHbb125', 'ggHbbWW125', 'ZL','TTL','VVL','wFakes','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','JJH',"WH125","WHWW125","ZH125","ZHWW125"]
  mc_processes_nowfakes = ['bbH','bbH125','bbHWW125','JJH','jjH','jjH_inc','ggjjH','ggH','ggH125','ZL','TTL','VVL','wFakes','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','JJH',"WH125","WHWW125","ZH125","ZHWW125"]

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2016','lnN', ch.SystMap()(1.010))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.006))

  cb.cp().process(mc_processes_nowfakes).channel(["tt","em"]).AddSyst(cb, 'CMS_prefiring', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['ZTT','ZL','ZJ']).channel(["tt","em"]).AddSyst(cb, 'CMS_htt_dyShape_2016', 'shape', ch.SystMap()(0.10)) #FIXME not present in mt,et

