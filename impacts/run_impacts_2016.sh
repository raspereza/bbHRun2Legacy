cd ..
python scripts/setupCards.py --year 2016 --channel mt
python scripts/setupCards.py --year 2016 --channel et
combineTool.py -M T2W -i output/cards/mt2016 -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
combineTool.py -M T2W -i output/cards/et2016 -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
cd impacts
combineTool.py -M Impacts -d ../output/cards/mt2016/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/mt2016/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/mt2016/ws.root -m 125.38 -o impacts_mt2016.json
plotImpacts.py -i impacts_mt2016.json -o impacts_mt2016
combineTool.py -M Impacts -d ../output/cards/mt2016/ws.root -m 125.38 -o impacts_mt2016_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_mt2016_nostat.json -o impacts_mt2016_nostat
rm higgsCombine_*
combineTool.py -M Impacts -d ../output/cards/et2016/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/et2016/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/et2016/ws.root -m 125.38 -o impacts_et2016.json
plotImpacts.py -i impacts_et2016.json -o impacts_et2016
combineTool.py -M Impacts -d ../output/cards/et2016/ws.root -m 125.38 -o impacts_et2016_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_et2016_nostat.json -o impacts_et2016_nostat
rm higgsCombine_*
