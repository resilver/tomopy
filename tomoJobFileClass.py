class img2tiffJobFile(object):
        """__init__() This is a class constructor for jobfiles used for converting images to HDF5 files"""
        def __init__(self, dirName='.', imageExt='tif', scanStartRow=0, scanEndRow=None, dataBase=None, whiteBase=None, darkBase=None, dataStart=0, dataEnd=None,  whiteStart=None, whiteEnd=None, darkStart=None, darkEnd=None, dataClass = 'uint16', outputDir='.', outputFileName = 'out.h5', numDig=5):
            self.dirName = dirName
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
            
class hdf5toReconJobFile(object):
    """__init__() This is a class constructor for jobfiles used to convert HDF5 files to tomographic reconstructions"""
    def __init__(self, dirName='.', inputFileName='out.h5', startSlice=None, endSlice=None, outDir='tmp', outBase = 'recon_', center=None):
            self.dirName = dirName
            self.inputFileName = inputFileName
            self.startSlice = startSlice
            self.endSlice = endSlice
            self.outDir = outDir
            self.outBase = outBase
            self.center = center