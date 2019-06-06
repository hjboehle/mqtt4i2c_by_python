'''
Created on 27.04.2019

@author: hjboehle
'''
# Messages about the logging configuration
LOGGING_MESSAGE_LOG_FILE = 'logfile: '

# Message about the reading of the item configuration
PROGRAMM_MESSAGE_ITEM_CONFIGURATION_VALID_XMLFILE = 'validate the item configuration xml file against the xml schema ...'
PROGRAMM_MESSAGE_ITEM_CONFIGURATION_OPEN_XMLFILE = 'read the configuration of the items ...'
PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_SWITCHES = '   read the configuration of the switches ... '
PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_CONTACTS = '   read the configuration of the contacts ...'
PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_SWITCH = '      read the configuration of a switch ... '
PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_CONTACT = '      read the configuration of a contact ...'
PROGRAMM_MESSAGE_READY_1 = '... ready'
PROGRAMM_MESSAGE_READY_2 = '   ... ready'
PROGRAMM_MESSAGE_READY_3 = '      ... ready'

# Message about an termination of the program after an error
PROGRAM_ERROR_NOT_VALID_ITEM_CONFIGURATION_XMLFILE = 'item configuration xml file is not valid'
PROGRAM_ERROR_XML_FILE_NOT_FOUND_ERROR = 'unexpected error:'
PROGRAM_ERROR_UNEXPECTED_ERROR = 'XML file not found'
PROGRAM_ERROR_TERMINATION_MESSAGE = 'Program will now be terminated'

# parameter lists for the class LogGenerator
PARAMETERS_ITEM_SWITCHES = []
PARAMETERS_ITEM_SWITCHES.append('         topic')
PARAMETERS_ITEM_SWITCHES.append('         i2c bus')
PARAMETERS_ITEM_SWITCHES.append('         i2c address')
PARAMETERS_ITEM_SWITCHES.append('         i2c pmx channel')
PARAMETERS_ITEM_SWITCHES.append('         i2c pmx address')
PARAMETERS_ITEM_SWITCHES.append('         value on')
PARAMETERS_ITEM_SWITCHES.append('         value off')

PARAMETERS_ITEM_CONTACTS = []
PARAMETERS_ITEM_CONTACTS.append('         topic')
PARAMETERS_ITEM_CONTACTS.append('         i2c bus')
PARAMETERS_ITEM_CONTACTS.append('         i2c address')
PARAMETERS_ITEM_CONTACTS.append('         i2c pmx channel')
PARAMETERS_ITEM_CONTACTS.append('         i2c pmx address')
PARAMETERS_ITEM_CONTACTS.append('         value open')
PARAMETERS_ITEM_CONTACTS.append('         value closed')
