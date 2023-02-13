#!/bin/bash
model=$1
cat=$2
ulimit -s unlimited

PostFitShapesFromWorkspace -d ${model}/restore_binning/${cat}.txt -w ${model}/combined/cmb/bbH_combined.root -m 125 --cat ${cat} -o ${model}_${cat}.root
