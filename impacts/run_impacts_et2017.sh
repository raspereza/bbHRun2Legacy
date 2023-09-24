cd ..
python scripts/setupCards.py --year 2017 --channel et
combineTool.py -M T2W -i output/cards/et2017 -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
cd impacts
combineTool.py -M Impacts -d ../output/cards/et2017/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/et2017/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/et2017/ws.root -m 125.38 -o impacts_et2017_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_et2017_nostat.json -o impacts_et2017_nostat
rm higgsCombine_*

