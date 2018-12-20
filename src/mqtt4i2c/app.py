'''
Created on 17.12.2018

@author: hjboehle
'''

from mqtt4i2c import settings
from mqtt4i2c.ItemSwitch import ItemSwitch
from mqtt4i2c.I2cConfiguration import I2cConfiguration

def main():
    i2c_configuration = I2cConfiguration(settings.I2C_XML_CONFIGURATION_FILE_NAME)
    mqtt_configuration = i2c_configuration.get_mqtt_configuration()
    number_of_items_subscribe = mqtt_configuration[0]
    number_of_items_publish = mqtt_configuration[1]
    print('number of items to subscribe:', number_of_items_subscribe)
    print('number of items to publish:', number_of_items_publish)
    
    item_switch = ItemSwitch('1', '70', '0', '27', '1', '0')
    print('item_switch - i2cbus: ', item_switch.i2c_bus)
    
if __name__ == '__main__':
    main()

