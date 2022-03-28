def main():
    # import sys
    # sys.path.extend(['/home/jang/data/Python3/pyaerocom'])
    from pyaerocom.io.read_eea_aqerep_v2 import ReadEEAAQEREP_V2
    import pyaerocom as pya
    # pya.change_verbosity('warning')
    filename = '/lustre/storeA/project/aerocom/aerocom1/AEROCOM_OBSDATA/EEA_AQeRep.v2/renamed/SE/SE_6001_31058_2018_timeseries.csv.gz'
    r = ReadEEAAQEREP_V2()
    data = r.read(vars_to_retrieve=['concco'])
    # data = r.read_file(filename, 'concco')
    # data = r.read_file(filename, 'concpm25')
    print('finished')
    
    

if __name__ == "__main__":
    main()