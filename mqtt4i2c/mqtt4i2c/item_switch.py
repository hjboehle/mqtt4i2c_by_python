'''
Created on 18.12.2018

@author: hjboehle
'''

from mqtt4i2c.item_abstract import ItemAbstract

class ItemSwitch(ItemAbstract):

    def __init__(self, topic, i2c_bus, i2c_address, i2c_pmx_channel, i2c_pmx_address, value_on, value_off):
        super().__init__(topic, i2c_bus, i2c_address, i2c_pmx_channel, i2c_pmx_address)
        self.value_on = value_on
        self.value_off = value_off
        
    def perform_action(self, action):
        if action == 'Switch On':
            print('Switch On')
        elif action == 'Switch Off':
            print('Switch Off')
        else:
            print('unsupported action')
            
    def get_value_on(self):
        return self.value_on
            
    def get_value_off(self):
        return self.value_off
