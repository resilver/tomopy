from tomoJobFileClass import img2tiffJobFile as tjf
from tomoJobFileClass import hdf5toReconJobFile as rjf

def tomoJobList():
    img2tiffJobList = [];
    reconJobList = [];
    
    
    img2tiffJobList.append(tjf())
    reconJobList.append(rjf())
    
    return (img2tiffJobList, reconJobList)
    



