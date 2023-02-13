#!/bin/bash
for era in 2016 2017 2018
do
    mkdir -p ${1}/${era}/cmb/
    mkdir -p ${1}/${era}/cmb/common
    cp ${1}/${era}/htt_*/*.txt  ${1}/${era}/cmb/
    cp ${1}/${era}/htt_*/common/*.root ${1}/${era}/cmb/common
done
mkdir -p ${1}/combined/cmb/
mkdir -p ${1}/combined/cmb/common 
for era in 2016 2017 2018
do
    cp ${1}/${era}/htt_*/*.txt  ${1}/combined/cmb/
    cp ${1}/${era}/htt_*/common/*.root ${1}/combined/cmb/common
done
