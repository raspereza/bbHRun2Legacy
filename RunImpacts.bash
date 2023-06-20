#!/bin/bash
# $1 - channel

combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 --rMin -10 --rMax 10 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit 
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 --rMin -10 --rMax 10 --robustFit 1 -t -1 --expectSignal 1 --doFits
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 -o impacts_${1}.json
