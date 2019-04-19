'''
Created on 03.04.2019

@author: hjboehle
'''
import xml.etree.ElementTree as ET
from mqtt4i2c.I2cConfiguration import I2cConfiguration
#from mqtt4i2c.ItemSwitch import ItemSwitch

types = ['Switch', 'Contact']
i2c_configuration = I2cConfiguration('resources/i2c_configuration.xml')
tree = ET.ElementTree(file='resources/i2c_configuration.xml')
print(types[0])
item_configuration = i2c_configuration.get_item_switch_configuration(tree, types[0])
print(item_configuration)

print('filename:', i2c_configuration.test())

root = tree.getroot()

topic = i2c_configuration.get_topic(tree, types[0])
print(topic)

i2cdata = i2c_configuration.get_i2cdata(tree, types[0])
print(i2cdata)

itemstate = i2c_configuration.get_itemstate(tree, types[0], 'On')
print(itemstate)

itemstate = i2c_configuration.get_itemstate(tree, types[0], 'Off')
print(itemstate)

def get_topic(n, item_type):
    i = 1
    for elem in tree.iterfind(f".//item[@type='{item_type}']//topic"):
        if i == n:
            return elem.text
        i += 1

def get_i2cdata(n, item_type):
    i = 1
    i2cdata = []
    for elem in tree.iterfind(f".//item[@type='{item_type}']//i2cdata"):
        if i == n:
            for child in elem:
                i2cdata.append([child.tag, child.text])
        i += 1
    return i2cdata

def get_itemstate(n, item_type, itemstate_type):
    i = 1
    for elem in tree.iterfind(f".//item[@type='{item_type}']//itemstate[@type='{itemstate_type}']"):
        if i == n:
            for child in elem:
                if child.tag == 'hex-value':
                    itemstate = child.text
                #print(child.tag)
        i += 1
    return itemstate

print('++++++++++++++++++')
print('1. topic:', get_topic(1, 'Switch'))
i2cdata = get_i2cdata(1, 'Switch')
print('1.', i2cdata[0][0], ':', i2cdata[0][1])
print('1.', i2cdata[1][0], ':', i2cdata[1][1])
print('1.', i2cdata[2][0], ':', i2cdata[2][1])
print('1.', i2cdata[3][0], ':', i2cdata[3][1])
print('1. On:', get_itemstate(1, 'Switch', 'On'))
print('1. Off:', get_itemstate(1, 'Switch', 'Off'))
print('++++++++++++++++++')
print('2. topic:', get_topic(2, 'Switch'))
i2cdata = get_i2cdata(2, 'Switch')
print('2.', i2cdata[0][0], ':', i2cdata[0][1])
print('2.', i2cdata[1][0], ':', i2cdata[1][1])
print('2.', i2cdata[2][0], ':', i2cdata[2][1])
print('2.', i2cdata[3][0], ':', i2cdata[3][1])
print('2. On:', get_itemstate(2, 'Switch', 'On'))
print('2. Off:', get_itemstate(2, 'Switch', 'Off'))
print('++++++++++++++++++')
print(get_i2c_configuration(1, 'Switch'))
print(get_i2c_configuration(2, 'Switch'))