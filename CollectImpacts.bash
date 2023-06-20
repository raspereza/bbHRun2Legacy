#!/bin/bash
# $1 - channel
ulimit -s unlimited

cd impacts_${1}
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 -o impacts_${1}.json
cd -
