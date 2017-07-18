#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import paho.mqtt.subscribe as subscribe

def inmsg(client, userdata, message):

    if message.topic == "/runner":
        if message.payload == "stats":
            print("%s : %s" % (message.topic, message.payload))
            os.startfile('stats.lnk')
        if message.payload == "web":
            print("%s : %s" % (message.topic, message.payload))
            os.startfile('web.url')
        if message.payload == "calc":
            print("%s : %s" % (message.topic, message.payload))
            os.startfile('calc')
        if message.payload == "notepad":
            print("%s : %s" % (message.topic, message.payload))
            os.startfile('notepad')
        if message.payload == "paint":
            print("%s : %s" % (message.topic, message.payload))
            os.startfile('mspaint')
        if message.payload == "exit":
            print("%s : %s" % (message.topic, message.payload))
            os._exit(1)
            
print("waiting...")
subscribe.callback(inmsg, "#", hostname="hausenfefr.com")

