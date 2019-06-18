'''
Created on 28.04.2019

@author: hjboehle
'''

import logging
from mqtt4i2c import log_outputs

class LogGenerator:

    def __init__(self, log_list, log_type, logger):
        self.log_list = log_list
        self.log_type = log_type
        self.logger = logger
        
    def generate_lines_logfile(self):
        if self.log_type == 'switch':
            for i in range(0, len(self.log_list)):
                self.logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_SWITCH)
                log_lines = []
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[0] + ': ' + self.log_list[i].get_topic())
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[1] + ': ' + self.log_list[i].get_i2c_bus())
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[2] + ': ' + self.log_list[i].get_i2c_address())
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[3] + ': ' + self.log_list[i].get_i2c_pmx_channel())
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[4] + ': ' + self.log_list[i].get_i2c_pmx_address())
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[5] + ': ' + self.log_list[i].get_value_on())
                log_lines.append(log_outputs.PARAMETERS_ITEM_SWITCHES[6] + ': ' + self.log_list[i].get_value_off())
                for j in range(0, len(log_lines)):
                    self.logger.info(log_lines[j])
                self.logger.info(log_outputs.PROGRAMM_MESSAGE_READY_3)
        elif self.log_type == 'contact':
            for i in range(0, len(self.log_list)):
                self.logger.info(log_outputs.PROGRAMM_MESSAGE_ITEM_CONFIGURATION_READ_CONTACT)
                log_lines = []
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[0] + ': ' + self.log_list[i].get_topic())
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[1] + ': ' + self.log_list[i].get_i2c_bus())
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[2] + ': ' + self.log_list[i].get_i2c_address())
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[3] + ': ' + self.log_list[i].get_i2c_pmx_channel())
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[4] + ': ' + self.log_list[i].get_i2c_pmx_address())
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[5] + ': ' + self.log_list[i].get_value_open())
                log_lines.append(log_outputs.PARAMETERS_ITEM_CONTACTS[6] + ': ' + self.log_list[i].get_value_closed())
                for j in range(0, len(log_lines)):
                    self.logger.info(log_lines[j])
                self.logger.info(log_outputs.PROGRAMM_MESSAGE_READY_3)
