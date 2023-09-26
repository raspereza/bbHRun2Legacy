import CombineHarvester.CombineTools.ch as ch


bbhsignals = ['bbH_htt','ggH_bb_htt','intH_bb_htt','ggH_htt','intH_htt','bbH_hww','ggH_bb_hww','intH_bb_hww','ggH_hww','intH_hww']
httprocs_sig = ['bbH_htt','ggH_bb_htt','intH_bb_htt','ggH_htt','intH_htt']
hwwprocs_sig = ['bbH_hww','ggH_bb_hww','intH_bb_hww','ggH_hww','intH_hww']

h125ttprocs = ['ggH_htt','qqH_htt','WH_htt','ZH_htt','ttH_htt','qqH125','WH125','ZH125','TTH125','ttH','TTH','ttH125','VBF']
#h125wwprocs = ['ggH_hww','qqH_hww','ttH_hww','ZH_hww','WH_hww','qqHWW125','TTHWW125','WHWW125','ZHWW125']
h125wwprocs = ['ggH_hww','qqH_hww','ttH_hww','ZH_hww','WH_hww','qqHWW125','TTHWW125']
  
httprocs = httprocs_sig + h125ttprocs 
hwwprocs = h125wwprocs + hwwprocs_sig 

nojetfakes = httprocs + hwwprocs + ['EMB','DYJets','ZTT','ZL','ST','TT','TTL','TTT','VVL','VV','W','TTVJets']
  

mc_processes = httprocs + hwwprocs + ['DYJets','ZTT','ZL','ZJ','ST','TT','TTL','TTT','TTJ','VVL','VV','W','TTVJets']


def AddCommonSystematics(cb, year):
  backgrounds = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()


  #Signal theory uncertainties
  cb.cp().process(bbhsignals).AddSyst(cb,'QCDscale_bbH','lnN', ch.SystMap()((0.76,1.201)))
  cb.cp().process(['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt','ggH_bb_hww','ggH_hww']).AddSyst(cb,'QCDscale_ggH','lnN', ch.SystMap()((0.93,1.046)))
  cb.cp().process(['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt','ggH_bb_hww','ggH_hww']).AddSyst(cb,'pdf_Higgs_ggH','lnN', ch.SystMap()(1.032))

  #Additional uncertainty for ggH+2b 
  # cb.cp().process(['ggH_bb_htt','ggH_bb_hww']).AddSyst(cb,'QCDscale_ggHbb','lnN',ch.SystMap()(1.40))
  # taken from  arXiv:1808.01660v3 (table 1, yt2 BI-HEFT). Needs further revision.
  cb.cp().process(['ggH_bb_htt','ggH_bb_hww']).AddSyst(cb,'QCDscale_ggHbb','lnN',ch.SystMap()((0.69,1.47)))

  #Need to double check these ones 
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_THU','lnN', ch.SystMap()(1.017))
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_PU_mq','lnN', ch.SystMap()(1.0099))
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_PU_alphas','lnN', ch.SystMap()(1.0062))

  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_THU','lnN', ch.SystMap()(1.0099))
  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_PU_mq','lnN', ch.SystMap()(1.0099))
  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_PU_alphas','lnN', ch.SystMap()(1.0066))

  cb.cp().process(['ZH125','ZH','ZH1','ZHWW125']).AddSyst(cb,'QCDscale_ZH','lnN',ch.SystMap()(1.009))
  cb.cp().process(['ZH125','ZH','ZH1','ZHWW125']).AddSyst(cb,'pdf_Higgs_ZH','lnN',ch.SystMap()(1.013))
  cb.cp().process(['WH125','WH','WH1','WHWW125']).AddSyst(cb,'QCDscale_WH','lnN',ch.SystMap()(1.008))
  cb.cp().process(['WH125','WH','WH1','WHWW125']).AddSyst(cb,'pdf_Higgs_WH','lnN',ch.SystMap()(1.018))
  cb.cp().process(['ttH125','ttH','TTH125','TTHWW125','TTH']).AddSyst(cb,'QCDscale_ttH','lnN',ch.SystMap()(1.08))
  cb.cp().process(['ttH125','ttH','TTH125','TTHWW125','TTH']).AddSyst(cb,'pdf_Higgs_ttH','lnN',ch.SystMap()(1.036))
  cb.cp().process(['VBF','qqH125','qqHWW125']).AddSyst(cb,'QCDscale_qqH','lnN',ch.SystMap()(1.005))
  cb.cp().process(['VBF','qqH125','qqHWW125']).AddSyst(cb,'pdf_Higgs_qqbar','lnN',ch.SystMap()(1.021))
  
  #Tau trigger efficiency 
  tautriggerdmbins = ["0","1","10","11"]
  for taubin in tautriggerdmbins:
     cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))
     cb.cp().process(["EMB"]).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_emb_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))
     cb.cp().process(["EMB"]).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))

  #Tau ID
  cb.cp().process(nojetfakes).channel(['mt','et']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))
  cb.cp().process(httprocs+['EMB','DYJets','ZTT','ZL','ST','TT','TTL','VVL','VV','W','TTVJets']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.06))
  cb.cp().process(['TTL','VVL']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))

  #Electron ID
  cb.cp().process(mc_processes).channel(['et','em']).AddSyst(cb,"CMS_eff_e_"+year,"lnN",ch.SystMap()(1.02))

  #Muon ID
  cb.cp().process(mc_processes).channel(['mt','em']).AddSyst(cb,"CMS_eff_m_"+year,"lnN",ch.SystMap()(1.02))

  #emu Trigger
  cb.cp().process(mc_processes).channel(['em']).AddSyst(cb,"CMS_eff_trigger_em_"+year,"lnN",ch.SystMap()(1.015))
  
  cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year, 'lnN', ch.SystMap()(1.014))
  cb.cp().process(mc_processes).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year,'lnN',ch.SystMap()(1.01))
  
  for taudm in ['1prong','1prong1pi','3prong']:
    cb.cp().process(mc_processes).channel(['et','mt','tt']).AddSyst(cb,'CMS_eff_t_'+taudm+"_"+year,'shape',ch.SystMap()(1.0))
    

  #Bkg normalisations
  cb.cp().channel(['et','mt','tt','em']).process(['VVT','VVJ','VVL','VV']).AddSyst(cb,'CMS_htt_vvXsec','lnN',ch.SystMap()(1.05))
  cb.cp().channel(['et','mt','tt','em']).process(['ST']).AddSyst(cb,'CMS_htt_stXsec','lnN',ch.SystMap()(1.05))
  cb.cp().channel(['et','mt','tt','em']).process(['TTL','TT','TTJ','TTT']).AddSyst(cb,'CMS_htt_tjXsec','lnN',ch.SystMap()(1.06))
  cb.cp().channel(['et','mt','tt','em']).process(['W','WJets']).AddSyst(cb,'CMS_htt_wjXsec','lnN',ch.SystMap()(1.04))
  cb.cp().channel(['et','mt','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'CMS_htt_zjXsec','lnN',ch.SystMap()(1.02))
  cb.cp().channel(['em']).process(['TTVJets']).AddSyst(cb,'CMS_htt_ttvXsec','lnN',ch.SystMap()(1.15))

  #emu QCD  
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_0jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_0jet_shape1_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_0jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_1jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_1jet_shape1_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_1jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_2jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_2jet_shape1_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_2jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_iso_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_nonClosure_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_btag_extrap','lnN',ch.SystMap()(1.05)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_btag_extrap_stat_'+year,'lnN',ch.SystMap()(1.04)) 

  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_em_JetToElecFakes_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_em_JetToMuonFakes_'+year,'shape',ch.SystMap()(1.0)) 

  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_em_BJetToElecFakes_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_em_BJetToMuonFakes_'+year,'shape',ch.SystMap()(1.0)) 

  cb.cp().channel(['em']).process(mc_processes).AddSyst(cb,'CMS_htt_em_JetToElecFakes_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(mc_processes).AddSyst(cb,'CMS_htt_em_JetToMuonFakes_'+year,'shape',ch.SystMap()(1.0)) 

  cb.cp().channel(['em']).process(mc_processes).AddSyst(cb,'CMS_htt_em_BJetToElecFakes_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(mc_processes).AddSyst(cb,'CMS_htt_em_BJetToMuonFakes_'+year,'shape',ch.SystMap()(1.0)) 

  #jetFake stat uncertainties
  jetbins = ['njet0','njet1','njet2']
  dmbins = ['dm0','dm1','dm10','dm11']

  for jbin in jetbins:
    for dm in dmbins:
      cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_stat_'+jbin+'_'+dm+'_'+year,'shape',ch.SystMap()(1.0))
  
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_stat_dR_nbtag1_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_stat_dR_nbtag2_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_syst_met_njet0_closure_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_syst_met_njet1_closure_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_syst_met_njet2_closure_'+year,'shape',ch.SystMap()(1.0))

  cb.cp().channel(['tt']).process(['wFakes']).AddSyst(cb,'CMS_htt_tt_wFakes_syst_'+year,'lnN',ch.SystMap()(1.3))

  cb.cp().channel(['tt']).process(['TT','VV','ZL','ST']).AddSyst(cb,'fake_m_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))

  cb.cp().channel(['tt']).process(['TT','VV','ZL','ST']).AddSyst(cb,'fake_e_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))

  # ttbar and DY shape uncertainties
  cb.cp().channel(['mt','et','tt','em']).process(['TT','TTL','TTJ','TTT']).AddSyst(cb,'ttbarShape','shape',ch.SystMap()(1.0))
  #cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'dyShape','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'dyShape1b','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'dyShape2b','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'dyxsec1b','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'dyxsec2b','shape',ch.SystMap()(1.0))

  # muR and muF uncertainties 
  cb.cp().channel(['mt','et','tt','em']).process(httprocs).AddSyst(cb,'QCDscaleMURSig','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(httprocs).AddSyst(cb,'QCDscaleMUFSig','shape',ch.SystMap()(1.0))

  cb.cp().channel(['em']).process(hwwprocs).AddSyst(cb,'QCDscaleMURSig','shape',ch.SystMap()(1.0))
  cb.cp().channel(['em']).process(hwwprocs).AddSyst(cb,'QCDscaleMUFSig','shape',ch.SystMap()(1.0))

  cb.cp().channel(['mt','et','tt','em']).process(['TT','TTL','TTJ','TTT']).AddSyst(cb,'QCDscaleMURTT','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['TT','TTL','TTJ','TTT']).AddSyst(cb,'QCDscaleMUFTT','shape',ch.SystMap()(1.0))

  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'QCDscaleMURDY','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'QCDscaleMUFDY','shape',ch.SystMap()(1.0))

  # parton shower uncertainties
  cb.cp().channel(['mt','et','tt','em']).process(httprocs).AddSyst(cb,'PS_ISRSig','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(httprocs).AddSyst(cb,'PS_FSRSig','shape',ch.SystMap()(1.0))
  cb.cp().channel(['em']).process(hwwprocs).AddSyst(cb,'PS_ISRSig','shape',ch.SystMap()(1.0))
  cb.cp().channel(['em']).process(hwwprocs).AddSyst(cb,'PS_FSRSig','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['TT','TTL','TTJ','TTT']).AddSyst(cb,'PS_ISRTT','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['TT','TTL','TTJ','TTT']).AddSyst(cb,'PS_FSRTT','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'PS_ISRDY','shape',ch.SystMap()(1.0))
  cb.cp().channel(['mt','et','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'PS_FSRDY','shape',ch.SystMap()(1.0))

  #cb.cp().channel(['mt','et','tt','em']).process(mc_processes).AddSyst(cb,'PS_ISR','shape',ch.SystMap()(1.0))
  #cb.cp().channel(['mt','et','tt','em']).process(mc_processes).AddSyst(cb,'PS_FSR','shape',ch.SystMap()(1.0))

def AddSystematics2018(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()


  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Uncorrelated_2018','lnN', ch.SystMap()(1.015))
  #  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.02))
  #  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.002))
  # correlated with the HIG-19-010 datacards
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Beam_Beam_Deflection','lnN', ch.SystMap()(1.002))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_X_Y_Factorization','lnN', ch.SystMap()(1.02))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Beam_Current_Calibration','lnN', ch.SystMap()(1.002))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Length_Scale','lnN', ch.SystMap()(1.002))

  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'pu_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2018_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesAbsolute', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesAbsolute_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesBBEC1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesBBEC1_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesEC2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesEC2_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesFlavorQCD', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesHF', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesHF_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesRelativeBal', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesRelativeSample_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jer2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'met_unclustered2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_1prong2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_1prong1pi2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_3prong2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt"]).AddSyst(cb, 'eff_trig_mt_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["et"]).AddSyst(cb, 'eff_trig_et_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'fake_m_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'fake_e_2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_qcd', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_w', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_tt', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_qcdfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_qcdfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_ttfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_ttfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2018_frac', 'shape', ch.SystMap()(1.0))
 


def AddSystematics2017(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Uncorrelated_2017','lnN', ch.SystMap()(1.020))
  #  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.009))
  #  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))
  #  correlated with the HIG-19-010 datacards
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Beam_Beam_Deflection','lnN', ch.SystMap()(1.004))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_X_Y_Factorization','lnN', ch.SystMap()(1.008))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Beam_Current_Calibration','lnN', ch.SystMap()(1.003))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Length_Scale','lnN', ch.SystMap()(1.003))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Ghosts_And_Satellites','lnN', ch.SystMap()(1.001))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Dynamic_Beta','lnN', ch.SystMap()(1.005))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'pu_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2017_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesAbsolute', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesAbsolute_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesBBEC1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesBBEC1_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesEC2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesEC2_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesFlavorQCD', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesHF', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesHF_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesRelativeBal', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesRelativeSample_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jer2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'met_unclustered2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_1prong2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_1prong1pi2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_3prong2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt"]).AddSyst(cb, 'eff_trig_mt_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["et"]).AddSyst(cb, 'eff_trig_et_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'fake_m_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'fake_e_2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'prefiring', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'prefiring2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_qcd', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_w', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_tt', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_qcdfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_qcdfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_ttfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_ttfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2017_frac', 'shape', ch.SystMap()(1.0))


def AddSystematics2016(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Uncorrelated_2016','lnN', ch.SystMap()(1.010))
  # cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.006))
  #  correlated with the HIG-19-010 datacards
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Beam_Beam_Deflection','lnN', ch.SystMap()(1.004))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_X_Y_Factorization','lnN', ch.SystMap()(1.009))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Ghosts_And_Satellites','lnN', ch.SystMap()(1.004))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_Dynamic_Beta','lnN', ch.SystMap()(1.005))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'pu_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'btag2016_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_preVFP_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_preVFP_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_preVFP_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_preVFP_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_preVFP_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_postVFP_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_postVFP_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_postVFP_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_postVFP_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_postVFP_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesAbsolute', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesAbsolute_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesBBEC1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesBBEC1_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesEC2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesEC2_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesFlavorQCD', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesHF', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesHF_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesRelativeBal', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jesRelativeSample_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'jer2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'met_unclustered2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_1prong2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_1prong1pi2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt"]).AddSyst(cb, 'scale_t_3prong2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt"]).AddSyst(cb, 'eff_trig_mt_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["et"]).AddSyst(cb, 'eff_trig_et_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'fake_m_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'fake_e_2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'prefiring', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'prefiring2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_qcd', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_w', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_tt', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_qcdfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_qcdfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_ttfitpar0', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_ttfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['QCD']).channel(["mt","et"]).AddSyst(cb, 'ff2016_frac', 'shape', ch.SystMap()(1.0))

def ConvertToLnN(cb,year):

  jetToLepFakes_processes = ['QCD','ZL','TT','ST','W','VV']
  jetToLepFakes_sys = ['CMS_htt_em_BJetToElecFakes_'+year,'CMS_htt_em_BJetToMuonFakes_'+year,'CMS_htt_em_JetToElecFakes_'+year,'CMS_htt_em_JetToMuonFakes_'+year]

  cb.cp().process(mc_processes).channel(['tt','em','mt','et']).syst_name(['jer'+year,'met_unclustered'+year]).ForEachSyst(lambda x:x.set_type('lnN'))
  cb.cp().process(jetToLepFakes_processes).channel(['em']).syst_name(jetToLepFakes_sys).ForEachSyst(lambda x:x.set_type('lnN'))

def renameSys(cb,year):
  cb.cp().RenameSystematic(cb,'met_unclustered'+year,'CMS_scale_met_unclustered_'+year)
  cb.cp().RenameSystematic(cb,'jer'+year,'CMS_res_j_'+year)

  cb.cp().RenameSystematic(cb,'jesAbsolute','CMS_scale_j_absolute')
  cb.cp().RenameSystematic(cb,'jesAbsolute_'+year,'CMS_scale_j_absolute_'+year)
  cb.cp().RenameSystematic(cb,'jesBBEC1','CMS_scale_j_bbec1')
  cb.cp().RenameSystematic(cb,'jesBBEC1_'+year,'CMS_scale_j_bbec1_'+year)
  cb.cp().RenameSystematic(cb,'jesEC2','CMS_scale_j_ec2')
  cb.cp().RenameSystematic(cb,'jesEC2_'+year,'CMS_scale_j_ec2_'+year)
  cb.cp().RenameSystematic(cb,'jesFlavorQCD','CMS_scale_j_flavorqcd')
  cb.cp().RenameSystematic(cb,'jesHF','CMS_scale_j_hf')
  cb.cp().RenameSystematic(cb,'jesHF_'+year,'CMS_scale_j_hf_'+year)
  cb.cp().RenameSystematic(cb,'jesRelativeBal','CMS_scale_j_relativebal')
  cb.cp().RenameSystematic(cb,'jesRelativeSample_'+year,'CMS_scale_j_relativesample_'+year)

  cb.cp().RenameSystematic(cb,'scale_t_1prong'+year,'CMS_scale_t_1prong_'+year)
  cb.cp().RenameSystematic(cb,'scale_t_1prong1pi'+year,'CMS_scale_t_1prong1pizero_'+year)
  cb.cp().RenameSystematic(cb,'scale_t_3prong'+year,'CMS_scale_t_3prong_'+year)

  cb.cp().RenameSystematic(cb,'eff_trig_mt_'+year,'CMS_eff_trigger_mt_'+year)
  cb.cp().RenameSystematic(cb,'eff_trig_et_'+year,'CMS_eff_trigger_et_'+year)

  tautriggerdmbins = ["0","1","10","11"]
  for taubin in tautriggerdmbins:
    cb.cp().RenameSystematic(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'CMS_eff_trigger_tt_dm'+taubin+'_'+year)

  cb.cp().RenameSystematic(cb,'btag'+year+'_jes','CMS_btag_jes_'+year)
  cb.cp().RenameSystematic(cb,'btag'+year+'_lf','CMS_btag_lf')
  cb.cp().RenameSystematic(cb,'btag'+year+'_hf','CMS_btag_hf')
  cb.cp().RenameSystematic(cb,'btag'+year+'_hfstats1','CMS_btag_hfstats1_'+year)
  cb.cp().RenameSystematic(cb,'btag'+year+'_hfstats2','CMS_btag_hfstats2_'+year)
  cb.cp().RenameSystematic(cb,'btag'+year+'_lfstats1','CMS_btag_lfstats1_'+year)
  cb.cp().RenameSystematic(cb,'btag'+year+'_lfstats2','CMS_btag_lfstats2_'+year)
  cb.cp().RenameSystematic(cb,'btag'+year+'_cferr1','CMS_btag_cferr1')
  cb.cp().RenameSystematic(cb,'btag'+year+'_cferr2','CMS_btag_cferr2')
  cb.cp().RenameSystematic(cb,'btag2016_preVFP_jes','CMS_btag_jes_2016_preVFP')
  cb.cp().RenameSystematic(cb,'btag2016_preVFP_hfstats1','CMS_btag_hfstats1_2016_preVFP')
  cb.cp().RenameSystematic(cb,'btag2016_preVFP_hfstats2','CMS_btag_hfstats2_2016_preVFP')
  cb.cp().RenameSystematic(cb,'btag2016_preVFP_lfstats1','CMS_btag_lfstats1_2016_preVFP')
  cb.cp().RenameSystematic(cb,'btag2016_preVFP_lfstats2','CMS_btag_lfstats2_2016_preVFP')
  cb.cp().RenameSystematic(cb,'btag2016_postVFP_jes','CMS_btag_jes_2016_postVFP')
  cb.cp().RenameSystematic(cb,'btag2016_postVFP_hfstats1','CMS_btag_hfstats1_2016_postVFP')
  cb.cp().RenameSystematic(cb,'btag2016_postVFP_hfstats2','CMS_btag_hfstats2_2016_postVFP')
  cb.cp().RenameSystematic(cb,'btag2016_postVFP_lfstats1','CMS_btag_lfstats1_2016_postVFP')
  cb.cp().RenameSystematic(cb,'btag2016_postVFP_lfstats2','CMS_btag_lfstats2_2016_postVFP')

  bbh_procs = ['bbH_htt','bbH_nobb_htt','bbH_hww','bbH_nobb_hww']
  ggh_procs = ['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt','ggH_bb_hww','ggH_hww']
  #wh_procs = ['WH125','WH','WH1','WHWW125','WH_htt','WH_hww']
  wh_procs = ['WH125','WH','WH1','WH_htt']
  zh_procs = ['ZH125','ZH','ZH1','ZHWW125','ZH_htt','ZH_hww']
  qqh_procs = ['VBF','qqH125','qqHWW125','qqH_htt','qqH_hww']
  tth_procs = ['ttH125','ttH','TTH125','TTHWW125','ttH_htt','ttH_hww']

  # bbH
  cb.cp().process(bbh_procs).RenameSystematic(cb,'QCDscaleMURSig','QCDscaleMUR_bbH')
  cb.cp().process(bbh_procs).RenameSystematic(cb,'QCDscaleMUFSig','QCDscaleMUF_bbH')
  cb.cp().process(bbh_procs).RenameSystematic(cb,'PS_ISRSig','PS_ISR_bbH')
  cb.cp().process(bbh_procs).RenameSystematic(cb,'PS_FSRSig','PS_FSR_bbH')

  # ggH
  cb.cp().process(ggh_procs).RenameSystematic(cb,'QCDscaleMURSig','QCDscaleMUR_ggH')
  cb.cp().process(ggh_procs).RenameSystematic(cb,'QCDscaleMUFSig','QCDscaleMUF_ggH')
  cb.cp().process(ggh_procs).RenameSystematic(cb,'PS_ISRSig','PS_ISR_ggH')
  cb.cp().process(ggh_procs).RenameSystematic(cb,'PS_FSRSig','PS_FSR_ggH')

  # qqH
  cb.cp().process(qqh_procs).RenameSystematic(cb,'QCDscaleMURSig','QCDscaleMUR_qqH')
  cb.cp().process(qqh_procs).RenameSystematic(cb,'QCDscaleMUFSig','QCDscaleMUF_qqH')
  cb.cp().process(qqh_procs).RenameSystematic(cb,'PS_ISRSig','PS_ISR_qqH')
  cb.cp().process(qqh_procs).RenameSystematic(cb,'PS_FSRSig','PS_FSR_qqH')

  # ZH
  cb.cp().process(zh_procs).RenameSystematic(cb,'QCDscaleMURSig','QCDscaleMUR_ZH')
  cb.cp().process(zh_procs).RenameSystematic(cb,'QCDscaleMUFSig','QCDscaleMUF_ZH')
  cb.cp().process(zh_procs).RenameSystematic(cb,'PS_ISRSig','PS_ISR_ZH')
  cb.cp().process(zh_procs).RenameSystematic(cb,'PS_FSRSig','PS_FSR_ZH')

  # WH
  cb.cp().process(wh_procs).RenameSystematic(cb,'QCDscaleMURSig','QCDscaleMUR_WH')
  cb.cp().process(wh_procs).RenameSystematic(cb,'QCDscaleMUFSig','QCDscaleMUF_WH')
  cb.cp().process(wh_procs).RenameSystematic(cb,'PS_ISRSig','PS_ISR_WH')
  cb.cp().process(wh_procs).RenameSystematic(cb,'PS_FSRSig','PS_FSR_WH')

  # ttH
  cb.cp().process(tth_procs).RenameSystematic(cb,'QCDscaleMURSig','QCDscaleMUR_ttH')
  cb.cp().process(tth_procs).RenameSystematic(cb,'QCDscaleMUFSig','QCDscaleMUF_ttH')
  cb.cp().process(tth_procs).RenameSystematic(cb,'PS_ISRSig','PS_ISR_ttH')
  cb.cp().process(tth_procs).RenameSystematic(cb,'PS_FSRSig','PS_FSR_ttH')

  # consistency with CMS naming convention
  cb.cp().RenameSystematic(cb,'QCDscaleMURDY','QCDscaleMUR_zj')
  cb.cp().RenameSystematic(cb,'QCDscaleMUFDY','QCDscaleMUF_zj')
  cb.cp().RenameSystematic(cb,'PS_ISRDY','PS_ISR_zj')
  cb.cp().RenameSystematic(cb,'PS_FSRDY','PS_FSR_zj')

  cb.cp().RenameSystematic(cb,'QCDscaleMURTT','QCDscaleMUR_tj')
  cb.cp().RenameSystematic(cb,'QCDscaleMUFTT','QCDscaleMUF_tj')
  cb.cp().RenameSystematic(cb,'PS_ISRTT','PS_ISR_tj')
  cb.cp().RenameSystematic(cb,'PS_FSRTT','PS_FSR_tj')

  # prefiring
  cb.cp().RenameSystematic(cb,'prefiring','CMS_prefiring')
  cb.cp().RenameSystematic(cb,'prefiring2017','CMS_prefiring2017')
  cb.cp().RenameSystematic(cb,'prefiring2016','CMS_prefiring2016')


  # datacard review
  cb.cp().RenameSystematic(cb,'ttbarShape','CMS_htt_ttbarShape')
  cb.cp().RenameSystematic(cb,'dyShape1b','CMS_bbhtt_dyShape1b')
  cb.cp().RenameSystematic(cb,'dyShape2b','CMS_bbhtt_dyShape2b')
  cb.cp().RenameSystematic(cb,'dyxsec1b','CMS_bbhtt_dyxsec1b')
  cb.cp().RenameSystematic(cb,'dyxsec2b','CMS_bbhtt_dyxsec2b')

  cb.cp().RenameSystematic(cb,'fake_m_'+year,'CMS_fake_m_'+year)
  cb.cp().RenameSystematic(cb,'fake_e_'+year,'CMS_fake_e_'+year)

  ffsysts = ["qcd","w","tt","qcdfitpar0","qcdfitpar1","wfitpar0","wfitpar1","wfitpar2","ttfitpar0","ttfitpar1","frac"]
  for ffsyst in ffsysts:
    cb.cp().RenameSystematic(cb,'ff'+year+'_'+ffsyst,'CMS_bbhtt_'+year+'_'+ffsyst)

