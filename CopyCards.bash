#!/bin/bash
dir_tt=/nfs/dust/cms/user/rasp/Run/tautau_datacards_sys_UL/BDT_coarse
dir_em=/nfs/dust/cms/user/rasp/Run/emu_datacards_sys_UL/BDT_fine
for era in 2016 2017 2018
do
    cp ${dir_tt}/bbH_tt_${era}.root shapes/htt_tt_bbH_comb.Run${era}.root
    cp ${dir_em}/bbH_em_${era}.root shapes/htt_em_bbH_comb.Run${era}.root
done
