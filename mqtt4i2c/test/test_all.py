'''
Created on 04.06.2019

@author: hjboehle
'''

import unittest
import test.test_item_configuration_xml_file
import test.test_item_configuration
import test.test_item_contact
import test.test_item_switch

 
suite = unittest.TestSuite()
suite.addTest(test.test_item_configuration_xml_file.TestCase())
suite.addTest(test.test_item_configuration.TestCase())
suite.addTest(test.test_item_contact.TestCase())
suite.addTest(test.test_item_switch.TestCase())

runner = unittest.TextTestRunner()
testresult = runner.run(suite)

if not testresult.wasSuccessful():
    exit(1)