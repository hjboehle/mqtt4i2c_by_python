'''
Created on 17.12.2018

@author: hjboehle
'''

from mqtt4i2c import settings
from mqtt4i2c.ItemConfiguration import ItemConfiguration
from mqtt4i2c.LogGenerator import LogGenerator
import sys
import logging
from mqtt4i2c import log_outputs
import xml.etree.ElementTree as ET

logging.basicConfig(level = logging.DEBUG)
#logging.basicConfig(filename = 'debug.log')

def main():
    # open the item XML configuration file
    logging.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_OPEN_XMLFILE)
    try:
        # prepare reading of the configuration
        item_configuration = ItemConfiguration(settings.ITEM_XML_CONFIGURATION_FILE_NAME)
        tree = ET.ElementTree(file=item_configuration.get_item_xml_configuration_file_name())
        # read configuration for the items from the type switch
        logging.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_SWITCHES)
        item_switches = item_configuration.get_item_switches(tree)
        LogGenerator(item_switches, 'switch').generate_lines_logfile()
        logging.info(log_outputs.PROGRAMM_MESSAGE_READY_2)
        # read configuration for the items from the type contact
        logging.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_CONTACTS)
        item_contacts = item_configuration.get_item_contacts(tree)
        LogGenerator(item_contacts, 'contact').generate_lines_logfile()
        logging.info(log_outputs.PROGRAMM_MESSAGE_READY_2)
        # end of reading the configuration
        logging.info(log_outputs.PROGRAMM_MESSAGE_READY_1)
    except FileNotFoundError as error:
        print(f'XML file not found: {error}')
        print(log_outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    except:
        print('Unexpected error: ', sys.exc_info()[0])
        print(log_outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    
    
if __name__ == '__main__':
    main()

