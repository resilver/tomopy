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
SegmentItem.JobOptions.ConvertHDF4ToTiff = true;
% Whether or not to convert the TIF images to HDF5 after transferring.
SegmentItem.JobOptions.ConvertToHDF5 = false;
% Whether or not to call the Python reconstruction code
% after moving each dataset.
SegmentItem.JobOptions.DoReconstructions = false;
JOBLIST(1) = SegmentItem;

% Second job
SegmentItem = DefaultJob;
SegmentItem.JobOptions.ConvertHDF4ToTiff = false;
SegmentItem.JobOptions.ConvertTiffToHDF5 = true;
SegmentItem.JobOptions.ConvertHDF5ToRecon = false;
JOBLIST(end + 1) = updateJobList(SegmentItem, 'A02');

% Third job
SegmentItem = DefaultJob;
SegmentItem.JobOptions.ConvertHDF4ToTiff = true;
SegmentItem.JobOptions.ConvertTiffToHDF5 = false;
SegmentItem.JobOptions.ConvertHDF5ToRecon = false;
JOBLIST(end + 1) = updateJobList(SegmentItem, 'A03');

% Third job
SegmentItem = DefaultJob;
SegmentItem.JobOptions.ConvertHDF4ToTiff = true;
SegmentItem.JobOptions.ConvertTiffToHDF5 = false;
SegmentItem.JobOptions.ConvertHDF5ToRecon = false;
JOBLIST(end + 1) = updateJobList(SegmentItem, 'A04');




end












