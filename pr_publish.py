#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho
import time
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.on_publish=on_publish
client.connect("broker.mqttdashboard.com",1883)
client.loop_start()
 
while True:
    temperature = int(71)
    (rc, mid) = client.publish("anjan/temperature", str(temperature), qos=1)
    time.sleep(30)
