for CH in tt mt et em
do
    for YEAR in 2018 2017 2016
    do
	for CAT in 1 2 3 4
	do 

	    python scripts/plotPostFit.py --file comb_shapes.root --mode prefit --ratio --log_y --channel $CH --year $YEAR --category $CAT
	    python scripts/plotPostFit.py --file comb_shapes.root --mode postfit --postfitshapes --ratio --log_y --channel $CH --year $YEAR --category $CAT
	done
    done
done
