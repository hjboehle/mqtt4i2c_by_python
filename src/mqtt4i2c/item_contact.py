'''
Created on 22.04.2019

@author: hjboehle
'''

from mqtt4i2c.item_abstract import ItemAbstract

class ItemContact(ItemAbstract):

    def __init__(self, topic, i2c_bus, i2c_address, i2c_pmx_channel, i2c_pmx_address, value_open, value_closed):
        super().__init__(topic, i2c_bus, i2c_address, i2c_pmx_channel, i2c_pmx_address)
        self.value_open = value_open
        self.value_closed = value_closed
        
    def perform_action(self, action):
        if action == 'Switch On':
            print('Switch On')
        elif action == 'Switch Off':
            print('Switch Off')
        else:
            print('unsupported action')
            
    def get_value_open(self):
        return self.value_open
            
    def get_value_closed(self):
        return self.value_closed
