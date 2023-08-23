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
    file="/lustre/storeB/project/aerocom/aerocom1/AEROCOM_OBSDATA/MACC_INSITU_AirNow/202010/2020102323.dat"
    DATA_ID = const.AIR_NOW_NAME

    reader = pio.ReadUngridded(DATA_ID)
    # file_reader = reader.get_lowlevel_reader(DATA_ID)
    # od_file = file_reader.read_file(file, vars_to_retrieve=["vmro3"])
    od = reader.read(vars_to_retrieve="vmro3")
    print(od)

    # ETOPO1_Ice_g_gmt4.grd
if __name__ == "__main__":
    main()