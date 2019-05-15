from CMGTools.TTHAnalysis.treeReAnalyzer import *

class EventVars2LSS:
    def __init__(self, label="", recllabel='Recl'):
        self.namebranches = [ "mindr_lep1_jet",
                              "mindr_lep2_jet",
                              "avg_dr_jet",
                              "MT_met_lep1",
                              #"MT_met_leplep",
                              #"sum_abspz",
                              #"sum_sgnpz"
                              ]
        self.label = "" if (label in ["",None]) else ("_"+label)
        self.systsJEC = {0:"", 1:"_jecUp", -1:"_jecDown"}
        self.inputlabel = '_'+recllabel
        self.branches = []
        for var in self.systsJEC: self.branches.extend([br+self.label+self.systsJEC[var] for br in self.namebranches])
    def listBranches(self):
        return self.branches[:]
    def __call__(self,event):

        allret = {}

        leps = [l for l in Collection(event,"LepFO","nLepFO")]

        for var in self.systsJEC:
            _var = var
            if not hasattr(event,"nJet25"+self.systsJEC[var]+self.inputlabel): _var = 0
            jets = [j for j in Collection(event,"JetSel","nJetSel")]
            jetptcut = 25
            if (_var==0): jets = filter(lambda x : x.pt>jetptcut, jets)
            elif (_var==1): jets = filter(lambda x : x.pt*x.corr_JECUp/x.corr>jetptcut, jets)
            elif (_var==-1): jets = filter(lambda x : x.pt*x.corr_JECDown/x.corr>jetptcut, jets)

            ### USE ONLY ANGULAR JET VARIABLES IN THE FOLLOWING!!!

            met = getattr(event,'MET_years_pt_nom')
            metphi = getattr(event,'MET_years_phi_nom')
            njet = len(jets); nlep = len(leps)
            # prepare output
            ret = dict([(name,0.0) for name in self.namebranches])
            # fill output
            if njet >= 1:
                ret["mindr_lep1_jet"] = min([deltaR(j,leps[0]) for j in jets]) if nlep >= 1 else 0;
                ret["mindr_lep2_jet"] = min([deltaR(j,leps[1]) for j in jets]) if nlep >= 2 else 0;
            if njet >= 2:
                sumdr, ndr = 0, 0
                for i,j in enumerate(jets):
                    for i2,j2 in enumerate(jets[i+1:]):
                        ndr   += 1
                        sumdr += deltaR(j,j2)
                ret["avg_dr_jet"] = sumdr/ndr if ndr else 0;
            if nlep > 0:
                ret["MT_met_lep1"] = sqrt( 2*leps[0].conept*met*(1-cos(leps[0].phi-metphi)) )
#            if nlep > 1:
#                px = leps[0].conePt*cos(leps[0].phi) + leps[1].conePt*cos(leps[1].phi) + met*cos(metphi) 
#                py = leps[0].conePt*sin(leps[0].phi) + leps[1].conePt*sin(leps[1].phi) + met*sin(metphi) 
#                ht = leps[0].conePt + leps[1].conePt + met
#                ret["MT_met_leplep"] = sqrt(max(0,ht**2 - px**2 - py**2))
#            if nlep >= 1:
#                sumapz, sumspz = 0,0
#                for o in leps[:2] + jets:
#                    pz = o.conePt*sinh(o.eta) if o in leps else o.pt*sinh(o.eta)
#                    sumspz += pz
#                    sumapz += abs(pz); 
#                ret["sum_abspz"] = sumapz
#                ret["sum_sgnpz"] = sumspz

            for br in self.namebranches:
                allret[br+self.label+self.systsJEC[var]] = ret[br]
	 	
	return allret


if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    tree.vectorTree = True
    tree.AddFriend("sf/t",argv[2])
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = EventVars2LSS('','Recl')
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

        
