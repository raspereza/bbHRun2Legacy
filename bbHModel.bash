#!/bin/bash
chan=$1
combineTool.py -M T2W -i output/cards/${chan}/* -P HiggsAnalysis.CombinedLimit.bbHModel:bbhModel -o ws.root
