'''
Created on 23.05.2019

@author: hjboehle
'''

import unittest
from mqtt4i2c.item_contact import ItemContact

class TestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def runTest(self):
        
        # create an instance from the class ItemContact
        item_contact = ItemContact('/house/hall/doorcontact', '0', '71', '2', '3B', '0', '1')

        # test method "get_topic" from class ItemContact (comes from abstract class ItemAbstract)
        self.assertEqual(item_contact.get_topic(), '/house/hall/doorcontact')

        # test method "get_value_open" from class ItemContact
        self.assertEqual(item_contact.get_value_open(), '0')

        # test method "get_value_closed" from class ItemContact
        self.assertEqual(item_contact.get_value_closed(), '1')

        # test method "get_i2c_bus" from class ItemContact (comes from abstract class ItemAbstract)
        self.assertEqual(item_contact.get_i2c_bus(), '0')

        # test method "get_i2c_address" from class ItemContact (comes from abstract class ItemAbstract)
        self.assertEqual(item_contact.get_i2c_address(), '71')

        # test method "get_i2c_pmx_channel" from class ItemContact (comes from abstract class ItemAbstract)
        self.assertEqual(item_contact.get_i2c_pmx_channel(), '2')

        # test method "get_i2c_pmx_address" from class ItemContact (comes from abstract class ItemAbstract)
        self.assertEqual(item_contact.get_i2c_pmx_address(), '3B')

