#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import glob

# input folder
input_folder  = sys.argv[1]

# netcdf file name
netcdf_file_name = os.path.basename(sys.argv[2])                                                   # example: netcdf_file_name = "test0.test1.test2.nc"
netcdf_file_name_splitted = netcdf_file_name.split(".")
netcdf_file_name_without_extension = ""
for i in range(0, len(netcdf_file_name_splitted) - 1, 1): 
    netcdf_file_name_without_extension += netcdf_file_name_splitted[i]
    if (i < (len(netcdf_file_name_splitted) - 2)): netcdf_file_name_without_extension += "."

# interval for years:
start_year   = int(sys.argv[3])
end_year     = int(sys.argv[4])
years = range(start_year, end_year + 1)

# output folder
output_folder = sys.argv[5]

# preparing output folder
try:
    os.makedirs(output_folder)
except:
    cmd = 'mkdir '+str(output_folder)
    os.system(cmd)

# merging daily resolution over areas
cmd = ''; print cmd
i_year = 0
for year in years:
    cmd += 'python nc_basin_merge_daily.py ' + str(input_folder) + " " + \
                                               str(output_folder) + "/" + netcdf_file_name_without_extension + "_" +  str(year) + ".nc" + " " + \
                                               "1" + " " + \
                                               str(year) + "-01-01 " + str(year) + "-12-31 " + \
                                               "selected "+ str(netcdf_file_name)
    cmd += " & "
cmd = cmd + "wait"       
print cmd
os.system(cmd)

# example: python merging_daily_per_year.py /projects/0/wtrcycle/users/edwinhs/05min_runs_january_2016/pcrglobwb_only_from_1958_4LCs_edwin_parameter_set discharge_dailyTot_output.nc 1958 2010 /scratch-shared/edwin/tmp/test/
