#ifndef bbHRun2Legacy_HttSystematics_h
#define bbHRun2Legacy_HttSystematics_h
#include "CombineHarvester/CombineTools/interface/CombineHarvester.h"

namespace ch {
// Run2 bbH analysis
  void AddbbHRun2Systematics(CombineHarvester& cb, bool embedding, bool ttbar_rate, int era);
}

#endif
