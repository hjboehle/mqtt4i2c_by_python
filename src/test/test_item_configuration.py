'''
Created on 16.05.2019

@author: hjboehle
'''

import unittest
from mqtt4i2c.item_configuration import ItemConfiguration
import xml.etree.ElementTree as ET

# for this unittest the file 'resources/item_configuration_valid.xml' is necessary

class TestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def runTest(self):

        # for the following unit tests the file 'resources/item_configuration_valid.xml' is necessary
        
        # test method "get_item_xml_configuration_file_name" from class ItemConfiguration
        item_configuration = ItemConfiguration('resources/item_configuration_valid.xml')
        item_xml_configuration_file_name = item_configuration.get_item_xml_configuration_file_name()
        self.assertEqual(item_xml_configuration_file_name, 'resources/item_configuration_valid.xml')
        
        # test method "get_topic" from class ItemConfiguration
        tree = ET.ElementTree(file=item_configuration.get_item_xml_configuration_file_name())
        topic_switch = item_configuration.get_topic(tree, 'Switch')
        self.assertEqual(topic_switch[0], '/house/homeoffice/lamp')
        self.assertEqual(topic_switch[1], '/house/livingroom/fan')
        topic_contact = item_configuration.get_topic(tree, 'Contact')
        self.assertEqual(topic_contact[0], '/house/homeoffice/windowcontact')
        
        # test method "get_i2cdata" from class ItemConfiguration with type "Switch"
        i2cdata_switch = item_configuration.get_i2cdata(tree, 'Switch')
        self.assertEqual(i2cdata_switch[0][1], '1')
        self.assertEqual(i2cdata_switch[1][1], '70')
        self.assertEqual(i2cdata_switch[2][1], '0')
        self.assertEqual(i2cdata_switch[3][1], '25')
        self.assertEqual(i2cdata_switch[4][1], '1')
        self.assertEqual(i2cdata_switch[5][1], '70')
        self.assertEqual(i2cdata_switch[6][1], '0')
        self.assertEqual(i2cdata_switch[7][1], '26')
        # test method "get_i2cdata" from class ItemConfiguration with type "Contact"
        i2cdata_switch = item_configuration.get_i2cdata(tree, 'Contact')
        self.assertEqual(i2cdata_switch[0][1], '1')
        self.assertEqual(i2cdata_switch[1][1], '70')
        self.assertEqual(i2cdata_switch[2][1], '0')
        self.assertEqual(i2cdata_switch[3][1], '27')

        # test method "get_itemstate" from class ItemConfiguration with type "Switch"
        itemstate_switch = item_configuration.get_itemstate(tree, 'Switch', 'On')
        self.assertEqual(itemstate_switch[0], '1')
        self.assertEqual(itemstate_switch[1], '1')
        itemstate_switch = item_configuration.get_itemstate(tree, 'Switch', 'Off')
        self.assertEqual(itemstate_switch[0], '0')
        self.assertEqual(itemstate_switch[1], '0')
        # test method "get_itemstate" from class ItemConfiguration with type "contact"
        itemstate_switch = item_configuration.get_itemstate(tree, 'Contact', 'Open')
        self.assertEqual(itemstate_switch[0], '0')
        itemstate_switch = item_configuration.get_itemstate(tree, 'Contact', 'Closed')
        self.assertEqual(itemstate_switch[0], '1')

        # test method "get_item_switches" from class ItemConfiguration
        item_switches = item_configuration.get_item_switches(tree)
        self.assertEqual(item_switches[0].get_topic(), '/house/homeoffice/lamp')
        self.assertEqual(item_switches[0].get_i2c_bus(), '1')
        self.assertEqual(item_switches[0].get_i2c_address(), '70')
        self.assertEqual(item_switches[0].get_i2c_pmx_channel(), '0')
        self.assertEqual(item_switches[0].get_i2c_pmx_address(), '25')
        self.assertEqual(item_switches[1].get_topic(), '/house/livingroom/fan')
        self.assertEqual(item_switches[1].get_i2c_bus(), '1')
        self.assertEqual(item_switches[1].get_i2c_address(), '70')
        self.assertEqual(item_switches[1].get_i2c_pmx_channel(), '0')
        self.assertEqual(item_switches[1].get_i2c_pmx_address(), '26')

        # test method "get_item_contacts" from class ItemConfiguration
        item_contacts = item_configuration.get_item_contacts(tree)
        self.assertEqual(item_contacts[0].get_topic(), '/house/homeoffice/windowcontact')
        self.assertEqual(item_contacts[0].get_i2c_bus(), '1')
        self.assertEqual(item_contacts[0].get_i2c_address(), '70')
        self.assertEqual(item_contacts[0].get_i2c_pmx_channel(), '0')
        self.assertEqual(item_contacts[0].get_i2c_pmx_address(), '27')
