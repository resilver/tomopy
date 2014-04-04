function JOBLIST = hdf2tiffJobList;
%% Some job options

% Number of processors to use
DefaultJob.JobOptions.NumberOfProcessors = 1;

% This specifies whether to convert the raw HDF4 data to tiffs.
DefaultJob.JobOptions.ConvertHDF4ToTiff = true;

% Whether or not to convert the TIF images to HDF5 after transferring.
DefaultJob.JobOptions.ConvertToHDF5 = false;

% Whether or not to call the Python reconstruction code
% after moving each dataset.
DefaultJob.JobOptions.DoReconstructions = false;

% DefaultJob.HDf4_To_Tiff;
% DefaultJob.Tiff_To_HDF5;
% DefaultJob.HDF5_to_recon;


%% Specify where to find the data
% Data repositories

% Input and ouput file extensions
DefaultJob.HDf4_To_Tiff.InputFileExtension = 'hdf';
DefaultJob.HDf4_To_Tiff.OutputFileExtension = '.tif';

DefaultJob.InputDataRepository = '/Volumes/Xray_data/Tomo_data_archive_1/2008_11_32ID-Drosophila';
DefaultJob.InputCaseName = 'A01';
DefaultJob.InputDataDir = fullfile(DefaultJob.InputCaseName, 'raw');

DefaultJob.OutputDataRepository = '/Users/mattgiarra/Documents/tomography/data/xray_data/2008_11_32ID-Drosophila/';
DefaultJob.OutputCaseName = 'A01';
DefaultJob.OutputDataDir = fullfile(DefaultJob.OutputCaseName, strrep(DefaultJob.OutputFileExtension, '.', ''));



% Name of the data within the raw HDF files. 
% The reconstruction code looks for this,
% so I think it has to be named '/data' to be compatible.
DefaultJob.HdfDataName = '/data';

% Image numbers. Set endImage = inf and StartImage to 0 
%to transfer all .hdf images found
DefaultJob.EndImage = inf;
DefaultJob.StartImage = 0;



DefaultJob.Tiff_To_HDF5.InputDirectory = DefaultJob.HDf4_To_Tiff.OutputDataDir;
DefaultJob.Tiff_To_HDF5.ImageExt = DefaultJob.HDf4_To_Tiff.OutputFileExtension;

DefaultJob.Tiff_To_HDF5.StartData = 1;

DefaultJob.Tiff_To_HDF5.EndData = false;
DefaultJob.Tiff_To_HDF5.ScanStartRow = 0;
DefaultJob.Tiff_To_HDF5.ScanEndRow = false;
DefaultJob.Tiff_To_HDF5.WhiteStart = 0;
DefaultJob.Tiff_To_HDF5.WhiteEnd = 0;
DefaultJob.Tiff_To_HDF5.DarkStart = false;
DefaultJob.Tiff_To_HDF5.DarkEnd = false;
DefaultJob.Tiff_To_HDF5.DataClass = 'uint16';
DefaultJob.Tiff_To_HDF5.OutputDir = fullfile(DefaultJob.OutputDataRepository, DefaultJob.OutputCaseName, 'h5');
DefaultJob.Tiff_To_HDF5.OutputFileName = [DefaultJob.OutputCaseName '.h5'];
DefaultJob.Tiff_To_HDF5.CodeName = ;







% Add jobs here.
% Create the job list
SegmentItem = DefaultJob;
JOBLIST(1) = SegmentItem;

SegmentItem = DefaultJob;
SegmentItem.InputCaseName = 'A02';
SegmentItem.InputDataDir = fullfile(SegmentItem.InputCaseName, 'raw');
SegmentItem.OutputCaseName = 'A02';
SegmentItem.OutputDataDir = fullfile(SegmentItem.OutputCaseName, 'tif');
JOBLIST(end + 1) = SegmentItem;

SegmentItem = DefaultJob;
SegmentItem.InputCaseName = 'A03';
SegmentItem.InputDataDir = fullfile(SegmentItem.InputCaseName, 'raw');
SegmentItem.OutputCaseName = 'A03';
SegmentItem.OutputDataDir = fullfile(SegmentItem.OutputCaseName, 'tif');
JOBLIST(end + 1) = SegmentItem;



end












