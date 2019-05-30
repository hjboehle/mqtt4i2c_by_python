'''
Created on 17.12.2018

@author: hjboehle
'''

from mqtt4i2c import settings
from mqtt4i2c.item_configuration import ItemConfiguration
import mqtt4i2c.log_generator
from mqtt4i2c import log_outputs
import xml.etree.ElementTree as ET
import sys
import logging

def main():
    # logging configuration
    log_file_name = settings.LOG_FILE_FOLDER + settings.LOG_FILE_NAME
    logger = logging.getLogger('mqtt4i2c.app')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file_name)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info(log_outputs.LOGGING_MESSAGE_LOG_FILE + log_file_name)

    # open the item XML configuration file
    logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_OPEN_XMLFILE)
    try:
        # prepare reading of the configuration
        item_configuration = ItemConfiguration(settings.ITEM_XML_CONFIGURATION_FILE_NAME)
        tree = ET.ElementTree(file=item_configuration.get_item_xml_configuration_file_name())
        # read configuration for the items from the type switch
        logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_SWITCHES)
        item_switches = item_configuration.get_item_switches(tree)
        log_generator_switches = mqtt4i2c.log_generator.LogGenerator(item_switches, 'switch')
        log_generator_switches.generate_lines_logfile()
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_2)
        # read configuration for the items from the type contact
        logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_CONTACTS)
        item_contacts = item_configuration.get_item_contacts(tree)
        log_generator_contacts = mqtt4i2c.log_generator.LogGenerator(item_contacts, 'contact')
        log_generator_contacts.generate_lines_logfile()
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_2)
        # end of reading the configuration
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_1)
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

