function pyReturn = runTomoReconstructions(JobFile)
% This function drives the python code hf5_to_recon, which does the tomographic
% reconstructions. That function's inputs are formatted like this:
%  hd5_to_recon(dirName='.', inputFileName='out.h5', startSlice=None, endSlice=None, outDir='.'):  

% Format the inputs
dir_name = JobFile.HDF5_To_Recon.InputDirectory;
input_file_name = JobFile.HDF5_To_Recon.InputFileName;
start_slice = JobFile.HDF5_To_Recon.StartSlice;
end_slice = JobFile.HDF5_To_Recon.EndSlice;
output_dir = JobFile.HDF5_To_Recon.OutputDir;
code_name = JobFile.HDF5_To_Recon.CodeName;

% Make the output directory if it doesn't exist.
if ~exist(output_dir, 'dir');
    mkdir(output_dir)
end

pythonInput = sprintf(...
           ['%s(dirName=''%s'', inputFileName=''%s'', '...
       'startSlice=%d','endSlice=%d, outDir=%s, '...
       code_name, dir_name, input_file_name, start_slice, end_slice, output_dir]);

% This is the command line statement that will run the code.
command = sprintf('python -c ''%s''', pythonInput);

% This returns 0 if the code ran successfully, I think.
pyReturn = system(command);



end