#!/bin/bash
channel=$1
cd impacts_${1}
plotImpacts.py -i impacts_${1}.json -o impacts_${1}
cd -
