'''
Created on 18.12.2018

@author: hjboehle
'''

import sys
from mqtt4i2c import outputs
import xml.etree.ElementTree as ET

class I2cConfiguration:

    def __init__(self, i2c_xml_configuration_file_name):
        self.i2c_xml_configuration_file_name = i2c_xml_configuration_file_name
        
    def test(self):
        return self.i2c_xml_configuration_file_name
        
    def get_item_configuration(self, item_type):
        try:
            i2c_configuration = I2cConfiguration('resources/i2c_configuration.xml')
            tree = ET.ElementTree(self.i2c_xml_configuration_file_name)
            if item_type == 'Switch':
                item_configuration = []
                item_configuration.append(i2c_configuration.get_topic(tree, item_type))
                i2cdata = i2c_configuration.get_i2cdata(tree, item_type)
                item_configuration.append(i2cdata[0][1])
                item_configuration.append(i2cdata[1][1])
                item_configuration.append(i2cdata[2][1])
                item_configuration.append(i2cdata[3][1])
                item_configuration.append(i2c_configuration.get_itemstate(tree, item_type, 'On'))
                item_configuration.append(i2c_configuration.get_itemstate(tree, item_type, 'Off'))
            return item_configuration
        except FileNotFoundError as error:
            print(f'XML file not found: {error}')
            print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
            sys.exit(1)
        except:
            print('Unexpected error: ', sys.exc_info()[0])
            print(outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
            sys.exit(1)
        
    def get_topic(self, tree, item_type):
        topic = []
        for elem in tree.iterfind(f".//item[@type='{item_type}']//topic"):
            topic.append([elem.tag, elem.text])
        return topic

    def get_i2cdata(self, tree, item_type):
        i2cdata = []
        for elem in tree.iterfind(f".//item[@type='{item_type}']//i2cdata"):
            for child in elem:
                i2cdata.append([child.tag, child.text])
        return i2cdata

    def get_itemstate(self, tree, item_type, itemstate_type):
        for elem in tree.iterfind(f".//item[@type='{item_type}']//itemstate[@type='{itemstate_type}']"):
            for child in elem:
                if child.tag == 'hex-value':
                    itemstate = child.text
        return itemstate
        
        