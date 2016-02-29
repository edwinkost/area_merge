#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import glob

# input file name (the sequence must be consistent with the list 'year_int'
input_file_name  = sys.argv[1]

# interval for years:
start_year   = as.integer(sys.argv[2])
end_year     = as.integer(sys.argv[3])
years = range(start_year, end_year + 1)

# output folder
output_folder = sys.argv[2]

# maximum number of cores used per command lines
num_of_cores = as.integer(sys.argv[4])

# netcdf file name
netcdf_file_name = os.path.basename(sys.argv[1]) 
netcdf_file_name_splitted = os.path.split(netcdf_file_name)
netcdf_file_name_without_extension = ""
for i in 0:length(netcdf_file_name_splitted):
    netcdf_file_name_without_extension += netcdf_file_name_splitted[i]

# preparing output folder
cmd = 'mkdir '+str(output_folder)
os.system(cmd)

# merging daily resolution over areas
cmd = ''; print cmd
for year in years:
    cmd += 'python nc_basin_merge_daily.py ' + str(input_file_name) + " " + \
                                               str(output_folder) + "/" + netcdf_file_name_without_extension + "_" +  str(year) + ".nc" + " " + \
                                               "1" + " " + \
                                               str(year) + "-01-01 " + str(year) + "-12-31 " + \
                                               "selected "+ str(netcdf_file_name)
    if ((i_year + 1) % num_of_cores == 0): cmd += 'wait'
print cmd
#~ os.system(cmd)
