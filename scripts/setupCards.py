#!/usr/bin/env python

import CombineHarvester.CombineTools.ch as ch
import CombineHarvester.bbHRun2Legacy.systematics as systs
import ROOT as R
import glob
import numpy as np
import os
import sys
import argparse

def drop_em_tt_qcd(chob,proc):
  drop_process =  proc.process()=='QCD' and proc.channel()=='em' and proc.bin_id()==1
  if(drop_process):
    chob.FilterSysts(lambda sys: matching_proc(proc,sys)) 
  return drop_process

parser = argparse.ArgumentParser()
parser.add_argument(
 '--channel', default='tt', help="""Which channels to run? Supported options: 'all', 'mt', 'et', 'tt', 'em'""")
parser.add_argument(
 '--output_folder', default='cards', help="""Subdirectory of ./output/ where the cards are written out to""")
parser.add_argument(
 '--year', default='2018', help="""Year to produce datacards for (2016, 2017, or 2018)""")
parser.add_argument(
 '--extra_folder', default='', help="""Additional folder for input shapes""")

args = parser.parse_args()

cb = ch.CombineHarvester()
cb.SetFlag("check-negative-bins-on-import",0)

shapes = os.environ['CMSSW_BASE'] + '/src/CombineHarvester/bbHRun2Legacy/shapes/'

chns = []
if args.channel=="all":
  chns = ['mt','et','tt','em']

if 'mt' in args.channel:
  chns.append('mt')

if 'et' in args.channel:
  chns.append('et')

if 'tt' in args.channel:
  chns.append('tt')

if 'em' in args.channel:
  chns.append('em')



year = args.year
if year is not "2016" and not "2017" and not "2018":
  print "Year ", year, " not supported! Choose from: '2016', '2017', '2018'"
  sys.exit()

bkg_procs = {
  'mt' : ['QCD','TT','ST','DYJets','VV'], #bbH_nobb_htt,ggH_htt, intH_htt labeled as signal for kappa model, for asymptotic limit they are not scaled with r
  'et' : ['QCD','TT','ST','DYJets','VV'],
  'tt' : ['ZTT','ZL','TT','VV','ST','jetFakes', 'wFakes'],
  'em' : ['ZTT','ZL','TT','VV','ST','QCD','W','TTVJets']
}

sig_procs = {
   'mt' : ['bbH_htt','ggH_bb_htt','intH_bb_htt','ggH_htt','intH_htt','VBF','ZH','WH','ttH'],#bbH_nobb_htt removed because of negative contribution
   'et' : ['bbH_htt','ggH_bb_htt','intH_bb_htt','ggH_htt','intH_htt','VBF','ZH','WH','ttH'],#bbH_nobb_htt removed because of negative contribution
   'tt' : ['bbH_htt','ggH_bb_htt','intH_bb_htt','ggH_htt','intH_htt','qqH125','WH125','ZH125','TTH125'],
   'em' : ['bbH_htt','ggH_bb_htt','intH_bb_htt','ggH_htt','intH_htt','bbH_hww','ggH_bb_hww','intH_bb_hww','ggH_hww','intH_hww','qqH125','WH125','ZH125','TTH125','qqHWW125','WHWW125','ZHWW125','TTHWW125']
}


categories = {
  'mt' : [
    #(1, 'inclusive'),
    (1, 'BDToutSig'),
    (2, 'BDToutTT'),
    (3, 'BDToutDY')
  ],
  'et' : [
    #(1, 'inclusive'),
    (1, 'BDToutSig'),
    (2, 'BDToutTT'),
    (3, 'BDToutDY')
  ],
  'tt' : [
    (1, "tt_cat0_NbtagGe1"), # Signal
    (2, "tt_cat2_NbtagGe1"), # Fakes 
    (3, "tt_cat3_NbtagGe1"), # Drell-Yan 
    (4, "tt_cat4_NbtagGe1")  # TTbar 
  ],
  'em' : [
    ( 1, "em_cat0_NbtagGe1"), # TTbar 
    ( 2, "em_cat1_NbtagGe1"), # DY
    ( 3, "em_cat2_NbtagGe1"), # Htautau signal
    ( 4, "em_cat3_NbtagGe1")  # HWW signal
  ]
}

replacement_dict = {
    "HWW125": "H_hww",
    "H125": "H_htt",
    "TTH": "ttH"
}

exact_replacement = {
  "ZH" : "ZH_htt",
  "WH" : "WH_htt",
  "ttH": "ttH_htt",
  "VBF": "qqH_htt"

}


for chn in chns:
  cb.AddObservations( ['*'], ['bbhtt'], ['13TeV'], [chn], categories[chn])
  cb.AddProcesses( ['*'], ['bbhtt'], ['13TeV'], [chn], bkg_procs[chn], categories[chn], False)
  cb.AddProcesses( ['*'], ['bbhtt'], ['13TeV'], [chn], sig_procs[chn], categories[chn], True)


systs.AddCommonSystematics(cb,year)

if args.year=='2018':
  systs.AddSystematics2018(cb)
if args.year=='2017':
  systs.AddSystematics2017(cb)
if args.year=='2016':
  systs.AddSystematics2016(cb)


cb.AddDatacardLineAtEnd("* autoMCStats 0")

for chn in chns:
  inputfile = shapes + '/htt_'+chn+'_bbH.Run'+year+'.root' 
  if chn in ["et","mt"]:
    #inputfile = shapes + '/htt_'+chn+'_bbH_comb.Run'+year+'.root' 
    cb.cp().channel([chn]).backgrounds().ExtractShapes(inputfile, '$BIN/$PROCESS', '$BIN/$PROCESS_$SYSTEMATIC') 
    cb.cp().channel([chn]).signals().ExtractShapes(inputfile, '$BIN/$PROCESS', '$BIN/$PROCESS_$SYSTEMATIC') 
  if chn in ["tt","em"]:
    cb.cp().channel([chn]).backgrounds().ExtractShapes(inputfile, '$BIN/$PROCESS', '$BIN/$PROCESS_$SYSTEMATIC') 
    cb.cp().channel([chn]).signals().ExtractShapes(inputfile, '$BIN/$PROCESS', '$BIN/$PROCESS_$SYSTEMATIC') 


for expr, replacement in replacement_dict.items():
  cb.cp().ForEachObj(lambda x: x.set_process(x.process().replace(expr, replacement)) if expr in x.process() else None) 


#semi leptonic channels


for expr, replacement in exact_replacement.items():
  cb.cp().ForEachObj(lambda x: x.set_process(replacement) if x.process()==expr else None) 



systs.ConvertToLnN(cb,year)

systs.renameSys(cb,year)

ch.SetStandardBinNames(cb)


def matching_proc(p,s):
  return ((p.bin()==s.bin()) and (p.process()==s.process()) and (p.signal()==s.signal()) 
         and (p.analysis()==s.analysis()) and  (p.era()==s.era()) 
         and (p.channel()==s.channel()) and (p.bin_id()==s.bin_id()) and (p.mass()==s.mass()))


def drop_bkg_interference(chob,proc):
  drop_mt_et =  proc.process()=='intH_htt' and (proc.channel()=='mt' or proc.channel()=='et') and (proc.bin_id()==2 or proc.bin_id()==3)
  drop_em =  (proc.process()=='intH_htt' or proc.process()=='intH_hww') and proc.channel()=='em' and (proc.bin_id()==2 or proc.bin_id()==1)
  drop_process = drop_mt_et or drop_em
  if(drop_process):
    chob.FilterSysts(lambda sys: matching_proc(proc,sys)) 
  return drop_process


cb.FilterProcs(lambda x: drop_bkg_interference(cb,x))
cb.FilterProcs(lambda x: drop_em_tt_qcd(cb,x))

#remove old datacards
for chn in chns:
  outdir = "output/" + args.output_folder + "/" + chn + year
  if os.path.isdir(outdir):
    for f in os.listdir(outdir):
      print "remove:",os.path.join(outdir,f)
      os.remove(os.path.join(outdir, f))

writer=ch.CardWriter("output/" + args.output_folder + "/$TAG/$BIN"+year+".txt",
                      "output/" + args.output_folder +"/$TAG/bbhtt_input_$BIN"+year+".root")
writer.SetWildcardMasses([])
writer.SetVerbosity(0);
                
#Combined:
writer.WriteCards("cmb",cb);

#Per channel:
for chn in chns:
  writer.WriteCards(chn,cb.cp().channel([chn]))

#Also have per-year cards available
peryearwriter=ch.CardWriter("output/" + args.output_folder + "/$TAG"+year+"/$BIN"+year+".txt",
                      "output/" + args.output_folder +"/$TAG"+year+"/bbhtt_input_$BIN"+year+".root")
peryearwriter.SetWildcardMasses([])
peryearwriter.SetVerbosity(0);
                
#Combined-per year:
peryearwriter.WriteCards("cmb",cb);

#Per channel-per year:
for chn in chns:
  peryearwriter.WriteCards(chn,cb.cp().channel([chn]))





 

