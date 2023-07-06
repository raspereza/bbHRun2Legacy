import CombineHarvester.CombineTools.ch as ch

def AddCommonSystematics(cb, year):
  backgrounds = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  bbhsignals = ['bbH_htt','bbH_nobb_htt','bbH_hww','bbH_nobb_hww']
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH_hww','bbH_nobb_hww','ggH_bb_hww','ggH_hww','ZL','TTL','VVL','qqH125','WH125','ZH125','TTH125','qqHWW125','WH','TTHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT','TTVJets','ttH125','ttH']
  nojetfakes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH_hww','bbH_nobb_hww','ggH_bb_hww','ggH_hww','ZL','TTL','VVL','qqH125','WH125','ZH125','TTH125','qqHWW125','WHWW125','ZHWW125','TTHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','EMB','W','ZTT','TTVJets','ttH125','ttH']
  httprocs = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','ZH','VBF','qqH125','WH125','ZH125','ttH125','TTH125','ttH']
  hwwprocs = ['bbH_hww','bbH_nobb_hww','ggH_bb_hww','ggH_hww','TTHWW125']
  h125ttprocs = ['ggH_htt','ZH','VBF','qqH125','WH125','ZH125','ttH125','TTH125','ttH']
  h125wwprocs = ['ggH_hww','qqHWW125','TTHWW125']
  hwwprocs_sig = ['bbH_hww','ggH_bb_hww']
  httprocs_sig = ['bbH_htt','ggH_bb_htt']

  #Signal theory uncertainties
  cb.cp().process(bbhsignals).AddSyst(cb,'QCDscale_bbH','lnN', ch.SystMap()((0.76,1.201)))
  cb.cp().process(['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt']).AddSyst(cb,'QCDscale_ggH','lnN', ch.SystMap()((0.93,1.046)))
  cb.cp().process(['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt']).AddSyst(cb,'pdf_Higgs_ggH','lnN', ch.SystMap()(1.032))
  #Additional uncertainty for ggH+2b 
  cb.cp().process(['ggH_bb_htt']).AddSyst(cb,'QCDscale_ggHbb','lnN',ch.SystMap()(1.40))

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
  cb.cp().process(['ttH125','ttH','TTH125','TTHWW125']).AddSyst(cb,'QCDscale_ttH','lnN',ch.SystMap()(1.08))
  cb.cp().process(['ttH125','ttH','TTH125','TTHWW125']).AddSyst(cb,'pdf_Higgs_ttH','lnN',ch.SystMap()(1.036))
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
  cb.cp().process(['bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ggH125','qqH125','WH125','ZH125','EMB','ZTT','TTT','VVT','TT','VV','ST']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.06))
  cb.cp().process(['TTL','VVL']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))

  #Electron ID
  cb.cp().process(mc_processes).channel(['et','em']).AddSyst(cb,"CMS_eff_e","lnN",ch.SystMap()(1.02))

  #Muon ID
  cb.cp().process(mc_processes).channel(['mt','em']).AddSyst(cb,"CMS_eff_m","lnN",ch.SystMap()(1.02))

  #emu Trigger
  cb.cp().process(mc_processes).channel(['em']).AddSyst(cb,"CMS_eff_em_trig_"+year,"lnN",ch.SystMap()(1.015))
  
  cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year, 'lnN', ch.SystMap()(1.014))
  cb.cp().process(mc_processes).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year,'lnN',ch.SystMap()(1.01))
  
  for taudm in ['1prong','1prong1pi','3prong']:
    cb.cp().process(mc_processes).channel(['et','mt','tt']).AddSyst(cb,'CMS_eff_t_'+taudm+"_"+year,'shape',ch.SystMap()(1.0))
    

  #Bkg normalisations
  cb.cp().channel(['et','mt','tt','em']).process(['VVT','VVJ','VVL','VV','ST']).AddSyst(cb,'CMS_htt_vvXsec','lnN',ch.SystMap()(1.05))
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
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT','TTH125','ttH125','ttH','TTHWW125','TTVJets']
  bkg_processes = ['TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT','TTH125','ttH125','ttH','TTHWW125','TTVJets']
  sig_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125']

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2018','lnN', ch.SystMap()(1.015))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.02))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.002))
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
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT','TTH125','ttH125','ttH','TTHWW125','TTVJets']

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2017','lnN', ch.SystMap()(1.020))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.009))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))
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
  #cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'prefiring', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'prefiring', 'shape', ch.SystMap()(1.0))
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
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT','TTH125','TTHWW125','TTVJets','ttH125','ttH']

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2016','lnN', ch.SystMap()(1.010))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.006))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'btag2016_cferr2', 'shape', ch.SystMap()(1.0))
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
  #cb.cp().process(mc_processes).channel(["mt","et","tt","em"]).AddSyst(cb, 'prefiring', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'prefiring', 'shape', ch.SystMap()(1.0))
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
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT','TTH125','ttH125','ttH','TTHWW125','TTVJets']

  jetToLepFakes_processes = ['QCD','ZL','TT','ST','W','VV']
  jetToLepFakes_sys = ['CMS_htt_em_BJetToElecFakes_'+year,'CMS_htt_em_BJetToMuonFakes_'+year,'CMS_htt_em_JetToElecFakes_'+year,'CMS_htt_em_JetToMuonFakes_'+year]

  cb.cp().process(mc_processes).channel(['tt','em','mt','et']).syst_name(['jer'+year,'met_unclustered'+year]).ForEachSyst(lambda x:x.set_type('lnN'))
  cb.cp().process(jetToLepFakes_processes).channel(['em']).syst_name(jetToLepFakes_sys).ForEachSyst(lambda x:x.set_type('lnN'))
