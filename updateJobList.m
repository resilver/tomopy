function JobFileOut = updateJobList(JobFileIn, caseName)
%% Parameters for converting HDF4 to Tiff
% This function modifies the file paths
% that a tomo reconstruction job file points to. 
% This is here so you can easily make new jobs without
% having to copy-paste a ton of code.
% Basically it's just guessing where you want to put things based
% on the name of the "case," like "A04", 'trial_02', etc.

% Copy the input job file to the output jobfile strucure
JobFileOut = JobFileIn;

% This reads the name of the data repository, which 
% probably won't change between jobs.
JobFileOut.CaseName = caseName;

% This reads the output repository, which probably won't change
% often between jobs
outputRepo = JobFileIn.OutputDataRepository;

% Parameters for converting HDF4 files to Tiff images.
JobFileOut.HDF4_To_Tiff.InputDataDir = fullfile(caseName, 'raw');
JobFileOut.HDF4_To_Tiff.OutputCaseName = caseName;
JobFileOut.HDF4_To_Tiff.OutputDataDir = fullfile(outputRepo, caseName, strrep(JobFileIn.HDF4_To_Tiff.OutputFileExtension, '.', ''));

% Parameters for converting Tiffs to HDF5
JobFileOut.Tiff_To_HDF5.InputDirectory = JobFileOut.HDF4_To_Tiff.OutputDataDir;
JobFileOut.Tiff_To_HDF5.OutputDir = fullfile(JobFileIn.OutputDataRepository, caseName, 'h5');
JobFileOut.Tiff_To_HDF5.OutputFileName = [caseName '.h5'];

% Parameters for hdf5 to tomo reconstruction
JobFileOut.HDF5_To_Recon.InputDirectory = JobFileOut.Tiff_To_HDF5.OutputDir;
JobFileOut.HDF5_To_Recon.InputFileName = JobFileIn.Tiff_To_HDF5.OutputFileName;
JobFileOut.HDF5_To_Recon.OutputDir = fullfile(JobFileIn.OutputDataRepository, caseName, 'recon');

    

end