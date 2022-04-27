# quick and dirty test for obs reading via the api

import tests.conftest
# VAR_NAME = ['concpm10']
# VAR_NAME = ['concpm25']
VAR_NAME = ['ratpm10pm25']
TS_TYPE = 'daily'
from pyaerocom import const
# ReadEEAAQEREP_V2.FILE_MASKS["concpm10"] = "**/AT*_5_*_2019_timeseries.csv*"
# ReadEEAAQEREP_V2.FILE_MASKS["concpm25"] = "**/AT*_6001_*_2019_timeseries.csv*"
# obs_data = obs_obj.read(vars_to_retrieve=VAR_NAME, ts_type=TS_TYPE)
# obs_data2 = obs_obj.read(vars_to_retrieve=VAR_NAME2)
# DATA_ID = "EEA_AQeRep.v2.Subset"

DATA_ID = 'EEAAQeRep.v2'
# DATA_ID = const.EBAS_MULTICOLUMN_NAME

def print_means(obs_data, vars=VAR_NAME, max_idx_to_print=3):
    print_idx = 1
    # vars.append('concpm10')
    # vars.append('concpm25')
    for var in vars:
        print(f"variable: {var}")
        for meta_idx in obs_data.unique_station_names:
            pass
            mean = obs_data[meta_idx][var].mean()
            min = obs_data[meta_idx][var].min()
            max = obs_data[meta_idx][var].max()

            print(f"station {meta_idx}: mean: {mean}; min: {min}; max: {max}")
            if print_idx >= max_idx_to_print:
                break


def main():
    import pyaerocom.io as pio
    obs_obj = pio.ReadUngridded(DATA_ID)
    obs_data1 = obs_obj.read(vars_to_retrieve=VAR_NAME)
    print_means(obs_data1, VAR_NAME)
    print(obs_data1)


if __name__ == "__main__":
    main()

# AT_6001_68561_2019_timeseries.csv.gz
# AT_5_68560_2019_timeseries.csv.gz
# AT_5_68588_2019_timeseries.csv.gz
# AT4S432