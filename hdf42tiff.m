% function hdf42tiff(JOBLIST);

outputDir = '/Users/mattgiarra/Documents/tomography/data/xray_data/2008_11_32ID-Drosophila/A01/tiff';
inputDir = '/Users/mattgiarra/Documents/tomography/data/xray_data/2008_11_32ID-Drosophila/A01/raw';

hdfDataName = '/data';

inputBase = 'A01_';
inputExt = '.hdf';
inputNumDigits = 5;
inputNumberFormat = ['%0' num2str(inputNumDigits) '.0f'];


outputBase = 'A01_';
outputExt = '.tif';
outputNumDigits = 5;
outputNumberFormat = ['%0' num2str(outputNumDigits) '.0f'];

startImage = 1;
endImage = 1444;



imageNumbers = startImage : skipImage : endImage;
nImages = length(imageNumbers);

for k = 1 : nImages
    % Specify the file names
    inputImageName = [inputBase num2str(imageNumbers(k), inputNumberFormat) inputExt];
    outputImageName = [outputBase num2str(imageNumbers(k), outputNumberFormat) outputExt];
    
    % Determine the file paths
    inputImagePath = fullfile(inputDir, inputImageName);
    outputImagePath = fullfile(outputDir, outputImageName);
    
    % Read the hdf file
    inputImage = hdfread(inputImagePath, hdfDataName);
    
    % Write the image data to a tiff file
    imwrite(inputImage, outputImagePath);
    
end





% end