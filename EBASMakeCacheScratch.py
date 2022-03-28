def main():
    from pyaerocom import const
    import pyaerocom.io as pio
    import pyaerocom as pya

    # DATA_ID = const.EBAS_MULTICOLUMN_NAME
    DATA_ID = const.EEA_NRT_NAME
    reader = pio.ReadUngridded(DATA_ID)
    vars_to_cache = [
        # "concso4pm25",
        # "concso4pm10",
        # "concpm10",
        # "concpm25",
        # "concso2",
        # "concso4",
        # "concbc",
        # "concoa",
        "concoc",
        # "conctc",
        # "concno2",
        # "concno3",
        # "concnh3",
        # "concnh4",
        # "wetso4",
        # "concso4pr",
    ]

    for var_to_read in vars_to_cache:
        data = reader.read(vars_to_retrieve=var_to_read)
        print(f"# of unique stations: {len(data.unique_station_names)}")
        print(data)

if __name__ == "__main__":
    main()
