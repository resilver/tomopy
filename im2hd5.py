import h5py
import os
import numpy as np
from scipy import misc
import re
import PIL.Image as Image
import datetime
import shutil
import getopt
import sys
import pdb

def im2hd5(inputDir = '.', imageExt='tif', scanStartRow=0, scanEndRow=None, dataBase=None, whiteBase=None, darkBase=None, dataStart=0, dataEnd=None,  whiteStart=None, whiteEnd=None, darkStart=None, darkEnd=None, dataClass = 'uint16', outputDir='.', outputFileName = 'out.h5', numDig=5):
       
    # Create the output directory if it doesn't already exist.
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
       
    # Figure out the output file path
    outputFilePath = os.path.join(outputDir, outputFileName)  
    
    #handling imeageExt
    imageExt = imageExt.lower()
    if imageExt[0] is '.':
        imageExt = imageExt[1:len(imageExt)]
    if imageExt not in ['tif', 'gif', 'jpeg', 'jpg']:
        print "Error - not a supported image type"
        return
       
    # Inform the user of where the output file is going to be written
    print 'Assembling HDF5 file: ' + os.path.realpath(outputFilePath)
    
    # Move the existing file to a temp folder.
    if os.path.isfile(outputFilePath):
        # Figure out what time it is, for naming the archived file
        dateNum = datetime.datetime.now();
        # Make an archive file path
        archivePath = os.path.join(outputDir, "archive_" + dateNum.strftime("%d-%b-%Y_%H-%M-%S_") + outputFileName);
        # Rename the existing file with the time-stamped archive file name.
        shutil.move(outputFilePath, archivePath)
    
    # This creates the output hdf5 file. The 'w' means 'truncate the file if it already exists'
    h5File = h5py.File(outputFilePath, 'w');
    
    # This creates a dataset within the hdf5 file.
    h5File.create_dataset('implements', data='exchange');
    
    # This creates a group called "exchange" within the hdf5 file.
    exchangeGrp = h5File.create_group("exchange");     
    
    # This determines the file names of the projection images.
    projectionData = readImageStack(inputDir, imageExt, dataStart, dataEnd, dataClass=dataClass, scanStartRow=scanStartRow, scanEndRow=scanEndRow, baseName=dataBase, numDig=numDig);
    # This creates a dataset called "data" within the group "exchange".
    # This dataset holds the raw projection images.
    group_data = exchangeGrp.create_dataset('data', data=projectionData, dtype=dataClass);
    
    # This determines the file names of the whitefield images.
    if whiteStart != None:
        whiteData = readImageStack(inputDir, imageExt, whiteStart, whiteEnd, dataClass=dataClass, scanStartRow=scanStartRow, scanEndRow=scanEndRow, baseName=whiteBase, numDig=numDig);
        # This creates a dataset called "data_white" within the group "exchange".
        # This dataset holds the raw whitefield images.
        exchangeGrp.create_dataset('data_white', data=whiteData, dtype=dataClass);
        
    # This determines the file names of the darkfield images.
    if darkStart != None:
        darkData = readImageStack(inputDir, imageExt, darkStart, darkEnd, dataClass=dataClass, scanStartRow=scanStartRow, scanEndRow=scanEndRow, baseName=darkBase, numDig=numDig); 
        # This creates a dataset called "data_dark" within the group "exchange".
        # This dataset holds the raw darkfield images.
        exchangeGrp.create_dataset('data_dark', data=darkData, dtype=dataClass);
    
    # This closes the hdf5 file.
    h5File.close();

def readImageStack(dirName='.', imageExt='tif', dataStart=0, dataEnd=None, scanStartRow=0, scanEndRow=None, dataClass='uint16', baseName=None, numDig=5):
    # This function reads a series of images and returns a 3-D array that contains all the images in the series.
    # readImageStack searches the directory named dirName for files that end in the extension imageExt. 
    # Then it returns the first dataEnd - dataStart images.
    
    # Make sure dataStart has a value
    if dataStart == None:
        dataStart = 0
    
    # This gets a list of the images to read
    fileList = listImageFiles(dirName, imageExt, dataStart, dataEnd, baseName=baseName, numDig=numDig);
    
    # Determine the number of images
    nImages = len(fileList)

    # This makes a list of images numbers.
    if dataEnd != None:
        lastImage = dataEnd
        #else:lastImage = len(fileList)
        imageNumbers = range(dataStart, lastImage + 1);
    else:
        imageNumbers = range(dataStart, nImages)
 
    # Load in the first image to determine its dimensions, class, etc
    imageSize = Image.open(os.path.join(dirName, fileList[0])).size;
    
    # Read the height and width of the image
    imageHeight = imageSize[1];
    imageWidth = imageSize[0];
         
    # This determines the last row that will be extracted from each image.
    if scanEndRow:
        endRow = scanEndRow
    else:
        endRow = imageHeight;
    
    # This counts the number of scan rows.
    nScanRows = endRow - scanStartRow;
    
    # Initialize the array to hole the images
    imageStack = np.zeros([nImages, nScanRows, imageWidth], dataClass)
    
    # This loads each image. This seems like a bad way to do this because we have to hold the entire image stack in memory, so systems without a lot of memory could crash. 
    for k in range(nImages):
        # This determines the file path to the k'th image
        if k % 10 is 0:
            print "On image %d of %d" %(k, nImages)
        filePath = os.path.join(dirName, fileList[k])
        # This loads in the image and reshapes it to be [x, y] formatted
        # so that it fits into the image stack.
        img = np.reshape(Image.open(filePath), [imageHeight, imageWidth]);      
        # This crops the image
        imgCropped = img[scanStartRow:endRow, :]
        
        # This adds the k'th image to the image stack.
        imageStack[k, :, :] = imgCropped;
   
    # This returns the image stack.
    return imageStack
    
def listImageFiles(dirName='.', imageExt='tif', dataStart=0, dataEnd=None, baseName=None, numDig=5):
    """
    This function returns a list of all the images of extension imType in the directory dirName. The returned list contains the first dataStart:dataEnd images.
    The issue with this is that it will return other files of similar extension, which means that the raw data directory shouldn't have any other image files in it.
    
    """ 
    # This gets a list of all the files the directory named dirName
    dirContents = os.listdir(dirName)
    
    # This determines which files in fileList end with the extension imType
    fileList = [fileName for fileName in dirContents if re.search('.*\.%s' %(imageExt), fileName) is not None]
    if baseName is not None:
        fileList = [fileName for fileName in fileList if re.search('%s\d{%d}' %(baseName, numDig), fileName) is not None]
    # This returns the section of the image list between the start and end image numbers.
    #pdb.set_trace()
    if dataEnd is None:
        dataEnd = len(fileList) - 1
    if dataStart is None:
        dataStart = 0
    
    return fileList[dataStart : dataEnd + 1]

         
# These lines allow the code to be run from the command line.
if __name__ == "__main__":
    #import sys, PythonCall
    #PythonCall.PythonCall(sys.argv).execute()
    #(dirName='.', imageExt='tif', dataStart=0, dataEnd=None, scanStartRow=0, scanEndRow=None, whiteStart=None, whiteEnd=None, darkStart=None, darkEnd=None, dataClass = 'uint16', outputDir='.', outputFileName = 'out.h5'
    #arglist = ["-dir", '-imext', '-dats', '-date', '-ssr', '-ser', '-ws', '-we', '-ds', '-de', '-dtype', '-outdir', '-outfn']
    try:    
        opt, args = getopt.getopt(sys.argv[1:], [] )
    except: print "ERROR ERROR ERROR"
    
    if len(args) is 13:
            
        #pdb.set_trace()
        for i in range(len(args)):
            if args[i].isdigit():
                args[i] = int(args[i])
            if args[i] == 'None':
                args[i] = None
        print args
            
        im2hd5(*args)    

    
    