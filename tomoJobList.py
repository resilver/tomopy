import os
from tomoJobFileClass import img2tiffJobFile as tjf
from tomoJobFileClass import hdf5toReconJobFile as rjf

def tomoJobList():
    
    # This makes an empty list to hold the image-to-hdf5 job list.
    img2hdfJobList = [];
    
    # This makes an empty list to hold the hdf5-to-reconstruction job list.
    reconJobList = [];
    
    # Input and output data repositories: all data for this jobfile are located beneath these two directories.
    inputDataRepository = '/Volumes/128.173.163.248/2013_07_2BM_copy/Jeff'
    outputDataRepository = '/Users/mattgiarra/Documents/tomography/data/2013_07_2BM_copy/Jeff'
    
    # This is the case name.
    caseName='test_sample_Diplo_4'
    
    # Image-to-HDF parameters
    dataBase = "Diplodocus_1_200mm_4_"
    dataStart = 1
    dataEnd = None
    whiteBase = "Diplodocus_1_200mm_4postFlat_"
    whiteStart = 2
    whiteEnd = None
    darkBase = "Diplodocus_1_200mm_4postDark_"
    darkStart = 2
    darkEnd = None
    hdfOutputFileName = caseName + '.hdf5'
    imageInputDir = os.path.join(inputDataRepository, caseName)
    hdfOutputDir = os.path.join(outputDataRepository, caseName, 'hdf5')
    runImg2Hdf = True # Specify whether to run the processes.
    
    #________ HDF-to-reconstruction parameters ___________#
    reconInputDirName = hdfOutputDir
    reconInputFileName = hdfOutputFileName
    reconOutDir = os.path.join(outputDataRepository, caseName, 'recon')
    reconOutBase = caseName + '_recon_'
    # Set start and end slices to None to reconstruc the entire dataset.
    startSlice = 500
    endSlice = 550 
    rotationCenter = None # Set the rotation center to None to find it automatically.
    runHdf2Recon = True # Specify whether to run the processes.
  
    #________ Augment joblist ___________#
    # Append this job information to the image-to-HDF job file!
    img2hdfJobList.append(tjf(inputDir=imageInputDir, dataBase=dataBase, whiteBase=whiteBase, darkBase=darkBase, dataStart = dataStart, dataEnd = dataEnd, whiteStart=whiteStart, whiteEnd=whiteEnd, darkStart=darkStart, darkEnd=darkEnd, outputDir=hdfOutputDir, outputFileName = hdfOutputFileName, runJob = runImg2Hdf))
    
    # Append the job information to the HDF-to-reconstruction job file!
    reconJobList.append(rjf(inputDir=reconInputDirName, inputFileName=reconInputFileName, startSlice=startSlice, endSlice=endSlice, outputDir = reconOutDir, outBase = reconOutBase, center=rotationCenter, runJob = runHdf2Recon))
        
    # Return variables!!
    return (img2hdfJobList, reconJobList)