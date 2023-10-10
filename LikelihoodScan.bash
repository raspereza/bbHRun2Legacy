#!/bin/bash
ulimit -s unlimited
# $1 - workspace (cmb, et, mt, tt, em)

# insert in the list nuisance parameters you would like to scan
#for par in prop_binbbhtt_tt_1_13TeV2018_bin6 prop_binbbhtt_tt_1_13TeV2016_bin6 CMS_scale_t_3prong_2016 prop_binbbhtt_et_1_13TeV2018_bin5 CMS_scale_t_3prong_2016 CMS_scale_t_1prong_2016
for par in prop_binbbhtt_mt_1_13TeV2017_bin0
do

    combineTool.py -m 125 -M MultiDimFit -P ${par} --setParameterRanges ${par}=-4,4:r=-10,10 --floatOtherPOIs 1 --points 41 --robustFit 1 -d output/cards/${1}/ws.root --algo grid --alignEdges 1 --cminDefaultMinimizerStrategy=0 -n _${par}

done
