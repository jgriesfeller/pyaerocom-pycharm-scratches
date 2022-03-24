def main():
    import matplotlib.pyplot as plt

    plt.close("all")

    from pyaerocom import const
    from pyaerocom.io.read_aeronet_sunv3 import ReadAeronetSunV3
    import pyaerocom.io as pio
    import pyaerocom as pya

    # pya.change_verbosity(new_level='warning', log=pya.logger)
    # reader = ReadAeronetSunV3(const.AERONET_SUN_V3L2_AOD_ALL_POINTS_NAME)
    # od = reader.read_file("/home/jang/MyPyaerocom/testdata-minimal/obsdata/AeronetSunV3Lev2.0.AP/renamed/19930101_20211120_Zvenigorod.lev20")
    # print(od)
    DATA_ID = const.EBAS_MULTICOLUMN_NAME
    reader = pio.ReadUngridded(DATA_ID)
    vars_to_cache = ["concCocpm25", "concso4", "SO4ugSm3"]
    vars_to_cache = [
        # "concso4pm25",
        # "concso4pm10",
        # "concso2",
        # "concbc",
        # "concoa",
        # "concoc",
        # "conctc",
        # "concno2",
        # "concno3",
        # "concnh3",
        # "concnh4",
        # "wetso4",
        # "concso4pr",
    ]

    # data = reader.read(vars_to_retrieve="concCocpm25")
    for var_to_read in vars_to_cache:
        data = reader.read(vars_to_retrieve=var_to_read)
        print(f"# of unique stations: {len(data.unique_station_names)}")
        print(data)

    # ETOPO1_Ice_g_gmt4.grd


if __name__ == "__main__":
    main()
