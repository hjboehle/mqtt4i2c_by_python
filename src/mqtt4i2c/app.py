'''
Created on 17.12.2018

@author: hjboehle
'''

from mqtt4i2c import settings
from mqtt4i2c.ItemConfiguration import ItemConfiguration
import sys
from mqtt4i2c import outputs
import xml.etree.ElementTree as ET

def main():
    # open the item XML configuration file
    try:
        item_configuration = ItemConfiguration(settings.ITEM_XML_CONFIGURATION_FILE_NAME)
        tree = ET.ElementTree(file=item_configuration.get_item_xml_configuration_file_name())
    except FileNotFoundError as error:
        print(f'XML file not found: {error}')
        print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    except:
        print('Unexpected error: ', sys.exc_info()[0])
        print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    
    # read configuration for the items from the type switch
    item_switches = item_configuration.get_item_switches(tree)
    for i in range(0, len(item_switches)):
        item_switch = item_switches[i]
        print('item_switch_topic', i, ':', item_switch.get_topic())
        print('item_switch_i2c_bus', i, ':', item_switch.get_i2c_bus())
        print('item_switch_i2c_address', i, ':', item_switch.get_i2c_address())
        print('item_switch_i2c_pmx_channel', i, ':', item_switch.get_i2c_pmx_channel())
        print('item_switch_i2c_pmx_address', i, ':', item_switch.get_i2c_pmx_address())
        print('item_switch_value_on', i, ':', item_switch.get_value_on())
        print('item_switch_value_on', i, ':', item_switch.get_value_off())
    
    # read configuration for the items from the type contact
    item_contacts = item_configuration.get_item_contacts(tree)
    for i in range(0, len(item_contacts)):
        item_contact = item_contacts[i]
        print('item_contact_topic', i, ':', item_contact.get_topic())
        print('item_contact_i2c_bus', i, ':', item_contact.get_i2c_bus())
        print('item_contact_i2c_address', i, ':', item_contact.get_i2c_address())
        print('item_contact_i2c_pmx_channel', i, ':', item_contact.get_i2c_pmx_channel())
        print('item_contact_i2c_pmx_address', i, ':', item_contact.get_i2c_pmx_address())
        print('item_switch_value_open', i, ':', item_contact.get_value_open())
        print('item_switch_value_closed', i, ':', item_contact.get_value_closed())
    
if __name__ == '__main__':
    main()

