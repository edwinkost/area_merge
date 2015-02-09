#!/bin/bash
#SBATCH -N 1
#SBATCH -t 119:59:00 
#SBATCH -p normal
#SBATCH -n 24       # number of CPUs requested; required for a correct multicore multi processing

cd /home/edwin/edwinkost/github/area_merge/nc_basin_merge
python nc_basin_merge.py /projects/wtrcycle/users/edwinhs/05min_runs_28_november_2014/multi_cores_non_natural_1960_to_2010 /projects/wtrcycle/users/edwin/05min_runs_28_november_2014/multi_cores_non_natural_1960_to_2010/global 2

