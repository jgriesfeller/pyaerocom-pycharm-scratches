import matplotlib.pyplot as plt

import pyaerocom as pya

plt.close("all")

from pyaerocom import const
from pyaerocom.io.read_eea_aqerep_v2 import ReadEEAAQEREP_V2
from pyaerocom.io import ReadUngridded

import tests.conftest



def main():

    DATA_ID = "EEA_AQeRep.v2.Subset"
    VAR_NAME = 'concpm10'

    import pyaerocom.io as pio
    obs_obj = ReadUngridded(DATA_ID)
    lowlevel_reader = obs_obj.get_lowlevel_reader(DATA_ID)
    obs_data1 = obs_obj.read(vars_to_retrieve=VAR_NAME)



if __name__ == "__main__":
    main()