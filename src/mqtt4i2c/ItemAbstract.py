'''
Created on 18.12.2018

@author: hjboehle
'''

class ItemAbstract(object):

    def __init__(self, i2c_bus, i2c_address, i2c_pmx_channel, i2c_pmx_address):
        self.i2c_bus = i2c_bus
        self.i2c_address = i2c_address
        self.i2c_pmx_channel = i2c_pmx_channel
        self.i2c_pmx_address = i2c_pmx_address

    def perform_action(self, action):
        raise NotImplementedError('to implement by subclass')