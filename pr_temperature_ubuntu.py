#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------#
# File name: temp.py
# Author: Anjan Kumar
# Date created: 14/04/2017
# Date last modified: 15/04/2017
# Python Version: 3.5.2
#-------------------------------#
import utils
#alt sensors bash
# import re
# import subprocess
#
# sensors = subprocess.check_output("sensors")
# print(sensors)
# temperatures={match[0]: float(match[1]) for match in re.findall("^(.?)\:\s+\+?(.*?)°C", sensors, re.MULTILINE)}
#using lib
from pyspectator.processor import Cpu
from time import sleep
cpu = Cpu(monitoring_latency=1)
systemName="Lenovo L420"

def Log():
    print (cpu.temperature)
    senseData = {   'Temperature'   :cpu.temperature,
                    'System'        :systemName
                }
    utils.makePayload(senseData)
    sleep(1)

