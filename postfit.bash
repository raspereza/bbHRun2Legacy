#!/bin/bash
dir=/nfs/dust/cms/user/rasp/Run/MSSM_HTT
model=$1
cat=$2
ulimit -s unlimited

PostFitShapesFromWorkspace -d ${model}/restore_binning/${cat}.txt -w ${model}/combined/cmb/bbH_combined.root -m 125 --cat ${cat} -f fitDiagnostics_${model}_bbH_combined.root:fit_b --postfit -o ${model}_${cat}_bonly.root


