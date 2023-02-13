#!/bin/bash
# $1 - model

for year in 2016 2017 2018 
do
    for cat in 1 2 3 4 5 6 7 8
    do
	./prefit.bash ${1} htt_tt_${cat}_${year}
    done
done
