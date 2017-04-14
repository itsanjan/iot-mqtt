#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------#
# File name: temp.py
# Author: Anjan Kumar
# Date created: 14/04/2017
# Date last modified: 15/04/2017
# Python Version: 3.5.2
#-------------------------------#
import json
def makePayload(data):
    with open('data.txt', 'w') as f:
      json.dump(data, f, ensure_ascii=False)
def loadPayload():
    with open('data.txt', 'r') as f:
        data=json.load(f)
    return data
