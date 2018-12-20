'''
Created on 18.12.2018

@author: hjboehle
'''

class Subscriber:

    def __init__(self, topic, item):
        self.topic = topic
        self.item = item
        
    def subscribe(self, mqtt_client):
        mqtt_client.subscribe(self.topic)
        # TODO
        mqtt_client.message_callback_add(self.topic, self.on_message)
        
    def on_message(self, mqtt_client, userdate, message):
        self.item.act(message.payload)