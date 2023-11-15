for CH in em
do
    for CAT in 1
    do 
	PostFitShapesFromWorkspace -w run2plotcards/${CH}/ws.root -o prepostfit_shapes/Prepostfit_${CH}.root -m 125.38 -f output/cards/cmb/fitDiagnostics.ws.root:fit_s --total-shapes --postfit -d run2plotcards/${CH}/combined.txt.cmb
	python scripts/makeRun2Histo.py prepostfit_shapes/Prepostfit_${CH}.root --channel $CH --mode prefit --category $CAT
	python scripts/makeRun2Histo.py prepostfit_shapes/Prepostfit_${CH}.root --channel $CH --mode postfit --category $CAT
	python scripts/plotPostFit.py --file prepostfit_shapes/Prepostfit_${CH}.root --mode prefit --ratio --log_y --channel $CH --year Run2 --category $CAT
	python scripts/plotPostFit.py --file prepostfit_shapes/Prepostfit_${CH}.root --mode postfit --postfitshapes --ratio --log_y --channel $CH --year Run2 --category $CAT
    done
done
#for CH in mt et
#do
#    for CAT in 1 2 3
#    do 
#	PostFitShapesFromWorkspace -w run2plotcards/${CH}_${CAT}/ws.root -o prepostfit_shapes/Prepostfit_${CH}_${CAT}.root -m 125.38 -f output/cards/cmb/fitDiagnostics.ws.root:fit_s --total-shapes --postfit -d run2plotcards/${CH}_${CAT}/combined.txt.cmb
#	python scripts/makeRun2Histo_v2.py prepostfit_shapes/Prepostfit_${CH}_${CAT}.root --channel $CH --mode prefit --category $CAT
#	python scripts/makeRun2Histo_v2.py prepostfit_shapes/Prepostfit_${CH}_${CAT}.root --channel $CH --mode postfit --category $CAT
#	python scripts/plotPostFit.py --file prepostfit_shapes/Prepostfit_${CH}_${CAT}.root --mode prefit --ratio --log_y --channel $CH --year Run2 --category $CAT
#	python scripts/plotPostFit.py --file prepostfit_shapes/Prepostfit_${CH}_${CAT}.root --mode postfit --postfitshapes --ratio --log_y --channel $CH --year Run2 --category $CAT
#    done
#done

