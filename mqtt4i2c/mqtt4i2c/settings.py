'''
Created on 18.12.2018

@author: hjboehle
'''

# XML schema file to validate the item configuration XML file
ITEM_CONFIGURATION_XML_SCHEMA_FILE = 'resources/item_configuration.xsd'

# XML Namespace for the item configuration XML file
ITEM_CONFIGURATION_XML_FILE_NAMESPACE = 'http://www.github.com/hjboehle/mqtt4i2c'

# hostname or IP-address of the MQTT-Broker
BROKER_HOST = 'localhost'

# port of the MQTT-Broker
BROKER_PORT = '1883'

# Client ID of the I2C-MQTT-Client
CLIENT_ID = 'MQTT2I2C'

# Configuration-XML-File of the I2C-MQTT-Client
ITEM_XML_CONFIGURATION_FILE_NAME = 'resources/item_configuration.xml'
#I2C_XML_CONFIGURATION_FILE_NAME = 'resources/i2c_configuration_.xml' # file not available
#I2C_XML_CONFIGURATION_FILE_NAME = 'resources/i2c_configuration_corrupt.xml' # xml file contains text but not xml

# logfile folder
LOG_FILE_FOLDER = '/home/hjboehle/.mqtt4i2c/logs/'

# logfile name
LOG_FILE_NAME = 'mqtt4i2c'