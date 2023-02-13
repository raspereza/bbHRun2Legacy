#!/bin/bash
# $1 : ws = channel [tt,em]
# $2 : algo = (saturated, KS, AD)
ws=${1}
algo=${2}
cd GoF/
mv higgsCombine.${ws}_${algo}.obs.GoodnessOfFit.mH125.root gof_${ws}_${algo}.obs.root
rm gof_${ws}_${algo}.exp.root 
hadd gof_${ws}_${algo}.exp.root higgsCombine.${ws}_${algo}_*.exp.GoodnessOfFit.mH125.*.root
rm higgsCombine.${ws}_${algo}_*.exp.GoodnessOfFit.mH125.*.root
cd -
