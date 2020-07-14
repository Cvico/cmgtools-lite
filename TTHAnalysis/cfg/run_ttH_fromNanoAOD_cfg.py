import re, os, sys
from CMGTools.RootTools.samples.configTools import printSummary, mergeExtensions, doTestN, configureSplittingFromTime, cropToLumi
from CMGTools.RootTools.samples.autoAAAconfig import autoAAA
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
def byCompName(components, regexps):
    return [ c for c in components if any(re.match(r, c.name) for r in regexps) ]

year = int(getHeppyOption("year", "2018"))
analysis = getHeppyOption("analysis", "main")
preprocessor = getHeppyOption("nanoPreProcessor")

# Samples

if preprocessor:
    if year == 2018:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIAutumn18MiniAOD import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2018_MiniAOD import samples as allData
    elif year == 2017:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import dataSamples_31Mar2018 as allData
    elif year == 2016:
        from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv3 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import dataSamples_17Jul2018 as allDatas
else:
    if year == 2018:
        from CMGTools.RootTools.samples.samples_13TeV_2018_TopNanoAODv6 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2018_NanoAOD import dataSamples_25Oct2019 as allData
    elif year == 2017:
        from CMGTools.RootTools.samples.samples_13TeV_2017_TopNanoAODv6 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2017_NanoAOD import dataSamples_25Oct2019 as allData
    elif year == 2016:
        from CMGTools.RootTools.samples.samples_13TeV_2016_TopNanoAODv6 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2016_TopNanoAOD import samples as allData
#allData=[]
autoAAA(mcSamples_+allData, quiet=not(getHeppyOption("verboseAAA",False)), redirectorAAA="xrootd-cms.infn.it",node='T2_ES_IFCA') # must be done before mergeExtensions
mcSamples_, _ = mergeExtensions(mcSamples_)

# Triggers
# if year == 2018:
#     from CMGTools.RootTools.samples.triggers_13TeV_DATA2018 import all_triggers as triggers
# elif year == 2017:
#     from CMGTools.RootTools.samples.triggers_13TeV_DATA2017 import all_triggers as triggers
#     triggers["FR_1mu_iso"] = [] # they probably existed but we didn't use them in 2017
# elif year == 2016:
#     from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import all_triggers as triggers
#     triggers["FR_1mu_noiso_smpd"] = [] 

from CMGTools.TTHAnalysis.tools.nanoAOD.ttW_modules import triggerGroups_dict
print(analysis)
DatasetsAndTriggers = []
if analysis == "main":
    mcSamples = byCompName(mcSamples_, ["%s(|_PS)$"%dset for dset in [
        # single boson
        "WJetsToLNu_LO_ext","WJetsToLNu_LO", "DYJetsToLL_M10to50_LO", "DYJetsToLL_M50",
        # ttbar + single top + tW
        'TT_pow','TTLep_pow','TTSemi_pow','TTHad_pow'
        #"TTJets_SingleLeptonFromT", "TTJets_SingleLeptonFromTbar", "TTJets_DiLepton",
        "T_sch_lep", "T_tch", "TBar_tch", "T_tWch_noFullyHad", "TBar_tWch_noFullyHad",
        # conversions
        "TTGJets", "TGJets_lep", "WGToLNuG", "ZGTo2LG","WGToLNuG_01J",'TTGJets_ext'
        # ttV
        "TTWToLNu_fxfx", "TTZToLLNuNu_amc", "TTZToLLNuNu_m1to10",'TTWToLNu', 'TTZToLLNuNu',
        # ttH + tHq/tHW
        "TTHnobb_pow", "THQ", "THW", "TTH_ctcvcp",'TTH_pow',
        # top + V rare processes
        "TZQToLL", "tWll", "TTTT", "TTWW",'tZq_ll_1','tZq_ll_2','TTWW_LO'
        # diboson + DPS + WWss
        "WWTo2L2Nu", "WZTo3LNu_pow", "WZTo3LNu_fxfx", "ZZTo4L", "WW_DPS", "WWTo2L2Nu_DPS", "WpWpJJ",'TTTT_P8M2T4'
        # triboson
        "WWW", "WWW_ll", "WWZ", "WZG", "WZZ", "ZZZ",
        # other Higgs processes
        "GGHZZ4L", "VHToNonbb", "VHToNonbb_ll", "ZHTobb_ll", "ZHToTauTau", "TTWH", "TTZH",
    ]])
    DatasetsAndTriggers.append( ("DoubleMuon", triggerGroups_dict["Trigger_2m"][year] + triggerGroups_dict["Trigger_3m"][year]) )
    DatasetsAndTriggers.append( ("EGamma",     triggerGroups_dict["Trigger_2e"][year] + triggerGroups_dict["Trigger_3e"][year] + triggerGroups_dict["Trigger_1e"][year]) if year == 2018 else
                                ("DoubleEG",   triggerGroups_dict["Trigger_2e"][year] + triggerGroups_dict["Trigger_3e"][year]) )
    DatasetsAndTriggers.append( ("MuonEG",     triggerGroups_dict["Trigger_em"][year] + triggerGroups_dict["Trigger_mee"][year] + triggerGroups_dict["Trigger_mme"][year]) )
    DatasetsAndTriggers.append( ("SingleMuon", triggerGroups_dict["Trigger_1m"][year]) )
    DatasetsAndTriggers.append( ("SingleElectron", triggerGroups_dict["Trigger_1e"][year]) if year != 2018 else (None,None) )
elif analysis == "frqcd":
    mcSamples = byCompName(mcSamples_, [
        "QCD_Mu15", "QCD_Pt(20|30|50|80|120|170)to.*_Mu5", 
        "QCD_Pt(20|30|50|80|120|170)to.*_EMEn.*", 
      (r"QCD_Pt(20|30|50|80|120|170)to\d+$"       if year == 2018 else  
        "QCD_Pt(20|30|50|80|120|170)to.*_bcToE.*" ),        
        "WJetsToLNu_LO", "DYJetsToLL_M50_LO", "DYJetsToLL_M10to50_LO", "TT(Lep|Semi)_pow"
    ])
    egfrpd = {2016:"DoubleEG", 2017:"SingleElectron", 2018:"EGamma"}[year]
    DatasetsAndTriggers.append( ("DoubleMuon", triggers["FR_1mu_noiso"] + triggers["FR_1mu_iso"]) )
    DatasetsAndTriggers.append( (egfrpd,       triggers["FR_1e_noiso"] + triggers["FR_1e_iso"]) )
    DatasetsAndTriggers.append( ("SingleMuon", triggers["FR_1mu_noiso_smpd"]) )

# make MC
mcTriggers = sum((trigs for (pd,trigs) in DatasetsAndTriggers if trigs), [])
if getHeppyOption('applyTriggersInMC'):
    for comp in mcSamples:
        comp.triggers = mcTriggers

# make data
#print(DatasetsAndTriggers)
dataSamples = []; vetoTriggers = []
for pd, trigs in DatasetsAndTriggers:
    if not trigs: continue
    #print([pd])
    for comp in byCompName(allData, [pd+'.*']):
        #print(comp)
        comp.triggers = trigs[:]
        comp.vetoTriggers = vetoTriggers[:]
        dataSamples.append(comp)
    vetoTriggers += trigs[:]

selectedComponents = mcSamples + dataSamples
if getHeppyOption('selectComponents'):
    if getHeppyOption('selectComponents')=='MC':
        selectedComponents = mcSamples
    elif getHeppyOption('selectComponents')=='DATA':
        selectedComponents = dataSamples
    else:
        selectedComponents = byCompName(selectedComponents, getHeppyOption('selectComponents').split(","))
autoAAA(selectedComponents, quiet=not(getHeppyOption("verboseAAA",False)), redirectorAAA="xrootd-cms.infn.it")
if year==2018:
    configureSplittingFromTime(byCompName(mcSamples,['^(?!(TTJets_Single|T_|TBar_)).*']),150 if preprocessor else 10,12)
    configureSplittingFromTime(byCompName(mcSamples,['^(TTJets_Single|T_|TBar_).*']),70 if preprocessor else 10,12)
    configureSplittingFromTime(dataSamples,50 if preprocessor else 5,12)
else: # rerunning deepFlavor can take up to twice the time, some samples take up to 400 ms per event
    configureSplittingFromTime(byCompName(mcSamples,['^(?!(TTJets_Single|T_|TBar_)).*']),300 if preprocessor else 10,12)
    configureSplittingFromTime(byCompName(mcSamples,['^(TTJets_Single|T_|TBar_).*']),150 if preprocessor else 10,12)
    configureSplittingFromTime(dataSamples,100 if preprocessor else 5,12)
    configureSplittingFromTime(byCompName(dataSamples,['Single']),50 if preprocessor else 5,12)
selectedComponents, _ = mergeExtensions(selectedComponents)

# create and set preprocessor if requested
if preprocessor:
    from CMGTools.Production.nanoAODPreprocessor import nanoAODPreprocessor
    preproc_cfg = {2016: ("mc94X2016","data94X2016"),
                   2017: ("mc94Xv2","data94Xv2"),
                   2018: ("mc102X","data102X_ABC","data102X_D")}
    preproc_cmsswArea = "/afs/cern.ch/user/p/peruzzi/work/cmgtools_tth/CMSSW_10_2_16_UL"
    preproc_mc = nanoAODPreprocessor(cfg='%s/src/PhysicsTools/NanoAOD/test/%s_NANO.py'%(preproc_cmsswArea,preproc_cfg[year][0]),cmsswArea=preproc_cmsswArea,keepOutput=True)
    if year==2018:
        preproc_data_ABC = nanoAODPreprocessor(cfg='%s/src/PhysicsTools/NanoAOD/test/%s_NANO.py'%(preproc_cmsswArea,preproc_cfg[year][1]),cmsswArea=preproc_cmsswArea,keepOutput=True,injectTriggerFilter=True,injectJSON=True)
        preproc_data_D = nanoAODPreprocessor(cfg='%s/src/PhysicsTools/NanoAOD/test/%s_NANO.py'%(preproc_cmsswArea,preproc_cfg[year][2]),cmsswArea=preproc_cmsswArea,keepOutput=True,injectTriggerFilter=True,injectJSON=True)
        for comp in selectedComponents:
            if comp.isData:
                comp.preprocessor = preproc_data_D if '2018D' in comp.name else preproc_data_ABC
            else:
                comp.preprocessor = preproc_mc
    else:
        preproc_data = nanoAODPreprocessor(cfg='%s/src/PhysicsTools/NanoAOD/test/%s_NANO.py'%(preproc_cmsswArea,preproc_cfg[year][1]),cmsswArea=preproc_cmsswArea,keepOutput=True,injectTriggerFilter=True,injectJSON=True)
        for comp in selectedComponents:
            comp.preprocessor = preproc_data if comp.isData else preproc_mc
    if year==2017:
        preproc_mcv1 = nanoAODPreprocessor(cfg='%s/src/PhysicsTools/NanoAOD/test/%s_NANO.py'%(preproc_cmsswArea,"mc94Xv1"),cmsswArea=preproc_cmsswArea,keepOutput=True)
        for comp in selectedComponents:
            if comp.isMC and "Fall17MiniAODv2" not in comp.dataset:
                print "Warning: %s is MiniAOD v1, dataset %s" % (comp.name, comp.dataset)
                comp.preprocessor = preproc_mcv1
    if getHeppyOption("fast"):
        for comp in selectedComponents:
            comp.preprocessor = comp.preprocessor.clone(cfgHasFilter = True, inlineCustomize = ("""
process.selectEl = cms.EDFilter("PATElectronRefSelector",
    src = cms.InputTag("slimmedElectrons"),
    cut = cms.string("pt > 4.5 && miniPFIsolation.chargedHadronIso < 0.45*pt && abs(dB('PV3D')) < 8*edB('PV3D')"),
    filter = cms.bool(False),
)
process.selectMu = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("pt > 3 && miniPFIsolation.chargedHadronIso < 0.45*pt && abs(dB('PV3D')) < 8*edB('PV3D')"),
    filter = cms.bool(False),
)
process.skimNLeps = cms.EDFilter("PATLeptonCountFilter",
    electronSource = cms.InputTag("selectEl"),
    muonSource = cms.InputTag("selectMu"),
    tauSource = cms.InputTag(""),
    countElectrons = cms.bool(True),
    countMuons = cms.bool(True),
    countTaus = cms.bool(False),
    minNumber = cms.uint32(2),
    maxNumber = cms.uint32(999),
)
process.nanoAOD_step.insert(0, cms.Sequence(process.selectEl + process.selectMu + process.skimNLeps))
"""))
    if analysis == "frqcd":
        for comp in selectedComponents:
            comp.preprocessor = comp.preprocessor.clone(keepOutput = False, injectTriggerFilter = True, injectJSON = True)
            if 'Mu' in comp.dataset:
                comp.preprocessor = comp.preprocessor.clone(cfgHasFilter = True, inlineCustomize = """
process.skim1Mu = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("pt > %g && miniPFIsolation.chargedHadronIso < 0.45*pt && abs(dB('PV3D')) < 8*edB('PV3D')"),
    filter = cms.bool(True),
)
process.nanoAOD_step.insert(0, process.skim1Mu)
""" % (7.5 if "DoubleMuon" in comp.dataset else 4.5))
            elif 'QCD_Pt' in comp.dataset or "EGamma" in comp.dataset or "SingleElectron" in comp.dataset or "DoubleEG" in comp.dataset:
                comp.preprocessor = comp.preprocessor.clone(cfgHasFilter = True, inlineCustomize = """
process.skim1El = cms.EDFilter("PATElectronRefSelector",
    src = cms.InputTag("slimmedElectrons"),
    cut = cms.string("pt > 6 && miniPFIsolation.chargedHadronIso < 0.45*pt && abs(dB('PV3D')) < 8*edB('PV3D')"),
    filter = cms.bool(True),
)
process.nanoAOD_step.insert(0, process.skim1El)
""")

if analysis == "main":
    cropToLumi(byCompName(selectedComponents,["^(?!.*(TTH|TTW|TTZ)).*"]),1000.)
    cropToLumi(byCompName(selectedComponents,["T_","TBar_"]),100.)
    cropToLumi(byCompName(selectedComponents,["DYJetsToLL"]),2.)
if analysis == "frqcd":
    cropToLumi(selectedComponents, 1.0)
    cropToLumi(byCompName(selectedComponents,["QCD"]), 0.3)
    cropToLumi(byCompName(selectedComponents,["QCD_Pt\d+to\d+$"]), 0.1)
    configureSplittingFromTime(selectedComponents, 20, 3, maxFiles=8)
    configureSplittingFromTime(byCompName(selectedComponents, ["EGamma","Single.*Run2017.*","SingleMuon_Run2018.*"]), 10, 4, maxFiles=12) 
    configureSplittingFromTime(byCompName(selectedComponents, ["WJ","TT","DY","QCD_Mu15"]), 60, 3, maxFiles=6) 
    configureSplittingFromTime(byCompName(selectedComponents, [r"QCD_Pt\d+to\d+$","QCD.*EME"]), 60, 3, maxFiles=6) 


# print summary of components to process
if getHeppyOption("justSummary"): 
    printSummary(selectedComponents)
    sys.exit(0)

from CMGTools.TTHAnalysis.tools.nanoAOD.ttW_modules import *

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

# in the cut string, keep only the main cuts to have it simpler
modules = ttH_sequence_step1
cut = ttH_skim_cut
compression = "ZLIB:3" #"LZ4:4" #"LZMA:9"
branchsel_in = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/python/tools/nanoAOD/branchsel_in.txt"
branchsel_out = None

if analysis == "frqcd":
    modules = ttH_sequence_step1_FR
    cut = ttH_skim_cut_FR
    compression = "LZMA:9"
    branchsel_out = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/python/plotter/ttH-multilepton/qcd1l-skim-ec.txt"

POSTPROCESSOR = PostProcessor(None, [], modules = modules,
        cut = cut, prefetch = True, longTermCache = False,
        branchsel = branchsel_in, outputbranchsel = branchsel_out, compression = compression)

test = getHeppyOption("test")
if test == "94X-MC":
    TTLep_pow = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
    TTLep_pow.files = ["/afs/cern.ch/user/g/gpetrucc/cmg/NanoAOD_94X_TTLep.root"]
    lepSkim.requireSameSignPair = False
    lepSkim.minJets = 0
    lepSkim.minMET = 0
    lepSkim.prescaleFactor = 0
    selectedComponents = [TTLep_pow]
elif test=="ttW_sync":
    #TTJets_dilep= kreator.makeMCComponent("TTJets_dilep", "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
    TTWToLNu_fxfx     = kreator.makeMCComponent("TTWToLNu_fxfx", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", "CMS", ".*root", 0.2043, fracNegWeights=0.227)
    #TTJets_dilep.files = ["/pool/phedex/userstorage/clara/00D134FC-FBE9-E811-AF6C-1C6A7A26C53B.root"]
    TTWToLNu_fxfx.files =["/pool/phedex/userstorage/clara/sync_ttW/Top_nano/ttW/5AB18CAE-06D2-E811-B286-EC0D9A8221FE.root"]
    from CMGTools.Production.nanoAODPreprocessor import nanoAODPreprocessor
    #TTJets_dilep.preprocessor = nanoAODPreprocessor(cfg="/nfs/fanae/user/clara/ttW/CMSSW_10_2_22/src/NANO_NANO.py",cmsswArea = "/mnt_pool/ciencias_users/user/clara/ttW/CMSSW_10_2_22",keepOutput=True)
    #TTJets_dilep.preprocessor = nanoAODPreprocessor(cfg="/nfs/fanae/user/clara/CMSSW_10_2_18/src/PhysicsTools/NanoAOD/test/topNano_v6p1_2016_cfg.py",cmsswArea = "/nfs/fanae/user/clara/CMSSW_10_2_18/src/",keepOutput=True)
    TTWToLNu_fxfx.preprocessor = nanoAODPreprocessor(cfg="/nfs/fanae/user/clara/CMSSW_10_2_18/src/PhysicsTools/NanoAOD/test/topNano_v6p1_2016_cfg.py",cmsswArea = "/nfs/fanae/user/clara/CMSSW_10_2_18/src/",keepOutput=True)
    POSTPROCESSOR.modules.remove(lepSkim)
    POSTPROCESSOR.cut='1'
    selectedComponents = [TTWToLNu_fxfx]
elif test=="ttj_sync":
    TTJets_dilep= kreator.makeMCComponent("TTJets_dilep", "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
    TTJets_dilep.files = ["/pool/phedex/userstorage/clara/1A77724A-73EA-E811-A80E-0CC47A6C06C2.root"]
    from CMGTools.Production.nanoAODPreprocessor import nanoAODPreprocessor
    #TTJets_dilep.preprocessor = nanoAODPreprocessor(cfg="/nfs/fanae/user/clara/ttW/CMSSW_10_2_22/src/NANO_NANO.py",cmsswArea = "/mnt_pool/ciencias_users/user/clara/ttW/CMSSW_10_2_22",keepOutput=True)
    TTJets_dilep.preprocessor = nanoAODPreprocessor(cfg="/nfs/fanae/user/clara/CMSSW_10_2_18/src/PhysicsTools/NanoAOD/test/topNano_v6p1_2016_cfg.py",cmsswArea = "/nfs/fanae/user/clara/CMSSW_10_2_18/src/",keepOutput=True)
    POSTPROCESSOR.modules.remove(lepSkim)
    POSTPROCESSOR.cut='1'
    selectedComponents = [TTJets_dilep]
elif test=="ttW_post":
    TTWToLNu_fxfx     = kreator.makeMCComponent("TTWToLNu_fxfx", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", "CMS", ".*root", 0.2043, fracNegWeights=0.227)
    TTWToLNu_fxfx.files =["/nfs/fanae/user/clara/ttW/CMSSW_10_4_0/src/CMGTools/TTHAnalysis/cfg/ttW_newloose_2/TTWToLNu_fxfx_Chunk0/cmsswPreProcessing.root"]
    POSTPROCESSOR.modules.remove(lepSkim)
    POSTPROCESSOR.cut='1'
    selectedComponents = [TTWToLNu_fxfx]
elif test == "94X-MC-miniAOD":
    TTLep_pow = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
    TTLep_pow.files = [ 'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/TTTo2L2Nu_mtop166p5_TuneCP5_PSweights_13TeV-powheg-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/70000/3CC234EB-44E0-E711-904F-FA163E0DF774.root' ]
    localfile = os.path.expandvars("/tmp/$USER/%s" % os.path.basename(TTLep_pow.files[0]))
    if os.path.exists(localfile): TTLep_pow.files = [ localfile ] 
    from CMGTools.Production.nanoAODPreprocessor import nanoAODPreprocessor
    TTLep_pow.preprocessor = nanoAODPreprocessor("/afs/cern.ch/work/g/gpetrucc/ttH/CMSSW_10_4_0/src/nanov4_NANO_cfg.py")
    selectedComponents = [TTLep_pow]
elif test == "102X-MC":
    TTLep_pow = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2), useAAA=True )
    TTLep_pow.files = TTLep_pow.files[:1]
    selectedComponents = [TTLep_pow]

elif test == "94X-data":
    json = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
    SingleElectron_Run2017C_14Dec2018 = kreator.makeDataComponent("SingleElectron_Run2017C_14Dec2018", "/SingleElectron/Run2017C-Nano14Dec2018-v1/NANOAOD", "CMS", ".*root", json)
    SingleElectron_Run2017C_14Dec2018.files = ["0450ACEF-E1E5-1345-8660-28CF5ABE26BE.root"]
    SingleElectron_Run2017C_14Dec2018.triggers = triggerGroups_dict["Trigger_1e"][year]
    SingleElectron_Run2017C_14Dec2018.vetoTriggers = triggerGroups_dict["Trigger_2m"][year] + triggerGroups_dict["Trigger_3m"][year]+triggerGroups_dict["Trigger_2e"][year] + triggerGroups_dict["Trigger_3e"][year]+triggerGroups_dict["Trigger_em"][year] + triggerGroups_dict["Trigger_mee"][year] + triggerGroups_dict["Trigger_mme"][year]+triggerGroups_dict["Trigger_1m"][year]
    
    selectedComponents = [SingleElectron_Run2017C_14Dec2018]
elif test in ('2','3','3s'):
    doTestN(test, selectedComponents)

