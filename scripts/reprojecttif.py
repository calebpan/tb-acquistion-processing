#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:34:02 2018

@author: caleb.pan
"""
# =============================================================================
# THIS SCRIPT REPROJECTS RASTER TIFS BASED ON A
# USER DEFINED EPSG AND REMOVES THE SUBSEQUENT
# INPUT TIF FILE
# =============================================================================

import os

#==============================================================================
# SET THE ROOT DIRECTORY FOLDER
#==============================================================================
root = '/anx_lagr3/measurestb/1992/'

#==============================================================================
# SET THE FILENAME
#==============================================================================
filename = 'NSIDC-0630-EASE2_N6.25km-F11_SSMI-1992151-19V-E-SIR-CSU-v1.3.tif'

#==============================================================================
# DEFINE THE NEW EPSG
#==============================================================================
epsg = 'EPSG:102006'

infile = root + filename

#==============================================================================
# SET 'REPROJ.TIF' TO AT THE END OF THE OUTFILE TO DESCRIBE THE NEW DATAFILE
#==============================================================================
outfiles = infile[:-3] + '_reproj.tif'

#==============================================================================
# CREATE THE REPROJECT COMMAN USING GDALWARP
#==============================================================================
command = 'gdalwarp -overwrite -t_srs ' + epsg + ' -of GTiff ' + \
        infile + ' ' + outfiles
        
print 'reprojecting ' + infile

#==============================================================================
# CALL THE COMMAND USING OS
#==============================================================================
os.system(command)
#os.remove(infile) ##OPTION TO DELETE THE INPUTFILE




