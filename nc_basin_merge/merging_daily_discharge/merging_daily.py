#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import glob

# netcdf file name:
netcdf_file_name = sys.argv[1] 

# output folders 
output_folder    = '/scratch-shared/edwinhs/tmp/daily_file/'

# interval for years:
year_int  = [1986, 1987]

# input folders (the sequence must be consistent with the list 'year_int'
input_folder = [
'/projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_4LCs_edwin_parameter_set_kinematic_wave/continue_from_1983',
'/projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_4LCs_edwin_parameter_set_kinematic_wave/continue_from_1983',
]

# maximum number of cores used per command lines
num_of_cores = 30

# preparing output folder
cmd = 'mkdir '+str(output_folder)
os.system(cmd)

# TODO: copying the script 'nc_basin_merge.py' to the output_folder and change the working directory to the output_folder (such that the 'nc_basin_merge.py' will not be affected by any changes)

# merging daily resolution over areas
cmd = ''; print cmd
for i_year in range(0, len(year_int)-1):
    cmd += 'python nc_basin_merge.py %s %s/%i_to_%i/ %i %i-01-01 %i-12-31 selected %s & ' %(input_folder[i_year]         , output_folder, year_int[i_year]         , year_int[i_year+1]-1, num_of_cores, year_int[i_year]         , year_int[i_year+1]-1, netcdf_file_name)
cmd     += 'wait'
print cmd
os.system(cmd)
