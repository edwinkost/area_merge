#!/bin/bash
#SBATCH -N 1
#SBATCH -t 81:59:00
#SBATCH -p normal

cd /home/edwinhs/git/nc_basin_merge
python nc_basin_merge.py /projects/wtrcycle/users/edwinhs/05min_runs_28_november_2014/multi_cores_natural_1960_to_2010/ 4


