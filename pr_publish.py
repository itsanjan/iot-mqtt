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
import time
import utils
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.on_publish=on_publish
client.connect("broker.mqttdashboard.com",1883)
client.loop_start()

def push():
    senseOP=utils.loadPayload()
    print(senseOP)
    system      = str(senseOP["System"])
    temperature = int(senseOP["Temperature"])
    (rc, mid) = client.publish("anjan/temperature", temperature, qos=1)
    time.sleep(30)
