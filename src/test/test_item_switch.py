'''
Created on 23.05.2019

@author: hjboehle
'''

import unittest
from mqtt4i2c.item_switch import ItemSwitch

class TestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def runTest(self):
        
        # create an instance from the class ItemSwitch
        item_switch = ItemSwitch('/house/kitchen/radio', '0', '71', '1', '31', '1', '0')

        # test method "get_topic" from class ItemSwitch (comes from abstract class ItemAbstract)
        self.assertEqual(item_switch.get_topic(), '/house/kitchen/radio')

        # test method "get_value_on" from class ItemSwitch
        self.assertEqual(item_switch.get_value_on(), '1')

        # test method "get_value_off" from class ItemSwitch
        self.assertEqual(item_switch.get_value_off(), '0')

        # test method "get_i2c_bus" from class ItemSwitch (comes from abstract class ItemAbstract)
        self.assertEqual(item_switch.get_i2c_bus(), '0')

        # test method "get_i2c_address" from class ItemSwitch (comes from abstract class ItemAbstract)
        self.assertEqual(item_switch.get_i2c_address(), '71')

        # test method "get_i2c_pmx_channel" from class ItemSwitch (comes from abstract class ItemAbstract)
        self.assertEqual(item_switch.get_i2c_pmx_channel(), '1')

        # test method "get_i2c_pmx_address" from class ItemSwitch (comes from abstract class ItemAbstract)
        self.assertEqual(item_switch.get_i2c_pmx_address(), '31')
