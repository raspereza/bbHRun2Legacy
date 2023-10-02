# Instructions

## Setting up the area:

```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git checkout v8.2.0
cd ../..
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester -b 102x
cd CombineHarvester
git clone https://github.com/raspereza/bbHRun2Legacy.git bbHRun2Legacy
cd bbHRun2Legacy
git clone https://gitlab.cern.ch/adewit/bbhshapes.git shapes
cd ../..
scram b
```

The input shapes should be put in a directory `bbHRun2Legacy/shapes` and should be named `htt_CHANNEL_bbH.RunYEAR.root`, e.g. `htt_mt_bbH.Run2018.root`.
The scripts currently look for the individual process shapes in the main directory (tt, em) or in the `BDToutput` subdirectory (et, mt). Make sure the latest shapes for each channel are always in the `bbhshapes` repository so that everyone has access to them.

*TODO*: we should make sure the latest input shapes are always available to everyone, either by mirroring them from a common afs/eos directory or by sharing them in a separate repository.

The models should be copied to `HiggsAnalysis/CombinedLimit/python/`

## Setting up datacards

`python scripts/setupCards.py [options]`

The default channel is tt (set e.g. `--channel tt,mt` to run the tt and mt channels, or `--channel all` to run all 4 channels.
 
The default year is 2018, can switch this to other years but only one year will run at a time for the moment. If you run the script multiple times in succession, switching years in between but not changing the output directory, the datacards for each year will all end up in the correct place (/places).

## Make the workspace

`combineTool.py -M T2W -i output/cards/* -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root ` - this will make the workspace for all subdirectories. When running only one channel 'cmb' should equal that channel, otherwise there can be differences.

It is also possible to just run

`combineTool.py -M T2W -i output/cards/cmb -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root ` to produce the workspace only for the combined directory.

This will create workspaces with the default physics model, which creates one POI (r) which will scale both signal processes (ggH+2b and bbH). The interference term is scaled with -r.

For the kappa model run:

`combineTool.py -M T2W -i output/cards/* -P HiggsAnalysis.CombinedLimit.LHCHCGModels:K1Int -m 125.38 -o ws_kappas.root`

## Calculate limits

`combineTool.py -M AsymptoticLimits -d output/cards/cmb/ws.root --there --run blind`

Note the `--run blind` is important - we don't want to accidentally unblind the analysis.

## Impacts

To run the impacts one needs to run first an initial fit:
`combineTool.py -M Impacts -d output/cards/mt2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit`

Next the scan is done for each nuisance parameter:
`combineTool.py -M Impacts -d output/cards/mt2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits`

Once the jobs are completed the output can be collected with:
`combineTool.py -M Impacts -d output/cards/mt2018/ws.root -m 125.38 -o impacts.json`

and plotted with

`plotImpacts.py -i impacts.json -o impacts`

## MultiDimFit
The MultiDimFit for kappa_b and kappa_t is run with:

`combineTool.py -M MultiDimFit -d output/cards/cmb/ws_kappas.root --there --redefineSignalPOIs kappa_b,kappa_t --setParameters kappa_b=1,kappa_t=1 -m 125.38 --algo grid --points 300 -t -1`

The 2D plot for kappa_b and kappa_t can be produced with:

`python scripts/plotMultiDimFit.py output/cards/cmb/higgsCombine.Test.MultiDimFit.mH125.38.root`

Useful for debugging - just run a single fit (turn up the verbosity with -v 3 to get more detailed fit logs from minuit).

`combineTool.py -M MultiDimFit -d output/cards/cmb/ws.root --there -t -1 --expectSignal 1` (or `--expectSignal 0`) 

NB don't forget about the `-t -1` so as not to unblind accidentally

## Running FitDiagnostics
Useful for making post-fit plots of the signal region later / inspecting NP correlations&constraints without running the full impacts.

`combineTool.py -M FitDiagnostics -d output/cards/cmb/ws.root --there -t -1 --expectSignal 1` (or `--expectSignal 0`) 

NB don't forget about the `-t -1` so as not to unblind accidentally

