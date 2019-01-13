#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:08:17 2018

@author: caleb.pan
"""
# =============================================================================
# THIS SCRIPT IS A CONTINUATION OFF THE WGET.PY SCRIPT. HERE WE INPUT THE NEWLY
# DOWNLOADED NETCDF AND EXTRACT THE BRIGHTNESS TEMPERATURE (K) BAND AND CONVERT
# IT TO A GEOTIFF USING GDAL
# =============================================================================
import gdal
 
inputfile = 'FILENAME OF THE NETCDF TO FILE TO BE CONVERTED TO TIF'

# =============================================================================
# OPEN THE BRIGHTNESS TEMPERATURE (TB) VARIABLE STORED IN THE NETCDF                   
# =============================================================================
tb = gdal.Open('NETCDF:' + inputfile + ':TB')

# =============================================================================
# GET THE X,Y DIMENSIONS OF THE IMAGE
# =============================================================================
wide = tb.RasterXSize
high = tb.RasterYSize

# =============================================================================
# EXTRACT THE PROJECTION AND GEOTRANSFORM
# =============================================================================
prj = tb.GetProjection()
geo = tb.GetGeoTransform()

# =============================================================================
# EXTRACT THE BAND AND COVERT IT TO AN ARRAY
# =============================================================================
band = tb.GetRasterBand(1)
array = band.ReadAsArray()
array = array * 0.01

print 'converting netcdf to tif', inputfile
driver = gdal.GetDriverByName('GTiff')

# =============================================================================
# CREATE TIF FILE AS INT16, WRITE IT TO ONE BAND, AND ASSIGN THE X,Y DIMENSIONS
# =============================================================================
outraster = driver.Create(inputfile[:-3] +'.tif',wide,high,1, gdal.GDT_Int16)
outraster.SetGeoTransform(geo)
outraster.SetProjection(prj)
outraster.GetRasterBand(1).WriteArray(array)
                
# =============================================================================
# DELETE TB, OUTRASTER, AND DRIVER. IF NOT, THERE CAN BE A LOCK ASSIGNED TO 
# THE NEW TIF FILES.
# =============================================================================
del tb, outraster, driver
                    

