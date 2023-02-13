#!/bin/bash
# $1 = channel
ulimit -s unlimited
combineTool.py -M T2W -o "ws.root" -i output/cards/${1} -m 125
for year in 2016 2017 2018
do
    combineTool.py -M T2W -o "ws.root" -i output/cards/${1}${year} -m 125
done
