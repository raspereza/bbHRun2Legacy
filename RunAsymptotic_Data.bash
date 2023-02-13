#!/bin/bash
dir=${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards
ulimit -s unlimited
channel=$1
#combineTool.py -M AsymptoticLimits --noFitAsimov --rMin=0 --rMax=50 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --cminDefaultMinimizerTolerance=0.01 -d ${dir}/${channel}/ws.root -t -1 -n .ws -m 125
#combineTool.py -M AsymptoticLimits --rMin=0 --rMax=40 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --cminDefaultMinimizerTolerance=0.01 -d ${dir}/${ws}.root -t -1 -n .${ws} -m 125
combineTool.py -M AsymptoticLimits --rMin=0 --rMax=40 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --cminDefaultMinimizerTolerance=0.01 -d ${dir}/${channel}/ws.root -n .${ws} -m 125
