# -*- coding: utf-8 -*-
# Filename: tiff.py
""" Module for the basic functions to work with TIFF data files.
"""
import h5py
import os
import numpy as np
from scipy import misc
import PIL.Image as Image

def TIFF2HDF5(inputFile,
              inputStart,
              inputEnd,
              digits=3,
              zeros=True,
              dtype='uint16',
              outputFile='myfile.h5',
              whiteFile=None,
              whiteStart=None,
              whiteEnd=None,
              darkFile=None,
              darkStart=None,
              darkEnd=None):
    """ Converts a stack of projection 16-bit TIFF files
    in a folder to a single HDF5 file. The dataset is
    constructed using the projection data, white field
    and dark field images.

    Parameters
    ----------
    inputFile : str
        Name of the generic input file name
        for all the TIFF files to be assembled.

    inputStart, inputEnd : scalar
        Determines the portion of the TIFF images
        to be used for assembling the HDF file.

    digits : scalar, optional
        Number of digits used for file indexing.
        For example if 4: test_XXXX.tiff

    zeros : bool, optional
        If ``True`` assumes all indexing uses four digits
        (0001, 0002, ..., 9999). If ``False`` omits zeros in
        indexing (1, 2, ..., 9999)

    dtype : str, optional
        Corresponding Numpy data type of the TIFF file.

    outputFile : str
        Name of the output HDF file.

    whiteFile : str, optional
        Name of the generic input file name
        for all the white field
        TIFF files to be assembled.

    whiteStart, whiteEnd : scalar, optional
        Determines the portion of the white
        field TIFF images to be used for
        assembling HDF file.

    darkFile : str, optional
        Name of the generic input file name
        for all the white field
        TIFF files to be assembled.

    darkStart, darkEnd : scalar, optional
        Determines the portion of the dark
        field TIFF images to be used for
        assembling HDF file.
    """
    # Create new folders.
    #dirPath = os.path.dirname(outputFile)
    #if not os.path.exists(dirPath):
    #    os.makedirs(outputFile)

    # Read projection TIFF files in the given folder.
    inputData = readTIFFStack(inputFile,
                              inputStart,
                              inputEnd,
                              dtype=dtype,
                              digits=digits,
                              zeros=zeros)

    # Read white-field TIFF files in the given folder.
    whiteData = readTIFFStack(whiteFile,
                              whiteStart,
                              whiteEnd,
                              dtype=dtype,
                              digits=digits,
                              zeros=zeros)

    # Read dark-field TIFF files in the given folder.
    darkData = readTIFFStack(darkFile,
                             darkStart,
                             darkEnd,
                             dtype=dtype,
                             digits=digits,
                             zeros=zeros)

    # Write HDF5 file.
    print 'Assembling HDF5 file: ' + os.path.realpath(outputFile)
    f = h5py.File(outputFile, 'w')
    f.create_dataset('implements', data='exchange')
    exchangeGrp = f.create_group("exchange")
    exchangeGrp.create_dataset('data', data=inputData, dtype=dtype)
    exchangeGrp.create_dataset('data_white', data=whiteData, dtype=dtype)
    exchangeGrp.create_dataset('data_dark', data=darkData, dtype=dtype)
    f.close()


def readTIFF(inputFile, dtype='uint16'):
    """Read TIFF files.

    Parameters
    ----------
    inputFile : str
        Name of the input TIFF file.

    dtype : str, optional
        Corresponding Numpy data type of the TIFF file.

    .. See also:: http://docs.scipy.org/doc/numpy/user/basics.types.html
    """
    im = Image.open(inputFile)
    print list(im.size)
    out = np.fromstring(im.tostring(), dtype).reshape(tuple(list(im.size)))
    return out


def readTIFFStack(inputFile,
                  inputStart,
                  inputEnd,
                  digits=4,
                  zeros=True,
                  dtype='uint16'):
    """Read a stack of TIFF files in a folder.

    Parameters
    ----------
    inputFile : str
        Name of the input TIFF file.

    inputStart, inputEnd : scalar
        Determines the portion of the TIFF images
        to be used for assembling the HDF file.

    digits : scalar, optional
        Number of digits used for file indexing.
        For example if 4: test_XXXX.tiff

    zeros : bool, optional
        If ``True`` assumes all indexing uses four digits
        (0001, 0002, ..., 9999). If ``False`` omits zeros in
        indexing (1, 2, ..., 9999)

    dtype : str, optional
        Corresponding Numpy data type of the TIFF file.

    .. See also:: http://docs.scipy.org/doc/numpy/user/basics.types.html
    """
    if inputFile.endswith('tif') or \
       inputFile.endswith('tiff'):
        dataFile = inputFile.split('.')[-2]
        dataExtension = inputFile.split('.')[-1]

    fileIndex = ["" for x in range(digits)]
    for m in range(digits):
        if zeros is True:
           fileIndex[m] = '0' * (digits - m)
        elif zeros is False:
           fileIndex[m] = ''

    ind = range(inputStart, inputEnd)
    for m in range(len(ind)):
        if ind[m] < 10 :
            fileName = dataFile + fileIndex[0] + str(ind[m]) + '.' + dataExtension
        elif ind[m] < 100 :
            fileName = dataFile + fileIndex[1] + str(ind[m]) + '.' + dataExtension
        elif ind[m] < 1000 :
            fileName = dataFile + fileIndex[2] + str(ind[m]) + '.' + dataExtension
        elif ind[m] < 10000 :
            fileName = dataFile + str(ind[m]) + '.' + dataExtension           
            
        if os.path.isfile(fileName):
            print 'Reading file: ' + os.path.realpath(fileName)
            tmpdata = readTIFF(fileName, dtype = dtype)
            if m == 0: # Get resolution once.
                inputData = np.empty((inputEnd-inputStart,
                                      tmpdata.shape[0],
                                      tmpdata.shape[1]),
                                     dtype='uint16')
            inputData[m, :, :] = tmpdata

    return inputData

def write(dataset,
          outputFile='./data/recon.tiff',
          slicesStart=None,
          slicesEnd=None):
    """ Write reconstructed data to a stack
    of 2-D 32-bit TIFF images.

    Parameters
    -----------
    dataset : ndarray
        Reconstructed values.

    outputFile : str, optional
        Generic name for all TIFF images. Index will
        be added to the end of the name.

    slicesStart : scalar, optional
        First index of the data on first dimension
        of the array.

    slicesEnd : scalar, optional
        Last index of the data on first dimension
        of the array.
    """
    # Create new folders.
    dirPath = os.path.dirname(outputFile)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    # Remove TIFF extension.
    if outputFile.endswith('tiff'):
        outputFile = outputFile.split(".")[-2]

    # Select desired slices from whole data.
    numX, numY, numZ = dataset.shape
    if slicesStart is None:
        slicesStart = 0
    if slicesEnd is None:
        slicesEnd = numX

    # Write data.
    ind = range(slicesStart, slicesEnd)
    for m in range(len(ind)):
        if ind[m] < 10:
            fileName = outputFile + '000' + str(ind[m]) + '.tiff'
        elif ind[m] < 100:
            fileName =  outputFile + '00' + str(ind[m]) + '.tiff'
        elif ind[m] < 1000:
            fileName = outputFile + '0' + str(ind[m]) + '.tiff'
        elif ind[m] < 10000:
            fileName = outputFile + '' + str(ind[m]) + '.tiff'
        img = misc.toimage(dataset[m, :, :])
        #img = misc.toimage(dataset[m, :, :], mode='F')
        img.save(fileName)