#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------#
# File name: mqtt-sub.py
# Author: Anjan Kumar
# Date created: 14/04/2017
# Date last modified: 15/04/2017
# Python Version: 3.5.2
#-------------------------------#
import pr_temperature_ubuntu
import pr_publish

def main():
    pr_temperature_ubuntu.Log()
    pr_publish.push()

if __name__=="__main__":
    main()
