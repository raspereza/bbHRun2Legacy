cd ..
python scripts/setupCards.py --year 2018 --channel all
python scripts/setupCards.py --year 2017 --channel all
python scripts/setupCards.py --year 2016 --channel all
combineTool.py -M T2W -i output/cards/* -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
combineTool.py -M T2W -i output/cards/mt -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
combineTool.py -M T2W -i output/cards/et -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
cd impacts
combineTool.py -M Impacts -d ../output/cards/mt/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/mt/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/mt/ws.root -m 125.38 -o impacts_mt.json
plotImpacts.py -i impacts_mt.json -o impacts_mt
combineTool.py -M Impacts -d ../output/cards/mt/ws.root -m 125.38 -o impacts_mt_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_mt_nostat.json -o impacts_mt_nostat
rm higgsCombine_*
combineTool.py -M Impacts -d ../output/cards/et/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/et/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/et/ws.root -m 125.38 -o impacts_et.json
plotImpacts.py -i impacts_et.json -o impacts_et
combineTool.py -M Impacts -d ../output/cards/et/ws.root -m 125.38 -o impacts_et_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_et_nostat.json -o impacts_et_nostat
rm higgsCombine_*
combineTool.py -M Impacts -d ../output/cards/tt/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/tt/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20 --job-mode slurm
combineTool.py -M Impacts -d ../output/cards/tt/ws.root -m 125.38 -o impacts_tt.json
plotImpacts.py -i impacts_tt.json -o impacts_tt
combineTool.py -M Impacts -d ../output/cards/tt/ws.root -m 125.38 -o impacts_tt_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_tt_nostat.json -o impacts_tt_nostat
rm higgsCombine_*
combineTool.py -M Impacts -d ../output/cards/em/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/em/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20 --job-mode slurm
combineTool.py -M Impacts -d ../output/cards/em/ws.root -m 125.38 -o impacts_em.json
plotImpacts.py -i impacts_em.json -o impacts_em
combineTool.py -M Impacts -d ../output/cards/em/ws.root -m 125.38 -o impacts_em_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_em_nostat.json -o impacts_em_nostat
rm higgsCombine_*
combineTool.py -M Impacts -d ../output/cards/cmb/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit --rMin=-20 --rMax=20
combineTool.py -M Impacts -d ../output/cards/cmb/ws.root -m 125.38 --robustFit 1 -t -1 --expectSignal 1 --doFits --rMin=-20 --rMax=20 --job-mode slurm
combineTool.py -M Impacts -d ../output/cards/cmb/ws.root -m 125.38 -o impacts_cmb.json
plotImpacts.py -i impacts_cmb.json -o impacts_cmb
combineTool.py -M Impacts -d ../output/cards/cmb/ws.root -m 125.38 -o impacts_cmb_nostat.json --exclude 'rgx{prop.*}'
plotImpacts.py -i impacts_cmb_nostat.json -o impacts_cmb_nostat
rm higgsCombine_*
