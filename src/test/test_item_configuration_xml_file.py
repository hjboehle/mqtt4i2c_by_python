'''
Created on 04.06.2019

@author: hjboehle
'''

import unittest
import xmlschema
from mqtt4i2c.item_configuration import ItemConfiguration

class TestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def runTest(self):
        
        # Validation of the XML item configuration against the XML schema (XML file is valid)
        item_configuration = ItemConfiguration('resources/item_configuration_valid.xml')
        item_xml_configuration_file_name = item_configuration.get_item_xml_configuration_file_name()
        xml_schema_file_name = 'mqtt4i2c/item_configuration.xsd'
        # !!!!Note: once the method validate_item_configuration_xml-file is ready !!!!
        
