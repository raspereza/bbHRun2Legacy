#!/bin/bash
# $1 - channel
outputdir=${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/impacts_${1}
jobname=impacts_${1}

cat > ${outputdir}/${jobname}.sh <<EOF
#!/bin/sh
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cd ${CMSSW_BASE}/src
cmsenv
cd ${outputdir}
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 --rMin -10 --rMax 10 --robustFit 1 -t -1 --expectSignal 1 --doInitialFit 
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 --rMin -10 --rMax 10 --robustFit 1 -t -1 --expectSignal 1 --doFits
combineTool.py -M Impacts -d ${CMSSW_BASE}/src/CombineHarvester/bbHRun2Legacy/output/cards/${1}/ws.root -m 125.38 -o impacts_${1}.json
EOF
chmod u+x ${outputdir}/${jobname}.sh
cat > ${outputdir}/${jobname}.submit << EOF1
+RequestRuntime=50000

RequestMemory = 2000

executable = ${outputdir}/${jobname}.sh

transfer_executable = True
universe            = vanilla
getenv              = True
Requirements        = OpSysAndVer == "CentOS7"

output              = ${outputdir}/${jobname}.out
error               = ${outputdir}/${jobname}.error
log                 = ${outputdir}/${jobname}.log

queue
EOF1
chmod u+x ${outputdir}/${jobname}.submit
condor_submit ${outputdir}/${jobname}.submit

