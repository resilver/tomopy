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


% These data can be either numbers or strings
ambiguous_data = {start_slice; end_slice};

% Convert all the ambiguous data to strings.
for k = 1 : length(ambiguous_data)
    stringData{k} = num2str(ambiguous_data{k});
end

% Make the output directory if it doesn't exist.
if ~exist(output_dir, 'dir');
    mkdir(output_dir)
end

% Create the string to be run   
String = sprintf('source /Users/mattgiarra/virt_env/virt1/bin/activate; python %s %s %s %s %s %s', ...
    code_name, dir_name, input_file_name, stringData{:}, output_dir);
    
% This returns 0 if the code ran successfully, I think.
pyReturn = system(String);


end