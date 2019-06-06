'''
Created on 04.06.2019

@author: hjboehle
'''

import unittest
from mqtt4i2c.item_configuration import ItemConfiguration

class TestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def runTest(self):
        
        # Validation of the XML item configuration against the XML schema (XML file is valid)
        item_configuration = ItemConfiguration('resources/item_configuration_valid.xml')
        self.assertEqual(item_configuration.validate_item_xml_configuration_file('../mqtt4i2c/resources/item_configuration.xsd'), True)

        # Validation of the XML item configuration against the XML schema (XML file is not valid)
        item_configuration = ItemConfiguration('resources/item_configuration_corrupt.xml')
        self.assertEqual(item_configuration.validate_item_xml_configuration_file('../mqtt4i2c/resources/item_configuration.xsd'), False)
