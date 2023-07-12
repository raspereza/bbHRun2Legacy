#!/bin/bash
# $1 - channel
ulimit -s unlimited

OUTDIR=2Dscan
if [ ! -d "$OUTDIR" ]; then
    mkdir $OUTDIR
fi
cd $OUTDIR
combineTool.py -M MultiDimFit -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/kappa/ws_kappas.root --redefineSignalPOIs kappa_b,kappa_t --setParameters kappa_b=1,kappa_t=1 -m 125.38 --algo grid --points 1600 -t -1 --job-mode condor --sub-opts='+JobFlavour = "workday"' --merge 20 
cd -

