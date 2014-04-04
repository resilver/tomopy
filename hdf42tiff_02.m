function hdf42tiff_02(JOBLIST)

% Count the numeber of jobs
nJobs = length(JOBLIST);

% Loop over all jobs
for n = 1 : nJobs
    JobFile = JOBLIST(n);
    
    % Determine the paths to the input and output data repositories.
    inputRepository = JobFile.InputDataRepository;
    outputRepository = JobFile.OutputDataRepository;

    % Determine the short paths to the input and output directories
    inputDir = JobFile.InputDataDir;
    outputDir = JobFile.OutputDataDir;
    
    % Input and ouput file extensions
    inputFileExtension = JobFile.InputFileExtension;
    outputFileExtension = JobFile.OutputFileExtension;

    % Determine the full path to the input directory
    inputDataDir = fullfile(inputRepository, inputDir);

    % Determine the full path to the output directory
    outputDataDir = fullfile(outputRepository, outputDir);
    
    if ~exist(outputDataDir, 'dir');
        mkdir(outputDataDir)
    end

    % Read all the contents of the directory
    directoryContents = dir(inputDataDir);
    
    % Determine the name of the HDF data set within the structure
    hdfDataName = JobFile.HdfDataName;

    % Number of files in the input directory
    nFiles = length(directoryContents);

    % Inform the user
    disp(['Copying set ' inputDataDir ' --> ' outputDataDir '...']);
    
    % Number of images copied
    nCopied = 0;
    k = 1;
    % Figure out the last image
    endImage = min(nFiles, JobFile.EndImage);
    startImage = max(1, JobFile.StartImage);

    % This part converts the raw HDF4 images to tiffs
    % if that option was specified in the job file.
    if JobFile.JobOptions.ConvertHDF4ToTiff   
        % Copy the images and conver to tiff
        try
            while nCopied < endImage
               if regexp(directoryContents(k).name, inputFileExtension);
                   % Figure out the input file name and path
                   inputFileName = directoryContents(k).name;
                   inputFilePath = fullfile(inputDataDir, inputFileName);

                   % Figure out the output file name and path
                   outputFileName = [directoryContents(k).name(1:end-length(inputFileExtension)-1) '.' strrep(outputFileExtension, '.', '')];
                   outputFilePath = fullfile(outputDataDir, outputFileName);

                   % Copy the data
                   if k >= startImage
                       % Read in the raw hdf data
                       inputFile = hdfread(inputFilePath, hdfDataName);

                       % Write the image data to a tiff file. Make sure no
                       % compression is applied for tif data. This has to
                       % be done in an if statement because of matlab.
                       if ~isempty(regexpi, outputFileExtension, 'tif');
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
    
    % Whether or not to convert the TIF images to hd5 after transferring.
    if JobFile.JobOptions.ConvertToHdf5
        try
            %%% Run my python script
        catch ER
            disp([ER.message]);
            disp(['Error in converting tiffs to HDF5 for case ' JobList.InputCaseName]);
        end
    end
    
    % If you've specified to do the reconstructions,they gets done here.
    if JobFile.JobOptions.DoReconstruction
        try
            runTomoReconstructions(JobFile);        
        catch ER
            disp([ER.message])
            disp(['Error in reconstructions for case ' JobList.InputCaseName]);
        end
    end

end

 
end







