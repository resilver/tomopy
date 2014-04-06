function JOBLIST = tomoReconJobList;
% This function is used to create a job list which can drive
% the tomographic reconstruction process from raw projection images
% to reconstructed slices.
% For details about the contents of the job files,
% see the function defaultJobList.
%
% Example usage:
%   JobList = hdf2tiffJobList;
%   runTomoReconstructionJobList(JobList) % Do this to run all the jobs
%   runTomoReconstructionJobList(JobList(1)) % Do this to run just one job
%   runTomoReconstructionJobList(JobList(2:5)) % Do this to run a few jobs.

% Get the default job
DefaultJob = defaultJobList;

%% This where you update your own jobs.

% First job
SegmentItem = DefaultJob;
SegmentItem.CaseName = 'test_sample_Diplo_4';
SegmentItem.Tiff_To_HDF5.InputDirectory = '/Volumes/128.173.163.248/2013_07_2BM_copy/Jeff/test_sample_Diplo_4';
SegmentItem.Tiff_To_HDF5.ImageExt = '.tif';
SegmentItem.Tiff_To_HDF5.StartImage = 1;
SegmentItem.Tiff_To_HDF5.EndImage = 'None';
SegmentItem.Tiff_To_HDF5.ScanStartRow = 'None';
SegmentItem.Tiff_To_HDF5.ScanEndRow = 'None';
SegmentItem.Tiff_To_HDF5.WhiteStart = 1510;
SegmentItem.Tiff_To_HDF5.WhiteEnd = 'None';
SegmentItem.Tiff_To_HDF5.DarkStart = 1500;
SegmentItem.Tiff_To_HDF5.DarkEnd = 1509;
SegmentItem.Tiff_To_HDF5.DataClass = 'uint16';
SegmentItem.Tiff_To_HDF5.OutputDir = fullfile(SegmentItem.OutputDataRepository, SegmentItem.CaseName, 'h5');
SegmentItem.Tiff_To_HDF5.OutputFileName = [SegmentItem.CaseName '.h5'];
SegmentItem.Tiff_To_HDF5.CodeName = 'im2hd5.py';

% Parameters for hdf5 to tomo reconstruction
SegmentItem.HDF5_To_Recon.InputDirectory = SegmentItem.Tiff_To_HDF5.OutputDir;
SegmentItem.HDF5_To_Recon.InputFileName = SegmentItem.Tiff_To_HDF5.OutputFileName;
SegmentItem.HDF5_To_Recon.StartSlice = 'None';
SegmentItem.HDF5_To_Recon.EndSlice = 'None';
SegmentItem.HDF5_To_Recon.OutputDir = fullfile(SegmentItem.OutputDataRepository, SegmentItem.CaseName, 'recon');
SegmentItem.HDF5_To_Recon.CodeName = 'h5f_to_recon.py';

% This specifies whether to convert the raw HDF4 data to tiffs.
SegmentItem.JobOptions.ConvertHDF4ToTiff = false;

% Whether or not to convert the TIF images to HDF5 after transferring.
SegmentItem.JobOptions.ConvertTiffToHDF5 = true;

% Whether or not to call the Python reconstruction code
% after moving each dataset.
SegmentItem.JobOptions.ConvertHDF5ToRecon = false;

JOBLIST(1) = SegmentItem;




end












