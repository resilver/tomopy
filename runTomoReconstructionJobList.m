function runTomoReconstructionJobList(JOBLIST)

% Count the numeber of jobs
nJobs = length(JOBLIST);

% Loop over all jobs
for n = 1 : nJobs
    JobFile = JOBLIST(n);
    
    % Determine the paths to the input and output data repositories.
    inputRepository = JobFile.InputDataRepository;
    outputRepository = JobFile.OutputDataRepository;

    % Determine the short paths to the input and output directories
    inputDir = JobFile.HDF4_To_Tiff.InputDataDir;
    outputDir = JobFile.HDF4_To_Tiff.OutputDataDir;
    
    % Input and ouput file extensions
    inputFileExtension = JobFile.HDF4_To_Tiff.InputFileExtension;
    outputFileExtension = JobFile.HDF4_To_Tiff.OutputFileExtension;

    % Determine the full path to the input directory
    inputDataDir = fullfile(inputRepository, inputDir);
    
    % Make the output dir if it doesn't exist
    if ~exist(outputDir, 'dir');
        mkdir(outputDir)
    end

    % Read all the contents of the directory
    directoryContents = dir(inputDataDir);
    
    % Determine the name of the HDF data set within the structure
    hdfDataName = JobFile.HDF4_To_Tiff.HdfDataName;

    % Number of files in the input directory
    nFiles = length(directoryContents);

    % Number of images copied
    nCopied = 0;
    k = 1;
    % Figure out the last image
    endImage = min(nFiles, JobFile.HDF4_To_Tiff.EndImage);
    startImage = max(1, JobFile.HDF4_To_Tiff.StartImage);

    %% This part converts the raw HDF4 images to tiffs
    % if that option was specified in the job file.
    % Always do this for now.
%     if true;
    if JobFile.JobOptions.ConvertHDF4ToTiff 
        % Inform the user
        disp(['Copying set ' inputDataDir ' --> ' outputDir '...']);
    
        % Determine whether or not the images are tiffs.
        isTiff = ~isempty(regexpi(outputFileExtension, 'tif'));
        % Copy the images and conver to tiff
        try
            while nCopied < endImage
               if regexp(directoryContents(k).name, inputFileExtension);
                   % Figure out the input file name and path
                   inputFileName = directoryContents(k).name;
                   inputFilePath = fullfile(inputDataDir, inputFileName);

                   % Figure out the output file name and path
                   outputFileName = [directoryContents(k).name(1:end-length(inputFileExtension)-1) '.' strrep(outputFileExtension, '.', '')];
                   outputFilePath = fullfile(outputDir, outputFileName);

                   % Copy the data
                   if k >= startImage
                       % Read in the raw hdf data
                       inputFile = hdfread(inputFilePath, hdfDataName);

                       % Write the image data to a tiff file. Make sure no
                       % compression is applied for tif data. This has to
                       % be done in an if statement because of matlab.
                       if isTiff;
                            imwrite(inputFile, outputFilePath, 'compression', 'none');
                       else
                           imwrite(inputFile, outputFilePath);
                       end

                       % increment the copy count
                       nCopied = nCopied + 1;

                   end
               end  
               % Advance the image counter
               k=k+1;              
            end
            
        catch ER
            % Throw an error message if something goes wrong but proceed to the
            % next step.
            disp([ER.message]);
            disp(['Error transferring data for case ' JobList.InputCaseName])
        end
    end
    
    %% This part converts the TIF images to HDF5 format.
    if JobFile.JobOptions.ConvertTiffToHDF5
%     if 1 == 0; % This is disabled because I can't get it to work.
        try
            tiff_to_hdf5(JobFile);
        catch ER
            disp([ER.message]);
            disp(['Error in converting tiffs to HDF5 for case ' JobList.InputCaseName]);
        end
    end
    
    %% This part runs the tomographic reconstructions.
    % This is disabled.
    if 1 == 0;
%     if JobFile.JobOptions.ConvertHDF5ToRecon
        try
            runTomoReconstructions(JobFile);        
        catch ER
            disp([ER.message])
            disp(['Error in reconstructions for case ' JobList.InputCaseName]);
        end
    end

end

 
end







