#!/bin/bash
channel=$1
ulimit -s unlimited
dir=${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards

#combineTool.py -M FitDiagnostics --robustHesse 1 --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL --cminDefaultMinimizerTolerance 0.05 --X-rtd MINIMIZER_analytic --X-rtd FITTER_NEW_CROSSING_ALGO --cminDefaultMinimizerStrategy=0 --rMin=-10 --rMax=30 -m 125 -d ${dir}/${channel}/ws.root -n _${channel}_data -v 5

combineTool.py -M FitDiagnostics --robustHesse 1 --cminDefaultMinimizerTolerance 0.05 --X-rtd MINIMIZER_analytic --X-rtd FITTER_NEW_CROSSING_ALGO --cminDefaultMinimizerStrategy=0 --rMin=-10 --rMax=30 -m 125 -d ${dir}/${channel}/ws.root -n _${channel}_data -v 5
