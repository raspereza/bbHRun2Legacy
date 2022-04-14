#!/usr/bin/env python

import CombineHarvester.CombineTools.ch as ch
import CombineHarvester.bbHRun2Legacy.systematics as systs
import ROOT as R
import glob
import numpy as np
import os
import sys
import argparse

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
    'mt' : ['QCD','TT','ST','WJets','DYJets','VBF','ZH','ttH','jjH','ggjjH','jjH_inc','VV'],
    'et' : ['QCD','TT','ST','WJets','DYJets','VBF','ZH','ttH','jjH','ggjjH','jjH_inc','VV'],
    'tt' : ['EMB','ZL','TTL','VVL','jetFakes', 'wFakes','ggH125','qqH125'],
    'em' : ['EMB','ZL','TTL','VVL','jetFakes', 'wFakes','ggH125','qqH125','ggHWW125','qqHWW125'] #FIXME
}

sig_procs = {
   'mt' : ['bbH','ggH'],
   'et' : ['bbH','ggH'],
   'tt' : ['bbH125','ggHbb125'],
   'em' : ['bbH125','ggHbb125','bbHWW125','ggHbbWW125']
}


categories = {
  'mt' : [
    (1, 'inclusive'),
    #(1, 'sig'),
    #(2, 'tt'),
    #(3, 'dy')
  ],
  'et' : [
    (1, 'inclusive'),
    #(1, 'sig'),
    #(2, 'tt'),
    #(3, 'dy')
  ],
  'tt' : [
    (1, "tt_cat0_NbtagGt1"),
    (2, "tt_cat1_NbtagGt1"),
    (3, "tt_cat2_NbtagGt1"),
    (4, "tt_cat3_NbtagGt1")
  ],
  'em' : [
     ( 1, "em_xxh"), 
     ( 4, "em_ttbar"),
     ( 6, "em_misc"),
     ( 7, "em_emb"),
     ( 8, "em_ss")
  ]
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
    cb.cp().channel([chn]).backgrounds().ExtractShapes(inputfile, 'BDToutput/$PROCESS', 'BDToutput/$PROCESS_$SYSTEMATIC') 
    cb.cp().channel([chn]).signals().ExtractShapes(inputfile, 'BDToutput/$PROCESS', 'BDToutput/$PROCESS_$SYSTEMATIC') 
    #cb.cp().channel([chn]).backgrounds().ExtractShapes(inputfile, 'BDToutput/$PROCESS_$BIN', 'BDToutput/$PROCESS_$BIN_$SYSTEMATIC') 
    #cb.cp().channel([chn]).signals().ExtractShapes(inputfile, 'BDToutput/$PROCESS_$BIN', 'BDToutput/$PROCESS_$BIN_$SYSTEMATIC')
  if chn in ["tt", "em"]:
    cb.cp().channel([chn]).backgrounds().ExtractShapes(inputfile, '$BIN/$PROCESS', '$BIN/$PROCESS_$SYSTEMATIC') 
    cb.cp().channel([chn]).signals().ExtractShapes(inputfile, '$BIN/$PROCESS', '$BIN/$PROCESS_$SYSTEMATIC') 

ch.SetStandardBinNames(cb)

#remove old datacards
outdir = "output/" + args.output_folder + "/" + chn + year
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





 


