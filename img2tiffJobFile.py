class img2tiffJobFile(object):
        """__init__() functions as the class constructor"""
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
            
        def __call__(self):
            print 'called'
