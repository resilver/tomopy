function DefaultJob = defaultJobList();

% Number of processors to use
DefaultJob.JobOptions.NumberOfProcessors = 1;

% This specifies whether to convert the raw HDF4 data to tiffs.
DefaultJob.JobOptions.ConvertHDF4ToTiff = false;

% Whether or not to convert the TIF images to HDF5 after transferring.
DefaultJob.JobOptions.ConvertTiffToHDF5 = true;

% Whether or not to call the Python reconstruction code
% after moving each dataset.
DefaultJob.JobOptions.ConvertHDF5ToRecon = false;


%% Parameters for converting HDF4 to Tiff
% Data repositories
DefaultJob.CaseName = 'A01';

% Output data repository
DefaultJob.OutputDataRepository = '/Users/mattgiarra/Documents/tomography/data/2013_07_2BM_copy/Jeff';
DefaultJob.InputDataRepository = '/Volumes/128.173.163.248/2013_07_2BM_copy/Jeff';

% Input and ouput file extensions

DefaultJob.HDF4_To_Tiff.InputDataDir = fullfile(DefaultJob.InputDataRepository, DefaultJob.CaseName, 'raw');
DefaultJob.HDF4_To_Tiff.InputFileExtension = 'hdf';
DefaultJob.HDF4_To_Tiff.HdfDataName = '/data';
DefaultJob.HDF4_To_Tiff.OutputFileExtension = '.tif';
DefaultJob.HDF4_To_Tiff.OutputCaseName = DefaultJob.CaseName ;
DefaultJob.HDF4_To_Tiff.OutputDataDir = fullfile(DefaultJob.OutputDataRepository, DefaultJob.CaseName, strrep(DefaultJob.HDF4_To_Tiff.OutputFileExtension, '.', ''));

% Image numbers. Set endImage = inf and StartImage to 0 
%to transfer all .hdf images found
DefaultJob.HDF4_To_Tiff.StartImage = 0;
DefaultJob.HDF4_To_Tiff.EndImage = inf;

%% Parameters for converting Tiffs to HDF5
DefaultJob.Tiff_To_HDF5.InputDirectory = DefaultJob.HDF4_To_Tiff.OutputDataDir;
DefaultJob.Tiff_To_HDF5.ImageExt = DefaultJob.HDF4_To_Tiff.OutputFileExtension;
DefaultJob.Tiff_To_HDF5.StartImage = 1;
DefaultJob.Tiff_To_HDF5.EndImage = 'None';
DefaultJob.Tiff_To_HDF5.ScanStartRow = 'None';
DefaultJob.Tiff_To_HDF5.ScanEndRow = 'None';
DefaultJob.Tiff_To_HDF5.WhiteStart = 0;
DefaultJob.Tiff_To_HDF5.WhiteEnd = 0;
DefaultJob.Tiff_To_HDF5.DarkStart = 'None';
DefaultJob.Tiff_To_HDF5.DarkEnd = 'None';
DefaultJob.Tiff_To_HDF5.DataClass = 'uint16';
DefaultJob.Tiff_To_HDF5.OutputDir = fullfile(DefaultJob.OutputDataRepository, DefaultJob.CaseName, 'h5');
DefaultJob.Tiff_To_HDF5.OutputFileName = [DefaultJob.CaseName '.h5'];
DefaultJob.Tiff_To_HDF5.CodeName = 'im2hd5.py';

% Parameters for hdf5 to tomo reconstruction
DefaultJob.HDF5_To_Recon.InputDirectory = DefaultJob.Tiff_To_HDF5.OutputDir;
DefaultJob.HDF5_To_Recon.InputFileName = DefaultJob.Tiff_To_HDF5.OutputFileName;
DefaultJob.HDF5_To_Recon.StartSlice = false;
DefaultJob.HDF5_To_Recon.EndSlice = false;
DefaultJob.HDF5_To_Recon.OutputDir = fullfile(DefaultJob.OutputDataRepository, DefaultJob.CaseName, 'recon');
DefaultJob.HDF5_To_Recon.CodeName = 'h5f_to_recon';

end
%%



