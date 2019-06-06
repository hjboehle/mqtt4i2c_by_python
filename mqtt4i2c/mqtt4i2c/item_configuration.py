'''
Created on 18.12.2018

@author: hjboehle
'''

from mqtt4i2c.item_switch import ItemSwitch
from mqtt4i2c.item_contact import ItemContact
from mqtt4i2c import settings
import xmlschema

class ItemConfiguration:

    def __init__(self, item_xml_configuration_file_name):
        self.item_xml_configuration_file_name = item_xml_configuration_file_name
        
    def get_item_xml_configuration_file_name(self):
        return self.item_xml_configuration_file_name
    
    # method to validate the item configuration xml file against the xml schema
    def validate_item_xml_configuration_file(self, xml_schema_file_name):
        xsd = xmlschema.XMLSchema(xml_schema_file_name)
        if xsd.is_valid(self.item_xml_configuration_file_name):
            valid_item_configuration_xml_file = True
        else:
            valid_item_configuration_xml_file = False
        return (valid_item_configuration_xml_file)

    def get_item_switches(self, tree, name_space):
        item_switches = []
        item_type = 'Switch'
        topic = self.get_topic(tree, item_type, name_space)
        i2cdata = self.get_i2cdata(tree, item_type, name_space)
        value_on = self.get_itemstate(tree, item_type, 'On', name_space)
        value_off = self.get_itemstate(tree, item_type, 'Off', name_space)
        for i in range(0, len(topic)):
            j = i * 3 + i
            item_switch = ItemSwitch(topic[i], i2cdata[j][1], i2cdata[j+1][1], i2cdata[j+2][1], i2cdata[j+3][1], value_on[i], value_off[i])
            item_switches.append(item_switch)
        return item_switches

    def get_item_contacts(self, tree, name_space):
        item_contacts = []
        item_type = 'Contact'
        topic = self.get_topic(tree, item_type, name_space)
        i2cdata = self.get_i2cdata(tree, item_type, name_space)
        value_open = self.get_itemstate(tree, item_type, 'Open', name_space)
        value_closed = self.get_itemstate(tree, item_type, 'Closed', name_space)
        for i in range(0, len(topic)):
            j = i * 3 + i
            item_contact = ItemContact(topic[i], i2cdata[j][1], i2cdata[j+1][1], i2cdata[j+2][1], i2cdata[j+3][1], value_open[i], value_closed[i])
            item_contacts.append(item_contact)
        return item_contacts

    def get_topic(self, tree, item_type, name_space):
        topic = []
        for elem in tree.iterfind(f".//ns:item[@type='{item_type}'][@active='yes']//ns:topic", name_space):
            topic.append(elem.text)
        return topic

    def get_i2cdata(self, tree, item_type, name_space):
        i2cdata = []
        for elem in tree.iterfind(f".//ns:item[@type='{item_type}'][@active='yes']//ns:i2cdata", name_space):
            for child in elem:
                i2cdata.append([child.tag, child.text])
        return i2cdata

    def get_itemstate(self, tree, item_type, itemstate_type, name_space):
        itemstate = []
        for elem in tree.iterfind(f".//ns:item[@type='{item_type}'][@active='yes']//ns:itemstate[@type='{itemstate_type}']", name_space):
            for child in elem:
                if child.tag == '{' + name_space['ns'] + '}' 'hex-value':
                    itemstate.append(child.text)#
        return itemstate
