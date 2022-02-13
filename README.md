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
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
cd CombineHarvester
git clone https://github.com/raspereza/bbHRun2Legacy.git bbHRun2Legacy
cd ..
scram b
```

The input shapes should be put in a directory `bbHRun2Legacy/shapes` and should be named `htt_CHANNEL_bbH.RunYEAR.root`, e.g. `htt_mt_bbH.Run2018.root`.
The scripts currently look for the individual process shapes in the main directory (tt, em) or in the `BDToutput` subdirectory (et, mt).

*TODO*: we should make sure the latest input shapes are always available to everyone, either by mirroring them from a common afs/eos directory or by sharing them in a separate repository.

## Setting up datacards

`python scripts/setupCards.py [options]`

The default channel is tt (set e.g. `--channel tt,mt` to run the tt and mt channels, or `--channel all` to run all 4 channels.
 
The default year is 2018, can switch this to other years but only one year will run at a time for the moment. If you run the script multiple times in succession, switching years in between but not changing the output directory, the datacards for each year will all end up in the correct place (/places).

*TODO* Uncertainty model is not complete
*TODO* Naming conventions between the different channels - we should make sure that they match so it's easier not to miss any processes

## Make the workspace

`combineTool.py -M T2W -i output/cards/* -o ws.root ` - this will make the workspace for all subdirectories. When running only one channel 'cmb' should equal that channel, otherwise there can be differences.

It is also possible to just run

`combineTool.py -M T2W -i output/cards/cmb -o ws.root ` to produce the workspace only for the combined directory.

This will create workspaces with the default physics model, which creates one POI (r) which will scale both signal processes (ggH+2b and bbH).

## Calculate limits

`combineTool.py -M AsymptoticLimits -i output/cards/cmb/ws.root --there --run blind`

Note the `--run blind` is important - we don't want to accidentally unblind the analysis.

## MultiDimFit
Useful for debugging - just run a single fit (turn up the verbosity with -v 3 to get more detailed fit logs from minuit).

`combineTool.py -M MultiDimFit -i output/cards/cmb/ws.root --there -t -1 --expectSignal 1` (or `--expectSignal 0`) 

NB don't forget about the `-t -1` so as not to unblind accidentally

## Running FitDiagnostics
Useful for making post-fit plots of the signal region later / inspecting NP correlations&constraints without running the full impacts.

`combineTool.py -M FitDiagnostics -i output/cards/cmb/ws.root --there -t -1 --expectSignal 1` (or `--expectSignal 0`) 

NB don't forget about the `-t -1` so as not to unblind accidentally

