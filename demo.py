# -*- coding: utf-8 -*-
import tomopy

# Read HDF5 file.
data, white, dark, theta = tomopy.xtomo_reader('out.h5',
                                               slices_start=0,
                                               slices_end=19)
            
# Xtomo object creation and pipeline of methods.  
d = tomopy.xtomo_dataset(log='debug')
d.dataset(data, white, dark, theta)
d.normalize()
d.correct_drift()
d.phase_retrieval()
d.correct_drift()
#d.center=661.5
d.center=640;
d.gridrec()


# Write to stack of TIFFs.
tomopy.xtomo_writer(d.data_recon, 'tmp/test_', axis=0)

