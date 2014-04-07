# -*- coding: utf-8 -*-
import tomopy
import os

def hdf5_to_recon(dirName='.', inputFileName='out.h5', startSlice=None, endSlice=None, outDir='tmp', outBase = 'recon_', center=None):

    # This is the path to the input HDF5 file.
    inputFilePath = os.path.join(dirName, inputFileName)

    # This is the path to the output files
    outPath = os.path.join(outDir, outBase)

    # Read HDF5 file.
    data, white, dark, theta = tomopy.xtomo_reader(inputFilePath, slices_start=startSlice, slices_end=endSlice)
    # Xtomo object creation and pipeline of methods.  
    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta)
    d.normalize()
    d.correct_drift()
    d.phase_retrieval()
    d.correct_drift()
    
    # Appliy a median filter to the (images?) to improve the chance of success of the center finder.
    d.median_filter()
    
    # Find the center of rotation
    if center == None:
        d.optimize_center()
    else:
        d.center=center
    
    # Do the tomographic reconstruction
    d.gridrec()

    # Write to stack of TIFFs.
    tomopy.xtomo_writer(d.data_recon, outPath, axis=0, x_start=startSlice)

