# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:20:28 2018

@author: istvan
"""

import paho.mqtt.client as mqtt #import the client1
import time

broker_address="18.185.85.228" 
#broker_address="iot.eclipse.org"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

client = mqtt.Client("P1") #create new instance
client.username_pw_set(username='', password='')
client.on_message = on_message
client.connect(broker_address) #connect to broker

client.loop_start()
client.subscribe("test_button")
time.sleep(5)
client.loop_stop()

