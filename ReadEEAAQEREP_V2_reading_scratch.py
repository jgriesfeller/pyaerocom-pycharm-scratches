import tests.conftest

def main():
    # import sys
    # sys.path.extend(['/home/jang/data/Python3/pyaerocom'])
    from pyaerocom.io.read_eea_aqerep_v2 import ReadEEAAQEREP_V2
    var_name = 'concpm10'
    import pyaerocom as pya
    # pya.change_verbosity('warning')
    filename = '/lustre/storeA/project/aerocom/aerocom1/AEROCOM_OBSDATA/EEA_AQeRep.v2/renamed/SE/SE_6001_31058_2018_timeseries.csv.gz'
    r = ReadEEAAQEREP_V2("EEA_AQeRep.v2.Subset")
    # ReadEEAAQEREP_V2.FILE_MASKS["concpm10"] = "**/??_5_*_2019_timeseries.csv*"
    data = r.read(vars_to_retrieve=[var_name])
    print(data)
    print('finished')
    
    

if __name__ == "__main__":
    main()