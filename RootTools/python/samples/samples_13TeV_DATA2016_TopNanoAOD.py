from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

json='/nfs/fanae/user/clara/ttW_Top/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt'


#---------------------------RunB 2016 25Oct2019

DoubleMuon_Run2016B_25Oct2019_ver2 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016B_25Oct2019_ver2", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016B_25Oct2019_ver2 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016B_25Oct2019_ver2", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016B_25Oct2019_ver2 = kreator.makeMyPrivateDataComponent("DoubleEG_Run2016B_25Oct2019_ver2", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016B_25Oct2019_ver2 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016B_25Oct2019_ver2", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016B_25Oct2019_ver2 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016B_25Oct2019_ver2", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

#---------------------------RunC 2016 25Oct2019

DoubleMuon_Run2016C_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016C_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016C_25Oct2019 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016C_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016C_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleEG_Run2016C_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016C_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016C_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016C_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016C_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

#---------------------------RunD 2016 25Oct2019

DoubleMuon_Run2016D_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016D_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016D_25Oct2019 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016D_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016D_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleEG_Run2016D_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016D_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016D_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016D_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016D_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

#---------------------------RunE 2016 25Oct2019
DoubleMuon_Run2016E_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016E_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016E_25Oct2019 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016E_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016E_25Oct2019= kreator.makeMyPrivateDataComponent("DoubleEG_Run2016E_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016E_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016E_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016E_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016E_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

#---------------------------RunF 2016 25Oct2019

DoubleMuon_Run2016F_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016F_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016F_25Oct2019 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016F_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016F_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleEG_Run2016F_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016F_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016F_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016F_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016F_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

#---------------------------RunG 2016 25Oct2019

DoubleMuon_Run2016G_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016G_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016G_25Oct2019 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016G_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016G_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleEG_Run2016G_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016G_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016G_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016G_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016G_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

#---------------------------RunH 2016 25Oct2019

DoubleMuon_Run2016H_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleMuon_Run2016H_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
MuonEG_Run2016H_25Oct2019 = kreator.makeMyPrivateDataComponent("MuonEG_Run2016H_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
DoubleEG_Run2016H_25Oct2019 = kreator.makeMyPrivateDataComponent("DoubleEG_Run2016H_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleMuon_Run2016H_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleMuon_Run2016H_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)
SingleElectron_Run2016H_25Oct2019 = kreator.makeMyPrivateDataComponent("SingleElectron_Run2016H_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", "PRIVATE", ".*root", 'phys03',  json=json, useAAA=True)

DoubleMuon = [
    #DoubleMuon_Run2016B_25Oct2019_ver1,
    DoubleMuon_Run2016B_25Oct2019_ver2,
    DoubleMuon_Run2016C_25Oct2019,
    DoubleMuon_Run2016D_25Oct2019,
    DoubleMuon_Run2016E_25Oct2019,
    DoubleMuon_Run2016F_25Oct2019,
    DoubleMuon_Run2016G_25Oct2019,
    DoubleMuon_Run2016H_25Oct2019,
]

MuonEG = [
    #MuonEG_Run2016B_25Oct2019_ver1,
    MuonEG_Run2016B_25Oct2019_ver2,
    MuonEG_Run2016C_25Oct2019,
    MuonEG_Run2016D_25Oct2019,
    MuonEG_Run2016E_25Oct2019,
    MuonEG_Run2016F_25Oct2019,
    MuonEG_Run2016G_25Oct2019,
    MuonEG_Run2016H_25Oct2019,
]

DoubleEG = [
    #DoubleEG_Run2016B_25Oct2019_ver1,
    DoubleEG_Run2016B_25Oct2019_ver2,
    DoubleEG_Run2016C_25Oct2019,
    DoubleEG_Run2016D_25Oct2019,
    DoubleEG_Run2016E_25Oct2019,
    DoubleEG_Run2016F_25Oct2019,
    DoubleEG_Run2016G_25Oct2019,
    DoubleEG_Run2016H_25Oct2019,
]

SingleMuon = [
    #SingleMuon_Run2016B_25Oct2019_ver1,
    SingleMuon_Run2016B_25Oct2019_ver2,
    SingleMuon_Run2016C_25Oct2019,
    SingleMuon_Run2016D_25Oct2019,
    SingleMuon_Run2016E_25Oct2019,
    SingleMuon_Run2016F_25Oct2019,
    SingleMuon_Run2016G_25Oct2019,
    SingleMuon_Run2016H_25Oct2019,
]

SingleElectron = [
    #SingleElectron_Run2016B_25Oct2019_ver1,
    SingleElectron_Run2016B_25Oct2019_ver2,
    SingleElectron_Run2016C_25Oct2019,
    SingleElectron_Run2016D_25Oct2019,
    SingleElectron_Run2016E_25Oct2019,
    SingleElectron_Run2016F_25Oct2019,
    SingleElectron_Run2016G_25Oct2019,
    SingleElectron_Run2016H_25Oct2019,
]



dataSamples_Runs =  DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron

### ---------------------------------------------------------------------

dataSamples = dataSamples_Runs 
samples = dataSamples

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, localobjs=locals())
