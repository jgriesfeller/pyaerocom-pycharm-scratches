# quick and dirty test for model reading via the api

DATA_ID = 'EMEP.cams61.BASE'
# VAR_NAME = 'ratpm10pm25'
# VAR_NAME = 'concso4'
VAR_NAME = 'SO4ugSm3'
TS_TYPE = 'daily'

def main():
    import pyaerocom.io as pio
    
    model_obj = pio.ReadGridded(data_id = DATA_ID)
    model_data = model_obj.read_var(var_name=VAR_NAME, ts_type=TS_TYPE, rename_var=VAR_NAME)
    print(model_data)

if __name__ == "__main__":
    main()
