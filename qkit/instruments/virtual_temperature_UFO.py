from instrument import Instrument
import instruments
import types
import logging
import numpy as np
from time import sleep
from tip_client import tip_client

class virtual_temperature_UFO(Instrument):
    '''
        this is real hardware connected to the experiment
        add one of those to automatically note its value in the measurement files
    '''

    def __init__(self, name):
        Instrument.__init__(self, name, tags=['virtual'])
        
        self.add_parameter('temperature', type=types.FloatType,
            flags=Instrument.FLAG_GET, units='mK')
        
        self.t = tip_client('tip',address='pi-us74')   #tip raspberry instance
        
    def do_get_temperature(self):
        return round(float(self.t.r_get_T())*1000,2)   #T in mK