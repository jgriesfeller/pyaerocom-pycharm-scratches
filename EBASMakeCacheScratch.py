def main():
    from pyaerocom import const
    import pyaerocom.io as pio
    import pyaerocom as pya
    import numpy as np

    # DATA_ID = const.EBAS_MULTICOLUMN_NAME
    DATA_ID = const.EEA_NRT_NAME
    reader = pio.ReadUngridded(DATA_ID)
    vars_to_cache = [
        # "concso4pm25",
        # "concso4pm10",
        # "concpm10",
        # "concpm25",
        "concso2",
        # "concso4",
        # "concbc",
        # "concoa",
        # "conctc",
        # "concno2",
        # "concno3",
        # "concnh3",
        # "concnh4",
        # "wetso4",
        # "concso4pr",
        # "concco",
        # "vmro3",
    ]

    for var_to_read in vars_to_cache:
        data = reader.read(vars_to_retrieve=var_to_read)
        print(data)
        print(f"var {var_to_read} # of unique stations: {len(data.unique_station_names)}")
        units = np.unique([data.metadata[x]['var_info'][var_to_read]['units'] for x in data.metadata])
        print(f"var {var_to_read} unique units: {units}")
        if len(units) > 1:
            for unit in units:
                print(f"var {var_to_read} metadata idxs with unit {unit}:")
                print([x for x in data.metadata if data.metadata[x]['var_info'][var_to_read]['units'] == unit])
        data = None

if __name__ == "__main__":
    main()
