#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DATA_ID = "EBASMC"
# VAR_NAME = 'concpm10'
# VAR_NAME = 'conco3'
# VAR_NAME = 'concso4'
VAR_NAME = "vmro3"


def main():
    import pyaerocom.io as pio

    obs_obj = pio.ReadUngridded(DATA_ID)
    obs_data = obs_obj.read(vars_to_retrieve=VAR_NAME)
    print(obs_data)


if __name__ == "__main__":
    main()
