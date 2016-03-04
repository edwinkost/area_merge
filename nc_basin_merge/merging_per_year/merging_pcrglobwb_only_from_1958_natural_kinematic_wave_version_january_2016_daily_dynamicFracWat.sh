#!/bin/bash
#SBATCH -N 1
#SBATCH -t 5:00:00 
#SBATCH -p fat                                                                                                                                                                              

# dynamicFracWat
python merging_per_year.py /projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_natural_kinematic_wave/continue_from_1958 dynamicFracWat_dailyTot_output.nc daily 1958 1965 /scratch-shared/edwin/05min_runs_january_2016_merged/pcrglobwb_only_from_1958_natural_kinematic_wave/daily/ &
python merging_per_year.py /projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_natural_kinematic_wave/continue_from_1966 dynamicFracWat_dailyTot_output.nc daily 1966 1971 /scratch-shared/edwin/05min_runs_january_2016_merged/pcrglobwb_only_from_1958_natural_kinematic_wave/daily/ &
python merging_per_year.py /projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_natural_kinematic_wave/continue_from_1972 dynamicFracWat_dailyTot_output.nc daily 1972 1978 /scratch-shared/edwin/05min_runs_january_2016_merged/pcrglobwb_only_from_1958_natural_kinematic_wave/daily/ &
python merging_per_year.py /projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_natural_kinematic_wave/continue_from_1979 dynamicFracWat_dailyTot_output.nc daily 1979 1992 /scratch-shared/edwin/05min_runs_january_2016_merged/pcrglobwb_only_from_1958_natural_kinematic_wave/daily/ &
python merging_per_year.py /projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_natural_kinematic_wave/continue_from_1993 dynamicFracWat_dailyTot_output.nc daily 1993 1999 /scratch-shared/edwin/05min_runs_january_2016_merged/pcrglobwb_only_from_1958_natural_kinematic_wave/daily/ &
python merging_per_year.py /projects/0/wtrcycle/users/edwin/05min_runs_january_2016/pcrglobwb_only_from_1958_natural_kinematic_wave/continue_from_2000 dynamicFracWat_dailyTot_output.nc daily 2000 2010 /scratch-shared/edwin/05min_runs_january_2016_merged/pcrglobwb_only_from_1958_natural_kinematic_wave/daily/ &
wait
