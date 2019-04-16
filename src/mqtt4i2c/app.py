'''
Created on 17.12.2018

@author: hjboehle
'''

from mqtt4i2c import settings
from mqtt4i2c.ItemSwitch import ItemSwitch
from mqtt4i2c.I2cConfiguration import I2cConfiguration

def main():
    i2c_configuration = I2cConfiguration(settings.I2C_XML_CONFIGURATION_FILE_NAME)
    
    # configuration switch
    number_of_switches = i2c_configuration.get_number_of_items_per_type('Switch')
    print('number of switches:', number_of_switches)
        
    
    
if __name__ == '__main__':
    main()

