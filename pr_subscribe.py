#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------#
# File name: mqtt-sub.py
# Author: Anjan Kumar
# Date created: 14/04/2017
# Date last modified: 15/04/2017
# Python Version: 3.5.2
#-------------------------------#
import paho.mqtt.client as paho
 
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
 
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("anjan/#", qos=1)
 
client.loop_forever()
