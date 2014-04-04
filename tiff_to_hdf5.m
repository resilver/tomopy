function pyReturn = tiff_to_hdf5(JobFile)
% This function calls the python script:
% im2hd5(dirName='.', imageExt='tif', ...
%dataStart=0, dataEnd=None, scanStartRow=0, ..
%scanEndRow=None, whiteStart=None, whiteEnd=None, ...
%darkStart=None, darkEnd=None, dataClass = 'uint16', ...
%outputDir='.', outputFileName = 'out.h5')

input_directory = JobFile.Tiff_To_HDF5.InputDirectory;
input_image_ext = JobFile.Tiff_To_HDF5.ImageExt;
start_data = JobFile.Tiff_To_HDF5.StartImage;
end_data = JobFile.Tiff_To_HDF5.EndImage;
scan_start_row = JobFile.Tiff_To_HDF5.ScanStartRow;
scan_end_row = JobFile.Tiff_To_HDF5.ScanEndRow;
white_start = JobFile.Tiff_To_HDF5.WhiteStart;
white_end = JobFile.Tiff_To_HDF5.WhiteEnd;
dark_start = JobFile.Tiff_To_HDF5.DarkStart;
dark_end = JobFile.Tiff_To_HDF5.DarkEnd;
data_class = JobFile.Tiff_To_HDF5.DataClass;
output_dir = JobFile.Tiff_To_HDF5.OutputDir;
output_file_name = JobFile.Tiff_To_HDF5.OutputFileName;
code_name = JobFile.Tiff_To_HDF5.CodeName;

% Make the output dir if it doesn't exist
if ~exist(output_dir, 'dir')
    mkdir(output_dir);
end

String = ['%s(dirName=''%s'', imageExt=''%s'','...
    'dataStart=%d, dataEnd=%d, scanStartRow=%d, '...
    'scanEndRow=%d, whiteStart=%d, whiteEnd=%d, '...
    'darkStart=%d, darkEnd=%d, dataClass=''%s'',' ...
    'outputDir=''%s'', outputFileName=''%s'''];

pythonInput = sprintf(String,code_name, input_directory, ...
    input_image_ext, start_data, end_data,scan_start_row, ...
    scan_end_row, white_start, white_end, dark_start, ...
    dark_end, data_class, output_dir, output_file_name);

% This is the command line statement that will run the code.
command = sprintf('python -c ''%s''', pythonInput);

% This returns 0 if the code ran successfully, I think.
pyReturn = system(command);

end


