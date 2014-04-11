from im2hd5 import *
from hdf5_to_recon import *

class img2tiffJobFile(object):
        """__init__() This is a class constructor for jobfiles used for converting images to HDF5 files"""
        def __init__(self, inputDir='.', imageExt='tif', scanStartRow=0, scanEndRow=None, dataBase=None, whiteBase=None, darkBase=None, dataStart=0, dataEnd=None,  whiteStart=None, whiteEnd=None, darkStart=None, darkEnd=None, dataClass = 'uint16', outputDir='.', outputFileName = 'out.h5', numDig=5, runJob=True):
            self.inputDir = inputDir
            self.imageExt = imageExt
            self.scanStartRow = scanStartRow
            self.scanEndRow = scanEndRow
            self.dataBase = dataBase
            self.whiteBase = whiteBase
            self.darkBase = darkBase
            self.dataStart = dataStart
            self.dataEnd = dataEnd
            self.whiteStart = whiteStart
            self.whiteEnd = whiteEnd
            self.darkStart = darkStart
            self.darkEnd = darkEnd
            self.dataClass = dataClass
            self.outputDir = outputDir
            self.outputFileName = outputFileName
            self.numDig = numDig
            self.runJob = runJob
        
        # Run the image-to-HDF code.
        def run(self):
            if self.runJob:
                im2hd5(
                inputDir = self.inputDir,
                imageExt = self.imageExt,
                scanStartRow = self.scanStartRow,
                scanEndRow = self.scanEndRow,
                dataBase = self.dataBase,
                whiteBase = self.whiteBase,
                darkBase = self.darkBase,
                dataStart = self.dataStart,
                dataEnd = self.dataEnd,
                whiteStart = self.whiteStart,
                whiteEnd = self.whiteEnd,
                darkStart = self.darkStart,
                darkEnd = self.darkEnd,
                dataClass = self.dataClass,
                outputDir = self.outputDir,
                outputFileName = self.outputFileName,
                numDig = self.numDig
                )
            
class hdf5toReconJobFile(object):
    """__init__() This is a class constructor for jobfiles used to convert HDF5 files to tomographic reconstructions"""
    def __init__(self, inputDir = '.', inputFileName='out.h5', startSlice=None, endSlice=None, outputDir='recon', outBase = 'recon_', center=None, runJob=True):
            self.inputDir = inputDir
            self.inputFileName = inputFileName
            self.startSlice = startSlice
            self.endSlice = endSlice
            self.outputDir = outputDir
            self.outBase = outBase
            self.center = center
            self.runJob = runJob
                
    ## run tomo code        
    def run(self):
        if self.runJob:
            hdf5_to_recon(
            inputDir = self.inputDir,
            inputFileName=self.inputFileName,
            startSlice=self.startSlice,
            endSlice=self.endSlice,
            outputDir=self.outputDir,
            outBase = self.outBase,
            center=self.center
            )
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
             