cd ..
python scripts/setupCards.py --year 2018 --channel mt
combineTool.py -M T2W -i output/cards/mt2018 -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
cd impacts
combineTool.py -M Impacts -d ../output/cards/mt2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/mt2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/mt2018/ws.root -m 125.38 -o impacts_mt2018_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_mt2018_nostat.json -o impacts_mt2018_nostat
rm higgsCombine_*

