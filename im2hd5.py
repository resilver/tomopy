import h5py
import os
import numpy as np
from scipy import misc
import re
import PIL.Image as Image

def im2hd5(dirName='.', imageExt='tif', dataStart=0, dataEnd=None, scanStartRow=None, scanEndRow=None, whiteStart=None, whiteEnd=None, darkStart=None, darkEnd=None, dataClass = 'uint16', outputFilePath='out.h5'):
    # This function converts a directory full of sequentially-numbered images into an HDF5 file.
       
    # Inform the user of where the output file is going to be written
    print 'Assembling HDF5 file: ' + os.path.realpath(outputFilePath)
    
    # This creates the output hdf5 file. The 'w' means 'truncate the file if it already exists'
    h5File = h5py.File(outputFilePath, 'w');
    
    # This creates a dataset within the hdf5 file.
    h5File.create_dataset('implements', data='exchange');
    
    # This creates a group called "exchange" within the hdf5 file.
    exchangeGrp = h5File.create_group("exchange");     
    
    # This determines the file names of the projection images.
    projectionData = readImageStack(dirName, imageExt, dataStart, dataEnd, dataClass);
    
    # This creates a dataset called "data" within the group "exchange".
    # This dataset holds the raw projection images.
    exchangeGrp.create_dataset('data', data=projectionData, dtype=dataClass);
    
    # This determines the file names of the whitefield images.
    if whiteStart:
        whiteData = readImageStack(dirName, imageExt, whiteStart, whiteEnd, dataClass);
        # This creates a dataset called "data_white" within the group "exchange".
        # This dataset holds the raw whitefield images.
        exchangeGrp.create_dataset('data_white', data=whiteData, dtype=dataClass);
    
    # This determines the file names of the darkfield images.
    if darkStart:
        darkData = readImageStack(dirName, imageExt, darkStart, darkEnd, dataClass); 
        # This creates a dataset called "data_dark" within the group "exchange".
        # This dataset holds the raw darkfield images.
        exchangeGrp.create_dataset('data_dark', data=darkData, dtype=dataClass);
    
    # This closes the hdf5 file.
    h5File.close();

def readImageStack(dirName='.', imageExt='tif', dataStart=0, dataEnd=None, dataClass='uint16'):
    # This function reads a series of images and returns a 3-D array that contains all the images in the series.
    # readImageStack searches the directory named dirName for files that end in the extension imageExt. 
    # Then it returns the first dataEnd - dataStart images.
    
    # This gets a list of the images to read
    fileList = listImageFiles(dirName, imageExt, dataStart, dataEnd);
    
    # Determine the number of images
    nImages = len(fileList)
    
    # This makes a list of images numbers.
    imageNumbers = range(dataStart, dataEnd+1);
    
    # Load in the first image to determine its dimensions, class, etc
    imageSize = Image.open(dirName + fileList[0]).size;
    
    # Initialize the array to hole the images
    imageStack = np.zeros([nImages, imageSize[1], imageSize[0]], dataClass)
    
    # This loads each image. This seems like a bad way to do this because we have to hold the entire image stack in memory, so systems without a ton of memory will crash. 
    for k in imageNumbers:
        filePath = dirName + fileList[k]
        imageStack[k, :, :] = np.reshape(Image.open(filePath), [imageSize[1], imageSize[0]])
   
    # This returns the image stack.
    return imageStack
     
def listImageFiles(dirName='.', imageExt='tif', dataStart=0, dataEnd=None):
    """
    This function returns a list of all the images of extension imType in the directory dirName. The returned list contains the first dataStart:dataEnd images.
    The issue with this is that it will return other files of similar extension, which means that the raw data directory shouldn't have any other image files in it.
    
    """
    
    # This gets a list of all the files the directory named dirName
    dirContents = os.listdir(dirName)
    
    # This determines which files in fileList end with the extension imType
    fileList = [fileName for fileName in dirContents if re.search('.*\.%s' %(imageExt), fileName)]
    
    # This returns the section of the image list between the start and end image numbers.
    return fileList[dataStart : dataEnd + 1]



    
    