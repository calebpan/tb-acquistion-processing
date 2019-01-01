#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:02:36 2018

@author: caleb.pan
"""

"""
Caleb G. Pan
University of Montana
Numerical Terradynamic Simulation Group
Missoula, MT, USA
email caleb.pan@mso.umt.edu

IF YOU ARE NOT PERFORMING GLOBAL ANALYSIS, CLIPPING LARGE GLOBALLY DERIVED 
SATELLITE REMOTE SENSING IMAGES TO A SUBSET REGION IS HELPFUL FOR IMPROVED
DATA STORAGE AND PROCESSING.

THIS SCRIPT PROVIDES A QUICK AND EASY SOLUTION TO CLIPPING (MASKING) GEOTIF
TO A SMALLER AREA OF INTEREST. SPECIFICALLY, WE INPUT A GEOTIF AND CLIP IT TO 
AN INPUT SHAPEFILE USING GDALWARP. THE EXAMPLE IS SET UP AS A BATCH PROCESS
TO CLIP ALL TIFS WITHIN THE INPUT DIRECTORY. IT IS IMPORTANT THAT THE 
SHAPEFILE AND TIFS ARE IN THE SAME PROJECTION - HERE THE EPSG = 102006.

"""

import os, glob

# =============================================================================
# SET YOUR INPUT ROOT DIRECTORY (root) AND YOUR OUTPUT ROOT DIRECTORY (outroot)
# THE STRUCTURE OF THE INPUT FILE IS AS FOLLOWS:
# /anx_lagr2/caleb/SnowAlaska/finaltifs/smd/smd_1980.tif
# =============================================================================
root = '/anx_lagr2/caleb/SnowAlaska/finaltifs/smd/smd_'
outroot = '/anx_lagr2/caleb/SnowAlaska/finaltifs/smd/'

# =============================================================================
# SET THE INPUT SHAPEFILE TO BE USED FOR CLIPPING
# =============================================================================
shp = '/anx_lagr2/caleb/SnowAlaska/Shapefiles/Alaska_102006.shp'
# =============================================================================
# IN THIS EXAMPLE SCRIPT, WE ARE WORKING WITH DATA THAT ARE CREATED FOR EACH
# YEAR. HERE, WE SET THE START AND END YEARS
# =============================================================================
start = 1980
end = 2017

# =============================================================================
# FOR BATCH PROCESSING - GLOB PROVIDES A USEFUL UTILITY TO LOOP THROUGH 
# DIRECTORY FILES
# =============================================================================
globdir = glob.glob(root + '*')

for i in range(start,end,1):
    year = str(i)

    inputfile = root + year + '.tif' #INPUT TIF
    outfile = outroot + 'smd_' + year + '_clip.tif' #OUTPUT TIF
    print outfile      
    
# =============================================================================
#     DEFINE THE GDALWARP COMMAND. 6250 IS THE SPATIAL RESOLUTION OF THE INPUT
#     AND OUTPUT GEOTIF
# =============================================================================
    command = 'gdalwarp -dstnodata -9999 -q -cutline ' + shp + \
    ' -crop_to_cutline -tr ' + str(6250) + ' ' + str(6250) + ' -of GTiff ' \
    + inputfile + ' ' + outfile       
    
# =============================================================================
#     CALL THE COMMAND USING OS
# =============================================================================
    os.system(command)
 #   os.remove(inputfile) ##OPTIONALLY, DELETE THE INPUT TIF

