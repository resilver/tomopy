# ________CONVERT TIFFS TO HDF5 ________

tiffInputDir = "/Volumes/128.173.163.248/2013_07_2BM_copy/Jeff/test_sample_Diplo_4"
hdfOutputDir="/Users/mattgiarra/Documents/tomography/data/2013_07_2BM_copy/Jeff/test_sample_Diplo_4/h5"
hdfOutputName="test_sample_Diplo_4.hd5"

dataBase = "Diplodocus_1_200mm_4_"
dataStart = 1
dataEnd = 50

whiteBase = "Diplodocus_1_200mm_4postFlat_"
whiteStart = 2
whiteEnd = None

darkBase = "Diplodocus_1_200mm_4postDark_"
darkStart = 2
darkEnd = None

# Load into ipython
%run im2hd5

# Create the HDF file.
im2hd5(dirName=tiffInputDir, dataBase=dataBase, dataStart=dataStart, dataEnd=dataEnd, whiteBase=whiteBase, whiteStart=whiteStart, whiteEnd=whiteEnd, darkBase=darkBase, darkStart=darkStart, darkEnd=darkEnd, outputDir=hdfOutputDir, outputFileName=hdfOutputName)

#__________TOMOGRAPHIC RECONSTRUCTIONS_______________

# Directory in which to find the HDF5 file.
reconstructionInputDir = "/Users/mattgiarra/Documents/tomography/data/2013_07_2BM_copy/Jeff/test_sample_Diplo_4/hdf"

reconInputFile = "test_sample_Diplo_4.hd5"

# Output directory for tomographic reconstructions
outDir = "/Users/mattgiarra/Documents/tomography/data/2013_07_2BM_copy/Jeff/test_sample_Diplo_4/recon"

# Base name for tomographic reconstructions
outBase = "Diplodocus_1_200mm_4_";

# Stard and end slice numbers
startSlice = 500;
endSlice = 510;

# Center location. If this isn't specified, the code will find the center.
center=1015.08752441

## Uncomment this to automatically find the center.
#center = None

# Load into iPython
%run hdf5_to_recon

# Do the tomographic reconstruction.
hdf5_to_recon(dirName=reconstructionInputDir, inputFileName = reconInputFile, outBase = outBase, outDir=outDir, startSlice=startSlice, endSlice=endSlice, center=center)





