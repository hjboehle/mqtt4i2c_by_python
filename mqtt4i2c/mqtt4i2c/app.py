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
import log_generator

def main():
    # logging configuration
    log_file_name = settings.LOG_FILE_FOLDER + settings.LOG_FILE_NAME
    logger = logging.getLogger('mqtt4i2c')#.getChild('.app')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file_name)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s --> module: %(module)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info(log_outputs.LOGGING_MESSAGE_LOG_FILE + log_file_name)

    # validate the item XML configuration file against the xml schema
    logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_VALID_XMLFILE)
    item_configuration = ItemConfiguration(settings.ITEM_XML_CONFIGURATION_FILE_NAME)
    valid_item_configuration_xml_file = item_configuration.validate_item_xml_configuration_file(settings.ITEM_CONFIGURATION_XML_SCHEMA_FILE)
    if valid_item_configuration_xml_file == True:
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_1)
    else:
        logger.info(log_outputs.PROGRAM_ERROR_NOT_VALID_ITEM_CONFIGURATION_XMLFILE)
        logger.info(log_outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        exit(1)

    # open the item XML configuration file
    logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_OPEN_XMLFILE)
    try:
        # prepare reading of the configuration
        tree = ET.ElementTree(file=item_configuration.get_item_xml_configuration_file_name())
        name_space = {'ns': settings.ITEM_CONFIGURATION_XML_FILE_NAMESPACE}
        # read configuration for the items from the type switch
        logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_SWITCHES)
        item_switches = item_configuration.get_item_switches(tree, name_space)
        log_generator_switches = mqtt4i2c.log_generator.LogGenerator(item_switches, 'switch', logger)
        log_generator_switches.generate_lines_logfile()
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_2)

        # read configuration for the items from the type contact
        logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_CONTACTS)
        item_contacts = item_configuration.get_item_contacts(tree, name_space)
        log_generator_contacts = mqtt4i2c.log_generator.LogGenerator(item_contacts, 'contact', logger)
        log_generator_contacts.generate_lines_logfile()
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_2)
        # end of reading the configuration
        logger.info(log_outputs.PROGRAMM_MESSAGE_READY_1)
    except FileNotFoundError as error:
        logger.error(log_outputs.PROGRAM_ERROR_XML_FILE_NOT_FOUND_ERROR)
        logger.error(error)
        logger.error(log_outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)
    except:
        logger.error(log_outputs.PROGRAM_ERROR_UNEXPECTED_ERROR)
        logger.error(sys.exc_info()[0])
        logger.error(log_outputs.PROGRAM_ERROR_TERMINATION_MESSAGE)
        sys.exit(1)

if __name__ == '__main__':
    main()

