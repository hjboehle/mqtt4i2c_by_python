'''
Created on 17.12.2018

@author: hjboehle
'''

from mqtt4i2c import settings
from mqtt4i2c.ItemSwitch import ItemSwitch
from mqtt4i2c.I2cConfiguration import I2cConfiguration
import sys
from mqtt4i2c import outputs
import xml.etree.ElementTree as ET

def main():
    # open the I2C XML configuration file
    try:
        i2c_configuration = I2cConfiguration(settings.I2C_XML_CONFIGURATION_FILE_NAME)
        tree = ET.ElementTree(file=i2c_configuration.get_i2c_xml_configuration_file_name())
    except FileNotFoundError as error:
        print(f'XML file not found: {error}')
        print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    except:
        print('Unexpected error: ', sys.exc_info()[0])
        print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    
    # read configuration for the items from the type switch
    item_switch_configurations = i2c_configuration.get_item_switch_configurations(tree, 'Switch')
    print('item_switch_configurations:', item_switch_configurations)
    
    # read configuration for the items from the type contact
    item_switch_configurations = i2c_configuration.get_item_switch_configurations(tree, 'Contact')
    print('item_switch_configurations:', item_switch_configurations)
    
if __name__ == '__main__':
    main()

