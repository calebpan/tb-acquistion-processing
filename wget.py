#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:20:21 2018

@author: calebpan

Caleb. G. Pan
University of Montana
Numerical Terradynamic Simulation Group
Missoula, MT, USA
email caleb.pan@mso.umt.edu

THIS SCRIPT PROVIDES A PROCDURE TO DOWNLOAD MEaSUREs CALIBRATED ENHANCED-
RESOLUTION PASSIVE MICRWOAVE DAILY EASE-GRID 2.0 BRIGHTNESS TEMPERATURE ESDR
VERSION 1 IMAGES (https://nsidc.org/data/NSIDC-0630/versions/1) USING WGET.
THE SCRIPT CAN BE EASILY MODIFIED TO ACQUIRE A NUMBER OF SATELLITE DERIVED
DATASETS.

"""

import os
import datetime


def wget(fseries, freq, start, end,extent,sensor,src, resample):
    
    outdir = '/anx_lagr2/MEASURES_TB/' #SET OUTPUT DIRECTORY
    root = 'https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0630.001/'
    
    ##THE WGET COMMAND
    wget = 'wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies \
    --\keep-session-cookies --no-check-certificate --auth-no-challenge \
    -R *.xml -r --reject "index.html*" --directory-prefix='   
    
    ##USER DEFINED USERNAME AND PASSWORD
    login = ' --http-user=USERNAME --http-password=PASSWORD'

    ## THE MONTHS OF YEAR OF DATA THAT WILL BE DOWNLOADED
    monthlist = ['09']
  
    for i in range(start,end,1):
        year = str(i)
        for month in monthlist:            
            for day in range(1,32,1): ##CALENDAR DAYS
                if day < 10:
                    day = '0' + str(day)
                else:
                    day = str(day)  
                try:
                    date = datetime.datetime(int(year), int(month), int(day))
                    jd = date.strftime('%j')
                    
                    http = root  + year + '.' + month + '.' + day + '/'+ \
                    'NSIDC-0630-EASE2_N' + extent+'km-'+ fseries + '_' + \
                    sensor + '-'+ year + jd + '-' + freq + resample + src \
                    +'-v1.3.nc'
                    
                    makedir = outdir + year + month + day 
                    command = wget + makedir + ' -np -e robots=off ' \
                    + http + login
                    
                    print command
                    
                    #MAKE A DIRECTORY TO SAVE THE INCOMING IMAGE
                    os.system('mkdir ' + makedir)
                    
                    ##CALL THE WGET COMMAND
                    os.system(command)
                except:
                    pass
     
             

# =============================================================================
# SET YOUR INPUTS
# AS AN EXAMPLE, LET'S DOWNLOAD SSMI IMAGES AT VERTICALLY POLARIZED, 37 GHZ, 
# EVENING ACQUISTIONS FROM THE F15 SERIES AT THE ENHANCED SPATIAL RESOLUTION
# OF 3.125 KM (RATHER THAN 25) DURING THE YEAR 2001.   
# =============================================================================
                    
sensor = 'SSMI'
frequency = '37V-E'
extent = '3.125'
fseries = 'F15'
resample = '-SIR-'         
src = 'CSU'
startyear = 2001
endyear = 2002

wget(fseries,frequency,startyear,endyear,extent,sensor,src,resample)




