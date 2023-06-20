#!/bin/bash
dir_tt=/nfs/dust/cms/user/rasp/Run/tautau_datacards_sysJESv1/BDT_coarse
dir_em=/nfs/dust/cms/user/rasp/Run/emu_datacards_sysJESv1/BDT_coarse
for era in 2016 2017 2018
do
    cp ${dir_tt}/bbH_tt_${era}.root shapes/htt_tt_bbH.Run${era}.root
    cp ${dir_em}/bbH_em_${era}.root shapes/htt_em_bbH.Run${era}.root
done
