#!/bin/bash
channel=$1
ulimit -s unlimited
dir=${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards

combineTool.py -M FitDiagnostics --robustFit 1 --cminDefaultMinimizerTolerance 0.05 --X-rtd MINIMIZER_analytic --expectSignal 1.0 --X-rtd FITTER_NEW_CROSSING_ALGO --cminDefaultMinimizerStrategy=0 -t -1 --rMin=-5 --rMax=5 -m 125 -d ${dir}/${channel}/ws.root -n _${channel}_asimov -v 5
