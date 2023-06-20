#!/bin/bash
# $1 - channel
combine -M Significance --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --X-rtd ADDNLL_RECURSIVE=0 --X-rtd FITTER_NEW_CROSSING_ALGO --expectSignal=1 output/cards/${1}/ws.root 
#combineTool.py -M Significance --cminDefaultMinimizerTolerance 0.01 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --X-rtd FITTER_NEW_CROSSING_ALGO --rMin=-3 --rMax=3 -m 125 ${1}.txt
