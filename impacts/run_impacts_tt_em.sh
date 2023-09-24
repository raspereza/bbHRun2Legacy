cd ..
python scripts/setupCards.py --year 2018 --channel tt
python scripts/setupCards.py --year 2018 --channel em
combineTool.py -M T2W -i output/cards/tt2018 -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
combineTool.py -M T2W -i output/cards/em2018 -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
cd impacts
combineTool.py -M Impacts -d ../output/cards/tt2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/tt2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/tt2018/ws.root -m 125.38 -o impacts_tt2018.json
plotImpacts.py -i impacts_tt2018.json -o impacts_tt2018
combineTool.py -M Impacts -d ../output/cards/tt2018/ws.root -m 125.38 -o impacts_tt2018_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_tt2018_nostat.json -o impacts_tt2018_nostat
rm higgsCombine_*
combineTool.py -M Impacts -d ../output/cards/em2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/em2018/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/em2018/ws.root -m 125.38 -o impacts_em2018.json
plotImpacts.py -i impacts_em2018.json -o impacts_em2018
combineTool.py -M Impacts -d ../output/cards/em2018/ws.root -m 125.38 -o impacts_em2018_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_em2018_nostat.json -o impacts_em2018_nostat
rm higgsCombine_*
