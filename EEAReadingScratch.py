def main():
    from pyaerocom import const
    import pyaerocom.io as pio

    DATA_ID = const.EEA_V2_NAME
    reader = pio.ReadUngridded(DATA_ID)
    od = reader.read(vars_to_retrieve="concpm10")
    print(od)

if __name__ == "__main__":
    main()