#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------#
# File name: mqtt-sub.py
# Author: Anjan Kumar
# Date created: 14/04/2017
# Date last modified: 15/04/2017
# Python Version: 3.5.2
#-------------------------------#
import threading

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        if self.threadID==1: Thread1_pub()
        if self.threadID==2: Thread2_log()
def Thread1_pub():
    print("Thread 1 : up")
    import pr_publish
    pr_publish
def Thread2_log():
    print("Thread 2 : up")
    import pr_temperature_ubuntu
    pr_temperature_ubuntu

def main():
    thread1=myThread(1, "Thread-1", 1)
    thread2=myThread(2, "Thread-2", 1)
    thread1.start()
    thread2.start()

main()
