# -*- coding: utf-8 -*-
import tomopy
import os

def hd5_to_recon(dirName='.', inputFileName='out.h5', startSlice=None, endSlice=None, outDir='.'):

inputFilePath = os.path.join(dirName, inputFileName)

# Read HDF5 file.
data, white, dark, theta = tomopy.xtomo_reader(inputFilePath,
                                               slices_start=startSlice,
                                               slices_end=endSlice)

# Xtomo object creation and pipeline of methods.  
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
d.normalize()
d.correct_drift()
d.phase_retrieval()
d.correct_drift()
# d.center=661.5
d.gridrec()


# Write to stack of TIFFs.
tomopy.xtomo_writer(d.data_recon, outDir, axis=0)

