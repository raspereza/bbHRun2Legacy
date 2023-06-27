#!/bin/bash
# $1 - channel
ulimit -s unlimited

OUTDIR=impacts_${1}
if [ ! -d "$OUTDIR" ]; then
    mkdir $OUTDIR
fi
cd $OUTDIR
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 --rMin -10 --rMax 20 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit 
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 --rMin -10 --rMax 20 --robustFit 1 -t -1 --expectSignal 1 --job-mode condor --sub-opts='+JobFlavour = "workday"' --merge 3 --doFits
cd -

