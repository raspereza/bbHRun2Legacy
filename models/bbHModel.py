from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class bbHModel(PhysicsModel):
    def getYieldScale(self, bin, process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        self.modelBuilder.factory_('expr::negativer("-1*@0", r)')
        self.modelBuilder.out.function("negativer")
        if self.DC.isSignal[process]:
            if process in ["bbH_htt","ggH_bb_htt","bbH_hww","ggH_bb_hww"]:
                return "r"
            elif process in ["intH_bb_htt","intH_bb_hww"]:
                return "negativer"
        return 1

bbhModel = bbHModel()
