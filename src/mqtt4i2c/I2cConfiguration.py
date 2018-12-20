'''
Created on 18.12.2018

@author: hjboehle
'''

import sys
import xml.dom.minidom as minidom
from mqtt4i2c import outputs

class I2cConfiguration:

    def __init__(self, i2c_xml_configuration_file_name):
        self.i2c_xml_configuration_file_name = i2c_xml_configuration_file_name
        
    def get_mqtt_configuration(self):
        try:
            xml_document = minidom.parse(self.i2c_xml_configuration_file_name)
            item = xml_document.getElementsByTagName('item')
            number_of_items_subscribe = 0
            number_of_items_publish = 0
            for items in item:
                pattern = items.getAttribute('pattern')
                if pattern == 'subscribe':
                    number_of_items_subscribe += 1
                elif pattern == 'publish':
                    number_of_items_publish += 1
            mqtt_configuration = (number_of_items_subscribe, number_of_items_publish)
            return mqtt_configuration
        except FileNotFoundError as error:
            print(f'XML file not found: {error}')
            print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
            sys.exit(1)
        except:
            print('Unexpected error: ', sys.exc_info()[0])
            print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
            sys.exit(1)
        
        
        