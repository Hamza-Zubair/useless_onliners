import os
import shutil
import time
# function to copy specific files from directory and sub directories
def file_copier(source, extension):
    """
    Copies all files of specified extension from source directory/sub-directories
    Input:
    -----
    source: directory from where the files to be copied
    extension: str or tuple of str.
    Output:
    -----
    folder named "out" consisting all files of desired extension
    Dependencies:
    -----
    os, shutil, time libraries
    """
    # PEN DOWN THE TIME
    before_copy = time.time()
    
    # CHECK IF SOURCE DIRECTORY EXISTS OR ELSE THROW EXCEPTION
    if os.path.isdir(source) is True :
        destination = os.path.join(source, 'out')
        if os.path.isdir(destination):
            pass
        else:
            os.mkdir(destination)
        for folder, subfolder, filenames in os.walk(source):
            for filename in filenames:
                path_file = os.path.join(folder,filename)
                if path_file.endswith(extension):
                    try:
                        shutil.copy(path_file, destination)
                    except:
                        pass
    else:
        raise Exception("Source directory not found")
    
    # CHECKS THE COUNT OF COPIED FILES
    count = 0
    if len(os.listdir(destination)) > 0:
        for i in os.listdir(destination):
            timer_path = os.path.join(destination, i)
            timer = os.path.getmtime(timer_path)
            if timer > before_copy:
                count = count+1
        return('Count of copied files with {} extension is: {}'.format(extension, str(count)))
    else:
        return('No new file/s found with {} file extension'.format(extension))



# set source direcotry
src = (r'C:\Users\3d-digi\Desktop\script_making_shp')

# extension/s of file/s to be seperated. can be single str or tuple of str
ext = ('.shp','.dbf','.prj','.shx')

# run the function, tested with 200 folders and subfolders. takes ~0.2 secs
file_copier(src ,ext)