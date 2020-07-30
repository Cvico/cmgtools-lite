#!/usr/bin/env python
# This is a macro used to get mca-files
# from just the name of the sample

import os
import re
import sys

path = sys.argv[1]
NameInFile = sys.argv[2]
mcaName = sys.argv[3]
key = sys.argv[4]
norm = sys.argv[5]

submit = "{command}"

def GetListOfTrees(path):
    # First we get a list of the files in the given path
    files = os.listdir(path)
    return files

def GetKey(files, NameInFile):
    # Return a list with all the files containing
    # the key
    samples = [f for f in files if NameInFile in f]
    return samples
def CheckIfExists(mcaName):
    doExists = False
    if os.path.exists('./{mcaName}.txt'.format(mcaName = mcaName)): doExists = True
    return doExists

def openFile(mcaName, opt = "a"):
    mcaFile = open(mcaName, opt)
    return mcaFile

def WriteMCAfile(Samples, mcaName):
    # Write the mca file
    
    # First we check if it already exists, and if it doesn't then we create a new one
    if CheckIfExists(mcaName): mcaFile = openFile(mcaName + ".txt")
    else: mcaFile = openFile(mcaName + ".txt", "w")
    for s in Samples:
	s = s.replace(s[-5:], "")
	mcaFile.write("{key}: {s}: {norm} \n".format(key = key, s = s, norm = norm))

    return 

files = GetListOfTrees(path)
Samples = GetKey(files, NameInFile)
WriteMCAfile(Samples, mcaName)

