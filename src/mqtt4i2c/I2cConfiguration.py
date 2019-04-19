'''
Created on 18.12.2018

@author: hjboehle
'''

import sys
from mqtt4i2c import outputs

class I2cConfiguration:

    def __init__(self, i2c_xml_configuration_file_name):
        self.i2c_xml_configuration_file_name = i2c_xml_configuration_file_name
        
    def get_i2c_xml_configuration_file_name(self):
        return self.i2c_xml_configuration_file_name
        
    def get_item_switch_configurations(self, tree, item_type):
        item_switch_configurations = []
        topic = self.get_topic(tree, item_type)
        i2cdata = self.get_i2cdata(tree, item_type)
        if item_type == 'Switch':
            value_on = self.get_itemstate(tree, item_type, 'On')
            value_off = self.get_itemstate(tree, item_type, 'Off')
            for i in range(0, len(topic)):
                j = i * 3 + i
                item_switch_configuration = (topic[i], i2cdata[j][1], i2cdata[j+1][1], i2cdata[j+2][1], i2cdata[j+3][1], value_on[i], value_off[i])
                item_switch_configurations.append(item_switch_configuration)
        elif item_type == 'Contact':
            value_open = self.get_itemstate(tree, item_type, 'Open')
            value_closed = self.get_itemstate(tree, item_type, 'Closed')
            for i in range(0, len(topic)):
                j = i * 3 + i
                item_switch_configuration = (topic[i], i2cdata[j][1], i2cdata[j+1][1], i2cdata[j+2][1], i2cdata[j+3][1], value_open[i], value_closed[i])
                item_switch_configurations.append(item_switch_configuration)
        return item_switch_configurations
        
    def get_topic(self, tree, item_type):
        topic = []
        for elem in tree.iterfind(f".//item[@type='{item_type}']//topic"):
            topic.append(elem.text)
        return topic

    def get_i2cdata(self, tree, item_type):
        i2cdata = []
        for elem in tree.iterfind(f".//item[@type='{item_type}']//i2cdata"):
            for child in elem:
                i2cdata.append([child.tag, child.text])
        return i2cdata

    def get_itemstate(self, tree, item_type, itemstate_type):
        itemstate = []
        for elem in tree.iterfind(f".//item[@type='{item_type}']//itemstate[@type='{itemstate_type}']"):
            for child in elem:
                if child.tag == 'hex-value':
                    itemstate.append(child.text)#
        return itemstate
        
        