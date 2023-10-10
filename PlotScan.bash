#!/bin/bash
# $1 - nuisance parameter
ulimit -s unlimited

./scripts/plot1DScan.py --main=higgsCombine_${1}.MultiDimFit.mH125.root --POI=${1} --output=${1} --no-numbers --no-box --x_title="${1}" --x-min=-3.0 --x-max=3.0 --y-max=4.0 --main-label="obs" 

