# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:57:08 2018

@author: istvan
"""

import paho.mqtt.client as mqtt #import the client1
import cv2

broker_address="18.184.234.183" 
#broker_address="iot.eclipse.org"

def on_publish(mosq, userdata, mid):
    client.loop(5)
    client.disconnect()

client = mqtt.Client("P1") #create new instance
client.username_pw_set(username='istvan', password='kgt6st9')
client.on_publish = on_publish

client.connect(broker_address) #connect to broker
#
cap = cv2.VideoCapture("rtsp://localhost:8554/test")
#
ret, image = cap.read()
cv2.imwrite("frame.jpg", image)   # save frame as JPEG file      
f = open("frame.jpg", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)

client.publish("test_image",byteArr,0)
