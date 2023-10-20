import CombineHarvester.CombineTools.plotting as plot
import ROOT
from ROOT import TColor
import math
import argparse
import json
import sys
import os
import fnmatch
from array import array

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(False)

def getHistogram(fname, histname, dirname='', postfitmode='prefit', allowEmpty=False, logx=False):
  outname = fname.GetName()
  for key in fname.GetListOfKeys():
    histo = fname.Get(key.GetName())
    dircheck = False
    if dirname == '' : dircheck=True
    elif dirname in key.GetName(): dircheck=True
    if isinstance(histo,ROOT.TH1F) and key.GetName()==histname:
      if logx:
        bin_width = histo.GetBinWidth(1)
        xbins = []
        xbins.append(bin_width - 1)
        axis = histo.GetXaxis()
        for i in range(1,histo.GetNbinsX()+1):
         xbins.append(axis.GetBinUpEdge(i))
        rethist = ROOT.TH1F(histname,histname,histo.GetNbinsX(),array('d',xbins))
        rethist.SetBinContent(1,histo.GetBinContent(1)*(histo.GetBinWidth(1)-(bin_width - 1))/(histo.GetBinWidth(1)))
        rethist.SetBinError(1,histo.GetBinError(1)*(histo.GetBinWidth(1)-(bin_width - 1))/(histo.GetBinWidth(1)))
        for i in range(2,histo.GetNbinsX()+1):
          rethist.SetBinContent(i,histo.GetBinContent(i))
          rethist.SetBinError(i,histo.GetBinError(i))
        histo = rethist
      return [histo,outname]
    elif isinstance(histo,ROOT.TDirectory) and postfitmode in key.GetName() and dircheck:
      return getHistogram(histo,histname, allowEmpty=allowEmpty, logx=logx)
  print 'Failed to find %(postfitmode)s histogram with name %(histname)s in file %(fname)s '%vars()
  if allowEmpty:
    return [ROOT.TH1F('empty', '', 1, 0, 1), outname]
  else:
    return None

def signalComp(leg,plots,colour,style,norm=1.):
  return dict([('leg_text',leg),('plot_list',plots),('colour',colour),('style',style),('norm',norm)])

def backgroundComp(leg,plots,colour):
  return dict([('leg_text',leg),('plot_list',plots),('colour',colour)])

def createAxisHists(n,src,xmin=0,xmax=499):
  result = []
  for i in range(0,n):
    res = src.Clone()
    res.Reset()
    res.SetTitle("")
    res.SetName("axis%(i)d"%vars())
    res.SetAxisRange(xmin,xmax)
    res.SetStats(0)
    result.append(res)
  return result
  

plot.ModTDRStyle(r=0.04, l=0.14)

parser = argparse.ArgumentParser()
#Ingredients when output of PostFitShapes is already provided
parser.add_argument('--file', '-f',help='Input file if shape file has already been created')
parser.add_argument('-c','--channel',dest='channel', type=str, default='mt',action='store')
parser.add_argument('-y','--year', dest='year', type=str, default='2018', action='store')
parser.add_argument('--category',dest='category', type=str, action='store')
#Ingredients to internally call PostFitShapes
parser.add_argument('--dir', '-d', help='Directory for plot (channel-category containing the datacard and workspace)')
parser.add_argument('--postfitshapes',default=False,action='store_true',help='Run PostFitShapesFromWorkspace')
parser.add_argument('--workspace',default='mhmodp',help='Part of workspace filename right before .root')
parser.add_argument('--fitresult',help='Full path to fit result for making post fit plots')
parser.add_argument('--mode',default='prefit',help='prefit or postfit')
#Blinding options
parser.add_argument('--manual_blind', action='store_true',default=False,help='Blind data with hand chosen range')
parser.add_argument('--auto_blind',action='store_true',default=False,help='Blind data automatically based on s/root b')
parser.add_argument('--auto_blind_check_only',action='store_true',default=False,help='Only print blinding recommendation but still blind data using manual blinding')
parser.add_argument('--soverb_plot', action='store_true',default=False,help='Make plot with s/root b instead of ratio plot to test what it would blind')
parser.add_argument('--x_blind_min',default=0.7,help='Minimum x for manual blinding')
parser.add_argument('--x_blind_max',default=1.,help='Maximum x for manual blinding')
parser.add_argument('--empty_bin_error',action='store_true',default=False, help='Draw error bars for empty bins')
#General plotting options
parser.add_argument('--channel_label',default='#mu#tau_{h}',help='Channel - category label')
parser.add_argument('--ratio', default=False,action='store_true',help='Draw ratio plot')
parser.add_argument('--custom_x_range', help='Fix x axis range', action='store_true', default=False)
parser.add_argument('--x_axis_min',  help='Fix x axis minimum', default=0.0)
parser.add_argument('--x_axis_max',  help='Fix x axis maximum', default=1000.0)
parser.add_argument('--custom_y_range', help='Fix y axis range', action='store_true', default=False)
parser.add_argument('--y_axis_min',  help='Fix y axis minimum', default=1.)
parser.add_argument('--y_axis_max',  help='Fix y axis maximum', default=100.0)
parser.add_argument('--log_y', action='store_true',help='Use log for y axis')
parser.add_argument('--log_x', action='store_true',help='Use log for x axis')
parser.add_argument('--extra_pad', help='Fraction of extra whitespace at top of plot',default=0.0)
parser.add_argument('--outname',default='',help='Optional string for start of output filename')
parser.add_argument('--uniform_binning', default=False, action='store_true', help='Make plots in which each bin has the same width') 
parser.add_argument('--ratio_range',  help='y-axis range for ratio plot in format MIN,MAX', default="0.7,1.3")
parser.add_argument('--no_signal', action='store_true',help='Do not draw signal')
parser.add_argument('--sb_vs_b_ratio', action='store_true',help='Draw a Signal + Background / Background into the ratio plot')


args = parser.parse_args()

workspace = args.workspace
year = args.year
channel_label = args.channel_label
channel = args.channel
category = args.category
fitresult = args.fitresult
mode = args.mode
manual_blind = args.manual_blind
auto_blind = args.auto_blind
soverb_plot = args.soverb_plot
auto_blind_check_only = args.auto_blind_check_only
x_blind_min = args.x_blind_min
x_blind_max = args.x_blind_max
empty_bin_error = args.empty_bin_error
extra_pad = float(args.extra_pad)
custom_x_range = args.custom_x_range
custom_y_range = args.custom_y_range
x_axis_min = float(args.x_axis_min)
x_axis_max = float(args.x_axis_max)
y_axis_min = float(args.y_axis_min)
y_axis_max = float(args.y_axis_max)
log_y=args.log_y
log_x=args.log_x
sb_vs_b_ratio = args.sb_vs_b_ratio
uniform=args.uniform_binning
if uniform:
  log_y = False
  log_x = False
if(args.outname != ''):
  outname=args.outname + '_'
else:
  outname=''


categories = {
  'tt': {'1': 'Htt signal class',
         '2': 'Fake class',
         '3': 'DY class',
         '4': 'TT class'},
  'mt': {'1': 'Htt signal class',
         '2': 'TT class',
         '3': 'DY class'},
  'et': {'1': 'Htt signal class',
         '2': 'TT class',
         '3': 'DY class'},
  'em': {'1': 'TT class',
         '2': 'DY class',
         '3': 'Htt signal class',
         '4': 'HWW signal class'}}

mode_sig = 'prefit'
file_dir = 'bbhtt_'+channel+'_'+category+'_13TeV'+year+'_'+mode
file_dir_sig = 'bbhtt_'+channel+'_'+category+'_13TeV'+year+'_'+mode_sig

if year=="2018":
  lumi = "2018 59.7 fb^{-1} (13 TeV)"
elif year=="2017":
  lumi = "2017 41.5 fb^{-1} (13 TeV)"
elif year=="2016":
  lumi = "2016 36.3 fb^{-1} (13 TeV)"

if channel == "tt":
  channel_label = "#tau_{h}#tau_{h}, "+categories[channel][category]
if channel == "mt":
  channel_label = "#mu#tau_{h}, "+categories[channel][category]
elif channel == "et":
  channel_label = "e#tau_{h}, "+categories[channel][category]
elif channel == "em":
  channel_label = "e#mu, "+categories[channel][category]

x_title = "BDT"
y_title = "Events"
"""
if channel in ['tt','mt','et'] and category == '1':
  manual_blind = True
if channel == 'em' and category in ['3','4']:
  manual_blind = True
"""  

if args.dir and args.file and not args.postfitshapes:
  print 'Provide either directory or filename, not both'
  sys.exit(1)

if not args.dir and not args.file and not args.postfitshapes:
  print 'Provide one of directory or filename'
  sys.exit(1)

#if args.postfitshapes and not args.dir:
#  print 'Provide directory when running with --postfitshapes option'
#  sys.exit(1)
 
print "Providing shape file: ", args.file, ", with specified subdir name: ", file_dir
shape_file=args.file
shape_file_name=args.file

histo_file = ROOT.TFile(shape_file)

#Store plotting information for different backgrounds 
background_schemes = {
  'mt':[backgroundComp("H(125)",["ZH_htt","WH_htt","ggH_htt","ttH_htt"],TColor.GetColor(250, 202, 255)),
        backgroundComp("electroweak",["ST","VV"],TColor.GetColor(222,90,106)),
        backgroundComp("jet#rightarrow#tau_{h} fakes",["QCD"],TColor.GetColor("#c6f74a")),
	backgroundComp("t#bar{t}",["TT"], TColor.GetColor(155, 152, 204)),
	backgroundComp("Drell-Yan",["DYJets"], TColor.GetColor(248, 206, 104))],
  'et':[backgroundComp("H(125)",["ZH_htt","WH_htt","ggH_htt","ttH_htt"],TColor.GetColor(250, 202, 255)),
        backgroundComp("electroweak",["ST","VV"],TColor.GetColor(222,90,106)),
        backgroundComp("jet#rightarrow#tau_{h} fakes",["QCD"],TColor.GetColor("#c6f74a")),
	backgroundComp("t#bar{t}",["TT"], TColor.GetColor(155, 152, 204)),
	backgroundComp("Drell-Yan",["DYJets"], TColor.GetColor(248, 206, 104))],
  'tt': [backgroundComp("H(125)",["ggH_htt","qqH_htt","ZH_htt","WH_htt","ttH_htt"], ROOT.TColor.GetColor(250, 202, 255)),
         backgroundComp("electroweak",["ST","VV"],TColor.GetColor(222,90,106)),
         backgroundComp("j#rightarrow#tau mis-id",["jetFakes","wFakes"],TColor.GetColor("#c6f74a")),
         backgroundComp("t#bar{t}",["TT"], TColor.GetColor(155, 152, 204)),
	 backgroundComp("Drell-Yan",["ZTT","ZL"], TColor.GetColor(248, 206, 104))],
  'em':[backgroundComp("H(125)",["ggH_htt", "qqH_htt", "ZH_htt", "WH_htt", "ttH_htt", "ggH_hww", "qqH_hww", "WH_hww", "ZH_hww", "ttH_hww"], ROOT.TColor.GetColor(250, 202, 255)),
        backgroundComp("electroweak",["ST","VV","W","TTVJets"],TColor.GetColor(222,90,106)),
	backgroundComp("QCD",["QCD"],ROOT.TColor.GetColor("#c6f74a")),
	backgroundComp("t#bar{t}",["TT"], TColor.GetColor(155, 152, 204)),
	backgroundComp("Drell-Yan",["ZTT","ZL"], TColor.GetColor(248, 206, 104))]}

signal_schemes = {'mt' :[signalComp("bbH+ggH",['bbH_htt','ggH_bb_htt','intH_bb_htt'],4,1,50)],
'et' :[signalComp("bbH+ggH",['bbH_htt','ggH_bb_htt','intH_bb_htt'],4,1,50)],
'tt' :[signalComp("bbH#tau#tau",['bbH_htt','ggH_bb_htt','intH_bb_htt'],4,1,50)],
'em' :[signalComp("bbH#tau#tau",['bbH_htt','ggH_bb_htt','intH_bb_htt'],4,1,50),signalComp("bbHWW",['bbH_hww','ggH_bb_hww','intH_bb_hww'],7,1,50)]}

if channel=="em" and category=="1": #no QCD process for tt class of em channel
  background_schemes = {'em':[backgroundComp("H(125)",["ggH_htt", "qqH_htt", "ZH_htt", "WH_htt", "ttH_htt", "ggH_hww", "qqH_hww", "WH_hww", "ZH_hww", "ttH_hww"], ROOT.TColor.GetColor(250, 202, 255)),
        backgroundComp("electroweak",["ST","VV","W","TTVJets"],TColor.GetColor(222,90,106)),
	backgroundComp("t#bar{t}",["TT"], TColor.GetColor(155, 152, 204)),
	backgroundComp("Drell-Yan",["ZTT","ZL"], TColor.GetColor(248, 206, 104))]}


#Extract relevent histograms from shape file
sig_histos = []
for i,t in enumerate(signal_schemes[channel]):
  plots = t['plot_list']
  h = ROOT.TH1F()
  for j,k in enumerate(plots):
    if h.GetEntries()==0 and getHistogram(histo_file,k, file_dir_sig,mode_sig,logx=log_x) is not None:
      if not uniform:
        h = getHistogram(histo_file,k, file_dir_sig,mode_sig, logx=log_x)[0]
      else :
        htemp = getHistogram(histo_file,k,file_dir_sig, mode_sig,logx=log_x)[0]
        h = ROOT.TH1F(k,k,htemp.GetNbinsX(),0,htemp.GetNbinsX())
        for bp in range(0,htemp.GetNbinsX()):
          h.SetBinContent(bp+1,htemp.GetBinContent(bp+1))
          h.SetBinError(bp+1,htemp.GetBinError(bp+1))
      h.SetName(k)
    else:
      if getHistogram(histo_file,k, file_dir_sig,mode_sig, logx=log_x) is not None:
        if not uniform:
          h.Add(getHistogram(histo_file,k, file_dir_sig,mode_sig,logx=log_x)[0])
        else :
          htemp = getHistogram(histo_file,k,file_dir_sig, mode_sig,logx=log_x)[0]
          htemp2 = ROOT.TH1F(k,k,htemp.GetNbinsX(),0,htemp.GetNbinsX())
          for bp in range(0,htemp.GetNbinsX()):
            htemp2.SetBinContent(bp+1,htemp.GetBinContent(bp+1))
            htemp2.SetBinError(bp+1,htemp.GetBinError(bp+1))
          h.Add(htemp2)
  h.SetLineColor(t['colour'])
  h.SetLineStyle(t['style'])
  h.SetLineWidth(3)
  h.Scale(t['norm'])
  sig_histos.append(h)

sighist = getHistogram(histo_file,'TotalSig', file_dir_sig, mode_sig, args.no_signal, log_x)[0]
if sb_vs_b_ratio:
    sbhist = getHistogram(histo_file,'TotalProcs',file_dir, mode, args.no_signal, log_x)[0]
    bkg_sb_vs_b_ratio_hist = getHistogram(histo_file,'TotalBkg',file_dir, mode, logx=log_x)[0]
for i in range(0,sighist.GetNbinsX()):
  if sighist.GetBinContent(i) < y_axis_min: sighist.SetBinContent(i,y_axis_min)
bkghist = getHistogram(histo_file,'TotalBkg',file_dir, mode, logx=log_x)[0]

total_datahist = getHistogram(histo_file,"data_obs",file_dir, mode, logx=log_x)[0]
binerror_datahist = total_datahist.Clone()
blind_datahist = total_datahist.Clone()
total_datahist.SetMarkerStyle(20)
blind_datahist.SetMarkerStyle(20)
blind_datahist.SetLineColor(1)

#If using in test automated blinding mode, build the s/root b histogram for the ratio 
sighist_forratio = sighist.Clone()
sighist_forratio.SetName("sighist_forratio")
if soverb_plot:
    for j in range(1,bkghist.GetNbinsX()+1):
      soverb = sighist.GetBinContent(j)/math.sqrt(bkghist.GetBinContent(j))
      sighist_forratio.SetBinContent(j,soverb)
      sighist_forratio.SetBinError(j,0)
    


#Blinding by hand using requested range, set to 0.7-1.0 by default
if manual_blind or auto_blind_check_only:
  for i in range(0,total_datahist.GetNbinsX()):
    low_edge = total_datahist.GetBinLowEdge(i+1)
    high_edge = low_edge+total_datahist.GetBinWidth(i+1)
    if ((low_edge > float(x_blind_min) and low_edge < float(x_blind_max)) or (high_edge > float(x_blind_min) and high_edge<float(x_blind_max))):
      blind_datahist.SetBinContent(i+1,-0.1)
      blind_datahist.SetBinError(i+1,0)


#Set bin errors for empty bins if required:
if empty_bin_error:
  for i in range (1,blind_datahist.GetNbinsX()+1):
    if blind_datahist.GetBinContent(i) == 0:
      blind_datahist.SetBinError(i,1.8)

if uniform:
  blind_datahist2 = ROOT.TH1F(blind_datahist.GetName(),blind_datahist.GetName(),blind_datahist.GetNbinsX(),0,blind_datahist.GetNbinsX())
  total_datahist2 = ROOT.TH1F(total_datahist.GetName(),total_datahist.GetName(),total_datahist.GetNbinsX(),0,total_datahist.GetNbinsX())
  bkghist2 = ROOT.TH1F(bkghist.GetName(),bkghist.GetName(),bkghist.GetNbinsX(),0,bkghist.GetNbinsX())
  for i in range(0,blind_datahist.GetNbinsX()):
    blind_datahist2.SetBinContent(i,blind_datahist.GetBinContent(i))
    blind_datahist2.SetBinError(i,blind_datahist.GetBinError(i))
    total_datahist2.SetBinContent(i,total_datahist.GetBinContent(i))
    total_datahist2.SetBinError(i,total_datahist.GetBinError(i))
  blind_datahist = blind_datahist2
  total_datahist = total_datahist2
  for i in range(0,bkghist.GetNbinsX()):
    bkghist2.SetBinContent(i,bkghist.GetBinContent(i))
    bkghist2.SetBinError(i,bkghist.GetBinError(i))
  bkghist = bkghist2

  

#Normalise by bin width except in soverb_plot mode, where interpretation is easier without normalising
#Also don't normalise by bin width if plotting fractional bkg contribution
"""
if not soverb_plot and not uniform:
    blind_datahist.Scale(1.0,"width")
    total_datahist.Scale(1.0,"width")
    sighist.Scale(1.0,"width")
    bkghist.Scale(1.0,"width")
"""

#Create stacked plot for the backgrounds
bkg_histos = []
for i,t in enumerate(background_schemes[channel]):
  plots = t['plot_list']
  h = ROOT.TH1F()
  for j,k in enumerate(plots):
    if h.GetEntries()==0 and getHistogram(histo_file,k, file_dir,mode,logx=log_x) is not None:
      if not uniform:
        h = getHistogram(histo_file,k, file_dir,mode, logx=log_x)[0]
      else :
        htemp = getHistogram(histo_file,k,file_dir, mode,logx=log_x)[0]
        h = ROOT.TH1F(k,k,htemp.GetNbinsX(),0,htemp.GetNbinsX())
        for bp in range(0,htemp.GetNbinsX()):
          h.SetBinContent(bp+1,htemp.GetBinContent(bp+1))
          h.SetBinError(bp+1,htemp.GetBinError(bp+1))
      h.SetName(k)
    else:
      if getHistogram(histo_file,k, file_dir,mode, logx=log_x) is not None:
        if not uniform:
          h.Add(getHistogram(histo_file,k, file_dir,mode,logx=log_x)[0])
        else :
          htemp = getHistogram(histo_file,k,file_dir, mode,logx=log_x)[0]
          htemp2 = ROOT.TH1F(k,k,htemp.GetNbinsX(),0,htemp.GetNbinsX())
          for bp in range(0,htemp.GetNbinsX()):
            htemp2.SetBinContent(bp+1,htemp.GetBinContent(bp+1))
            htemp2.SetBinError(bp+1,htemp.GetBinError(bp+1))
          h.Add(htemp2)
  h.SetFillColor(t['colour'])
  h.SetLineColor(ROOT.kBlack)
  h.SetMarkerSize(0)
  
  #if not soverb_plot and not uniform : h.Scale(1.0,"width")
  bkg_histos.append(h)

stack = ROOT.THStack("hs","")
for hists in bkg_histos:
  stack.Add(hists)



#Setup style related things
c2 = ROOT.TCanvas()
c2.cd()

if args.ratio:
  pads=plot.TwoPadSplit(0.29,0.01,0.01)
else:
  pads=plot.OnePad()
pads[0].cd()
if(log_y):
  pads[0].SetLogy(1)
if(log_x):
  pads[0].SetLogx(1)

if custom_x_range:
    if x_axis_max > bkghist.GetXaxis().GetXmax(): x_axis_max = bkghist.GetXaxis().GetXmax()
if args.ratio:
  if(log_x): pads[1].SetLogx(1)
  axish = createAxisHists(2,bkghist,bkghist.GetXaxis().GetXmin(),bkghist.GetXaxis().GetXmax()-0.01)
  axish[1].GetXaxis().SetTitle(x_title)
  axish[1].GetYaxis().SetNdivisions(4)
  if soverb_plot: 
    axish[1].GetYaxis().SetTitle("S/#sqrt(B)")
  elif sb_vs_b_ratio: 
    axish[1].GetYaxis().SetTitle("")
  else: 
    axish[1].GetYaxis().SetTitle("Obs/Exp")
  #axish[1].GetYaxis().SetTitleSize(0.04)
  axish[1].GetYaxis().SetLabelSize(0.033)
  axish[1].GetXaxis().SetLabelSize(0.033)
  #axish[1].GetYaxis().SetTitleOffset(1.3)
  axish[0].GetYaxis().SetTitleSize(0.048)
  axish[0].GetYaxis().SetLabelSize(0.033)
  axish[0].GetYaxis().SetTitleOffset(1.44)
  axish[0].GetXaxis().SetTitleSize(0)
  axish[0].GetXaxis().SetLabelSize(0)
  axish[0].GetXaxis().SetRangeUser(x_axis_min,bkghist.GetXaxis().GetXmax()-0.01)
  axish[1].GetXaxis().SetRangeUser(x_axis_min,bkghist.GetXaxis().GetXmax()-0.01)
  axish[0].GetXaxis().SetMoreLogLabels()
  axish[0].GetXaxis().SetNoExponent()
  axish[1].GetXaxis().SetMoreLogLabels()
  axish[1].GetXaxis().SetNoExponent()

  if custom_x_range:
    axish[0].GetXaxis().SetRangeUser(x_axis_min,x_axis_max-0.01)
    axish[1].GetXaxis().SetRangeUser(x_axis_min,x_axis_max-0.01)
  if custom_y_range:
    axish[0].GetYaxis().SetRangeUser(y_axis_min,y_axis_max)
    axish[1].GetYaxis().SetRangeUser(y_axis_min,y_axis_max)

if not soverb_plot: axish[0].GetYaxis().SetTitle(y_title)
elif soverb_plot: axish[0].GetYaxis().SetTitle("Events")
axish[0].GetXaxis().SetTitle(x_title)
if not custom_y_range: axish[0].SetMaximum(extra_pad*bkghist.GetMaximum())
if not custom_y_range: 
  if(log_y): 
    if channel == "mt" or channel == "et":
      axish[0].SetMinimum(1.)
    else:
      axish[0].SetMinimum(1.)
  else: axish[0].SetMinimum(0)

hist_indices = [0]
for i in hist_indices:
    pads[i].cd()
    axish[i].Draw("AXIS")

    #Draw uncertainty band
    bkghist.SetFillColor(plot.CreateTransparentColor(12,0.4))
    bkghist.SetLineColor(0)
    bkghist.SetMarkerSize(0)

    stack.Draw("histsame")
    #Don't draw total bkgs/signal if plotting bkg fractions
    if not uniform:
      bkghist.Draw("e2same")
      if not args.no_signal:
        for legi,hists in enumerate(sig_histos):
          hists.Draw("histsame")
    if not soverb_plot: 
      blind_datahist.DrawCopy("e0x0same")
    axish[i].Draw("axissame")

pads[0].cd()
#Setup legend
legend = plot.PositionedLegend(0.35,0.15,3,0.03)
legend.SetNColumns(2)
legend.SetTextFont(42)
legend.SetTextSize(0.02)
legend.SetFillStyle(0)

signal_legend = None
if not args.no_signal:
    signal_legend = plot.PositionedLegend(0.2,0.05,3,0.18)
    signal_legend.SetTextFont(42)
    signal_legend.SetTextSize(0.02)
    signal_legend.SetFillStyle(0)

if not soverb_plot: legend.AddEntry(total_datahist,"Observed","PE")
#Drawn on legend in reverse order looks better
bkg_histos.reverse()
background_schemes[channel].reverse()
for legi,hists in enumerate(bkg_histos):
  legend.AddEntry(hists,background_schemes[channel][legi]['leg_text'],"f")
legend.AddEntry(bkghist,"Total Uncertainty","f")

if not args.no_signal:
  for legi,hists in enumerate(sig_histos):
    signal_legend.AddEntry(hists,signal_schemes[channel][legi]['leg_text']+" x %s"%signal_schemes[channel][legi]['norm'],"l")
                      
legend.Draw("same")
if not args.no_signal: signal_legend.Draw("same")

# Channel & Category label
latex2 = ROOT.TLatex()
latex2.SetNDC()
latex2.SetTextAngle(0)
latex2.SetTextColor(ROOT.kBlack)
latex2.SetTextSize(0.04)
latex2.DrawLatex(0.2,0.75,channel_label)

#CMS and lumi labels
plot.FixTopRange(pads[0], plot.GetPadYMax(pads[0]), extra_pad if extra_pad>0 else 0.37)
plot.DrawCMSLogo(pads[0], 'CMS', 'Internal', 11, 0.045, 0.05, 1.0, '', 1.0)
plot.DrawTitle(pads[0], lumi, 3)

#Add ratio plot if required
if args.ratio and not soverb_plot:
  ratio_bkghist = plot.MakeRatioHist(bkghist,bkghist,True,False)
  blind_datahist = plot.MakeRatioHist(blind_datahist,bkghist,True,False)
  if sb_vs_b_ratio:
    ratio_sbhist = plot.MakeRatioHist(sbhist,bkg_sb_vs_b_ratio_hist,True,False)
  
  pads[1].cd()
  pads[1].SetGrid(0,1)
  axish[1].Draw("axis")
  axish[1].SetMinimum(float(args.ratio_range.split(',')[0]))
  axish[1].SetMaximum(float(args.ratio_range.split(',')[1]))
  ratio_bkghist.SetMarkerSize(0)
  ratio_bkghist.Draw("e2same")
  if sb_vs_b_ratio:
    ratio_sbhist.SetMarkerSize(0)
    ratio_sbhist.SetLineColor(ROOT.kGreen+3)
    ratio_sbhist.SetLineWidth(3)
    ratio_sbhist.Draw("histsame][")
  blind_datahist.DrawCopy("e0x0same")
  pads[1].RedrawAxis("G")
  if sb_vs_b_ratio:
    # Add a ratio legend for y-splitted plots or plots with sb vs b ratios
    rlegend = plot.PositionedLegend(0.35,0.04,4,0.015,0.01)
    rlegend.SetTextFont(42)
    rlegend.SetTextSize(0.025)
    rlegend.SetFillStyle(1001)
    rlegend.SetFillColor(plot.CreateTransparentColor(3,0.2))
    rlegend.SetNColumns(2)
    rlegend.AddEntry(blind_datahist,"Obs/Bkg","PE")
    if sb_vs_b_ratio:
      rlegend.AddEntry(ratio_sbhist,"(Sig+Bkg)/Bkg","L")
    rlegend.Draw("same")
if soverb_plot:
  pads[1].cd()
  pads[1].SetGrid(0,1)
  axish[1].Draw("axis")
  axish[1].SetMinimum(0)
  axish[1].SetMaximum(10)
  sighist_forratio.SetLineColor(2)
  sighist_forratio.Draw("same")

pads[0].cd()
pads[0].GetFrame().Draw()
pads[0].RedrawAxis()



#Save as png and pdf with some semi sensible filename
if mode == "postfit":
  outname = mode+'/'+file_dir
else:
  outname = mode+'/'+file_dir
c2.SaveAs("%(outname)s.png"%vars())
#c2.SaveAs("%(outname)s.pdf"%vars())
