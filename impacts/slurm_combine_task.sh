#!/bin/sh
ulimit -s unlimited
set -e
cd /work/pbaertsc/bbh/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /work/pbaertsc/bbh/CMSSW_10_2_13/src/CombineHarvester/bbHRun2Legacy/impacts
if [ ${SLURM_ARRAY_TASK_ID} -eq 1 ]; then
  combine -M MultiDimFit -n _paramFit_Test_BR_htt_PU_alphas --algo impact --redefineSignalPOIs r -P BR_htt_PU_alphas --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 2 ]; then
  combine -M MultiDimFit -n _paramFit_Test_BR_htt_PU_mq --algo impact --redefineSignalPOIs r -P BR_htt_PU_mq --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 3 ]; then
  combine -M MultiDimFit -n _paramFit_Test_BR_htt_THU --algo impact --redefineSignalPOIs r -P BR_htt_THU --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 4 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_e --algo impact --redefineSignalPOIs r -P CMS_eff_e --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 5 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_1prong1pi_2016 --algo impact --redefineSignalPOIs r -P CMS_eff_t_1prong1pi_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 6 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_1prong1pi_2017 --algo impact --redefineSignalPOIs r -P CMS_eff_t_1prong1pi_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 7 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_1prong1pi_2018 --algo impact --redefineSignalPOIs r -P CMS_eff_t_1prong1pi_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 8 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_1prong_2016 --algo impact --redefineSignalPOIs r -P CMS_eff_t_1prong_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 9 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_1prong_2017 --algo impact --redefineSignalPOIs r -P CMS_eff_t_1prong_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 10 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_1prong_2018 --algo impact --redefineSignalPOIs r -P CMS_eff_t_1prong_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 11 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_3prong_2016 --algo impact --redefineSignalPOIs r -P CMS_eff_t_3prong_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 12 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_3prong_2017 --algo impact --redefineSignalPOIs r -P CMS_eff_t_3prong_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 13 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_3prong_2018 --algo impact --redefineSignalPOIs r -P CMS_eff_t_3prong_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 14 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_et_2016 --algo impact --redefineSignalPOIs r -P CMS_eff_t_et_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 15 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_et_2017 --algo impact --redefineSignalPOIs r -P CMS_eff_t_et_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 16 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_et_2018 --algo impact --redefineSignalPOIs r -P CMS_eff_t_et_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 17 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_wp_2016 --algo impact --redefineSignalPOIs r -P CMS_eff_t_wp_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 18 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_wp_2017 --algo impact --redefineSignalPOIs r -P CMS_eff_t_wp_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 19 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_t_wp_2018 --algo impact --redefineSignalPOIs r -P CMS_eff_t_wp_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 20 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_htt_tjXsec --algo impact --redefineSignalPOIs r -P CMS_htt_tjXsec --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 21 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_htt_vvXsec --algo impact --redefineSignalPOIs r -P CMS_htt_vvXsec --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 22 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_htt_zjXsec --algo impact --redefineSignalPOIs r -P CMS_htt_zjXsec --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 23 ]; then
  combine -M MultiDimFit -n _paramFit_Test_PS_FSR --algo impact --redefineSignalPOIs r -P PS_FSR --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 24 ]; then
  combine -M MultiDimFit -n _paramFit_Test_PS_ISR --algo impact --redefineSignalPOIs r -P PS_ISR --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 25 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscaleMUFDY --algo impact --redefineSignalPOIs r -P QCDscaleMUFDY --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 26 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscaleMUFSig --algo impact --redefineSignalPOIs r -P QCDscaleMUFSig --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 27 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscaleMUFTT --algo impact --redefineSignalPOIs r -P QCDscaleMUFTT --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 28 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscaleMURDY --algo impact --redefineSignalPOIs r -P QCDscaleMURDY --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 29 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscaleMURSig --algo impact --redefineSignalPOIs r -P QCDscaleMURSig --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 30 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscaleMURTT --algo impact --redefineSignalPOIs r -P QCDscaleMURTT --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 31 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_VH --algo impact --redefineSignalPOIs r -P QCDscale_VH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 32 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_bbH --algo impact --redefineSignalPOIs r -P QCDscale_bbH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 33 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_ggH --algo impact --redefineSignalPOIs r -P QCDscale_ggH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 34 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_ggHbb --algo impact --redefineSignalPOIs r -P QCDscale_ggHbb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 35 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_qqH --algo impact --redefineSignalPOIs r -P QCDscale_qqH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 36 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_ttH --algo impact --redefineSignalPOIs r -P QCDscale_ttH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 37 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_cferr1 --algo impact --redefineSignalPOIs r -P btag2016_cferr1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 38 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_cferr2 --algo impact --redefineSignalPOIs r -P btag2016_cferr2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 39 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_hf --algo impact --redefineSignalPOIs r -P btag2016_hf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 40 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_hfstats1 --algo impact --redefineSignalPOIs r -P btag2016_hfstats1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 41 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_hfstats2 --algo impact --redefineSignalPOIs r -P btag2016_hfstats2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 42 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_jes --algo impact --redefineSignalPOIs r -P btag2016_jes --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 43 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_lf --algo impact --redefineSignalPOIs r -P btag2016_lf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 44 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_lfstats1 --algo impact --redefineSignalPOIs r -P btag2016_lfstats1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 45 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2016_lfstats2 --algo impact --redefineSignalPOIs r -P btag2016_lfstats2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 46 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_cferr1 --algo impact --redefineSignalPOIs r -P btag2017_cferr1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 47 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_cferr2 --algo impact --redefineSignalPOIs r -P btag2017_cferr2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 48 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_hf --algo impact --redefineSignalPOIs r -P btag2017_hf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 49 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_hfstats1 --algo impact --redefineSignalPOIs r -P btag2017_hfstats1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 50 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_hfstats2 --algo impact --redefineSignalPOIs r -P btag2017_hfstats2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 51 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_jes --algo impact --redefineSignalPOIs r -P btag2017_jes --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 52 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_lf --algo impact --redefineSignalPOIs r -P btag2017_lf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 53 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_lfstats1 --algo impact --redefineSignalPOIs r -P btag2017_lfstats1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 54 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2017_lfstats2 --algo impact --redefineSignalPOIs r -P btag2017_lfstats2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 55 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_cferr1 --algo impact --redefineSignalPOIs r -P btag2018_cferr1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 56 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_cferr2 --algo impact --redefineSignalPOIs r -P btag2018_cferr2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 57 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_hf --algo impact --redefineSignalPOIs r -P btag2018_hf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 58 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_hfstats1 --algo impact --redefineSignalPOIs r -P btag2018_hfstats1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 59 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_hfstats2 --algo impact --redefineSignalPOIs r -P btag2018_hfstats2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 60 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_jes --algo impact --redefineSignalPOIs r -P btag2018_jes --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 61 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_lf --algo impact --redefineSignalPOIs r -P btag2018_lf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 62 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_lfstats1 --algo impact --redefineSignalPOIs r -P btag2018_lfstats1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 63 ]; then
  combine -M MultiDimFit -n _paramFit_Test_btag2018_lfstats2 --algo impact --redefineSignalPOIs r -P btag2018_lfstats2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 64 ]; then
  combine -M MultiDimFit -n _paramFit_Test_dyShape1b --algo impact --redefineSignalPOIs r -P dyShape1b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 65 ]; then
  combine -M MultiDimFit -n _paramFit_Test_dyShape2b --algo impact --redefineSignalPOIs r -P dyShape2b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 66 ]; then
  combine -M MultiDimFit -n _paramFit_Test_dyxsec1b --algo impact --redefineSignalPOIs r -P dyxsec1b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 67 ]; then
  combine -M MultiDimFit -n _paramFit_Test_dyxsec2b --algo impact --redefineSignalPOIs r -P dyxsec2b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 68 ]; then
  combine -M MultiDimFit -n _paramFit_Test_eff_trig_et_2016 --algo impact --redefineSignalPOIs r -P eff_trig_et_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 69 ]; then
  combine -M MultiDimFit -n _paramFit_Test_eff_trig_et_2017 --algo impact --redefineSignalPOIs r -P eff_trig_et_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 70 ]; then
  combine -M MultiDimFit -n _paramFit_Test_eff_trig_et_2018 --algo impact --redefineSignalPOIs r -P eff_trig_et_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 71 ]; then
  combine -M MultiDimFit -n _paramFit_Test_fake_e_2016 --algo impact --redefineSignalPOIs r -P fake_e_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 72 ]; then
  combine -M MultiDimFit -n _paramFit_Test_fake_e_2017 --algo impact --redefineSignalPOIs r -P fake_e_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 73 ]; then
  combine -M MultiDimFit -n _paramFit_Test_fake_e_2018 --algo impact --redefineSignalPOIs r -P fake_e_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 74 ]; then
  combine -M MultiDimFit -n _paramFit_Test_fake_m_2016 --algo impact --redefineSignalPOIs r -P fake_m_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 75 ]; then
  combine -M MultiDimFit -n _paramFit_Test_fake_m_2017 --algo impact --redefineSignalPOIs r -P fake_m_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 76 ]; then
  combine -M MultiDimFit -n _paramFit_Test_fake_m_2018 --algo impact --redefineSignalPOIs r -P fake_m_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 77 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_frac --algo impact --redefineSignalPOIs r -P ff2016_frac --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 78 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_qcd --algo impact --redefineSignalPOIs r -P ff2016_qcd --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 79 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_qcdfitpar0 --algo impact --redefineSignalPOIs r -P ff2016_qcdfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 80 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_qcdfitpar1 --algo impact --redefineSignalPOIs r -P ff2016_qcdfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 81 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_tt --algo impact --redefineSignalPOIs r -P ff2016_tt --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 82 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_ttfitpar0 --algo impact --redefineSignalPOIs r -P ff2016_ttfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 83 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_ttfitpar1 --algo impact --redefineSignalPOIs r -P ff2016_ttfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 84 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_w --algo impact --redefineSignalPOIs r -P ff2016_w --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 85 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_wfitpar0 --algo impact --redefineSignalPOIs r -P ff2016_wfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 86 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_wfitpar1 --algo impact --redefineSignalPOIs r -P ff2016_wfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 87 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2016_wfitpar2 --algo impact --redefineSignalPOIs r -P ff2016_wfitpar2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 88 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_frac --algo impact --redefineSignalPOIs r -P ff2017_frac --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 89 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_qcd --algo impact --redefineSignalPOIs r -P ff2017_qcd --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 90 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_qcdfitpar0 --algo impact --redefineSignalPOIs r -P ff2017_qcdfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 91 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_qcdfitpar1 --algo impact --redefineSignalPOIs r -P ff2017_qcdfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 92 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_tt --algo impact --redefineSignalPOIs r -P ff2017_tt --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 93 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_ttfitpar0 --algo impact --redefineSignalPOIs r -P ff2017_ttfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 94 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_ttfitpar1 --algo impact --redefineSignalPOIs r -P ff2017_ttfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 95 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_w --algo impact --redefineSignalPOIs r -P ff2017_w --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 96 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_wfitpar0 --algo impact --redefineSignalPOIs r -P ff2017_wfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 97 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_wfitpar1 --algo impact --redefineSignalPOIs r -P ff2017_wfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 98 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2017_wfitpar2 --algo impact --redefineSignalPOIs r -P ff2017_wfitpar2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 99 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_frac --algo impact --redefineSignalPOIs r -P ff2018_frac --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 100 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_qcd --algo impact --redefineSignalPOIs r -P ff2018_qcd --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 101 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_qcdfitpar0 --algo impact --redefineSignalPOIs r -P ff2018_qcdfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 102 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_qcdfitpar1 --algo impact --redefineSignalPOIs r -P ff2018_qcdfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 103 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_tt --algo impact --redefineSignalPOIs r -P ff2018_tt --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 104 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_ttfitpar0 --algo impact --redefineSignalPOIs r -P ff2018_ttfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 105 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_ttfitpar1 --algo impact --redefineSignalPOIs r -P ff2018_ttfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 106 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_w --algo impact --redefineSignalPOIs r -P ff2018_w --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 107 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_wfitpar0 --algo impact --redefineSignalPOIs r -P ff2018_wfitpar0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 108 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_wfitpar1 --algo impact --redefineSignalPOIs r -P ff2018_wfitpar1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 109 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ff2018_wfitpar2 --algo impact --redefineSignalPOIs r -P ff2018_wfitpar2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 110 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jer2016 --algo impact --redefineSignalPOIs r -P jer2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 111 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jer2017 --algo impact --redefineSignalPOIs r -P jer2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 112 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jer2018 --algo impact --redefineSignalPOIs r -P jer2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 113 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesAbsolute --algo impact --redefineSignalPOIs r -P jesAbsolute --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 114 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesAbsolute_2016 --algo impact --redefineSignalPOIs r -P jesAbsolute_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 115 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesAbsolute_2017 --algo impact --redefineSignalPOIs r -P jesAbsolute_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 116 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesAbsolute_2018 --algo impact --redefineSignalPOIs r -P jesAbsolute_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 117 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesBBEC1 --algo impact --redefineSignalPOIs r -P jesBBEC1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 118 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesBBEC1_2016 --algo impact --redefineSignalPOIs r -P jesBBEC1_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 119 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesBBEC1_2017 --algo impact --redefineSignalPOIs r -P jesBBEC1_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 120 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesBBEC1_2018 --algo impact --redefineSignalPOIs r -P jesBBEC1_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 121 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesEC2 --algo impact --redefineSignalPOIs r -P jesEC2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 122 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesEC2_2016 --algo impact --redefineSignalPOIs r -P jesEC2_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 123 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesEC2_2017 --algo impact --redefineSignalPOIs r -P jesEC2_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 124 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesEC2_2018 --algo impact --redefineSignalPOIs r -P jesEC2_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 125 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesFlavorQCD --algo impact --redefineSignalPOIs r -P jesFlavorQCD --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 126 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesHF --algo impact --redefineSignalPOIs r -P jesHF --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 127 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesHF_2016 --algo impact --redefineSignalPOIs r -P jesHF_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 128 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesHF_2017 --algo impact --redefineSignalPOIs r -P jesHF_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 129 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesHF_2018 --algo impact --redefineSignalPOIs r -P jesHF_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 130 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesRelativeBal --algo impact --redefineSignalPOIs r -P jesRelativeBal --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 131 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesRelativeSample_2016 --algo impact --redefineSignalPOIs r -P jesRelativeSample_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 132 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesRelativeSample_2017 --algo impact --redefineSignalPOIs r -P jesRelativeSample_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 133 ]; then
  combine -M MultiDimFit -n _paramFit_Test_jesRelativeSample_2018 --algo impact --redefineSignalPOIs r -P jesRelativeSample_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 134 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV --algo impact --redefineSignalPOIs r -P lumi_13TeV --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 135 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_1718 --algo impact --redefineSignalPOIs r -P lumi_13TeV_1718 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 136 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_2016 --algo impact --redefineSignalPOIs r -P lumi_13TeV_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 137 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_2017 --algo impact --redefineSignalPOIs r -P lumi_13TeV_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 138 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_2018 --algo impact --redefineSignalPOIs r -P lumi_13TeV_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 139 ]; then
  combine -M MultiDimFit -n _paramFit_Test_met_unclustered2016 --algo impact --redefineSignalPOIs r -P met_unclustered2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 140 ]; then
  combine -M MultiDimFit -n _paramFit_Test_met_unclustered2017 --algo impact --redefineSignalPOIs r -P met_unclustered2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 141 ]; then
  combine -M MultiDimFit -n _paramFit_Test_met_unclustered2018 --algo impact --redefineSignalPOIs r -P met_unclustered2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 142 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_VH --algo impact --redefineSignalPOIs r -P pdf_Higgs_VH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 143 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_ggH --algo impact --redefineSignalPOIs r -P pdf_Higgs_ggH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 144 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_qqbar --algo impact --redefineSignalPOIs r -P pdf_Higgs_qqbar --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 145 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_ttH --algo impact --redefineSignalPOIs r -P pdf_Higgs_ttH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 146 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin10 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 147 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin11 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 148 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin12 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 149 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin13 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 150 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin14 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 151 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin15 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 152 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin16 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 153 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin17 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 154 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin18 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 155 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin19 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 156 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 157 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin20 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin20 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 158 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin21 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin21 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 159 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin22 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin22 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 160 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin23 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin23 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 161 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin24 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin24 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 162 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin25 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin25 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 163 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin26 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin26 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 164 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin27 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin27 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 165 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 166 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin4 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 167 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin5 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 168 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin6 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 169 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin7 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 170 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin8 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 171 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2016_bin9 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2016_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 172 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin10 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 173 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin11 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 174 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin12 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 175 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin13 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 176 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin14 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 177 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin15 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 178 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin16 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 179 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin17 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 180 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin18 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 181 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin19 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 182 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 183 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin20 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin20 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 184 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin21 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin21 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 185 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin22 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin22 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 186 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin23 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin23 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 187 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin24 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin24 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 188 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin25 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin25 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 189 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin26 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin26 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 190 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin27 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin27 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 191 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 192 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin4 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 193 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin5 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 194 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin6 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 195 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin7 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 196 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin8 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 197 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2017_bin9 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2017_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 198 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin10 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 199 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin11 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 200 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin12 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 201 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin13 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 202 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin14 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 203 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin15 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 204 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin16 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 205 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin17 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 206 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin18 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 207 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin19 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 208 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 209 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin20 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin20 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 210 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin21 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin21 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 211 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin22 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin22 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 212 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin23 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin23 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 213 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin24 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin24 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 214 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin25 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin25 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 215 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin26 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin26 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 216 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin27 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin27 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 217 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 218 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin4 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 219 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin5 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 220 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin6 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 221 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin7 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 222 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin8 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 223 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_1_13TeV2018_bin9 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_1_13TeV2018_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 224 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2016_bin1 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2016_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 225 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2016_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2016_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 226 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2016_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2016_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 227 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2017_bin1 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2017_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 228 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2017_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2017_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 229 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2017_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2017_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 230 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2018_bin1 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2018_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 231 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2018_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2018_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 232 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_2_13TeV2018_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_2_13TeV2018_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 233 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2016_bin1 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2016_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 234 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2016_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2016_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 235 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2016_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2016_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 236 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2017_bin1 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2017_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 237 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2017_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2017_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 238 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2017_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2017_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 239 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2018_bin1 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2018_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 240 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2018_bin2 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2018_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 241 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binbbhtt_et_3_13TeV2018_bin3 --algo impact --redefineSignalPOIs r -P prop_binbbhtt_et_3_13TeV2018_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 242 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_1prong1pi2016 --algo impact --redefineSignalPOIs r -P scale_t_1prong1pi2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 243 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_1prong1pi2017 --algo impact --redefineSignalPOIs r -P scale_t_1prong1pi2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 244 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_1prong1pi2018 --algo impact --redefineSignalPOIs r -P scale_t_1prong1pi2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 245 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_1prong2016 --algo impact --redefineSignalPOIs r -P scale_t_1prong2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 246 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_1prong2017 --algo impact --redefineSignalPOIs r -P scale_t_1prong2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 247 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_1prong2018 --algo impact --redefineSignalPOIs r -P scale_t_1prong2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 248 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_3prong2016 --algo impact --redefineSignalPOIs r -P scale_t_3prong2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 249 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_3prong2017 --algo impact --redefineSignalPOIs r -P scale_t_3prong2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 250 ]; then
  combine -M MultiDimFit -n _paramFit_Test_scale_t_3prong2018 --algo impact --redefineSignalPOIs r -P scale_t_3prong2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
if [ ${SLURM_ARRAY_TASK_ID} -eq 251 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ttbarShape --algo impact --redefineSignalPOIs r -P ttbarShape --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 -t -1 --expectSignal 1 --rMin=-20 --rMax=20 -m 125.38 -d ../output/cards/et/ws.root
fi
