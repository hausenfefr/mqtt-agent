#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import paho.mqtt.subscribe as subscribe

def inmsg(client, userdata, message):

    if message.topic == "/runner":
        if message.payload == "stats":
            os.startfile('stats.lnk')
        if message.payload == "web":
            os.startfile('web.url')
        if message.payload == "calc":
            os.startfile('calc')
        if message.payload == "notepad":
            os.startfile('notepad')
        if message.payload == "paint":
            os.startfile('mspaint')
        if message.payload == "exit":
            os._exit(1)
            
subscribe.callback(inmsg, "#", hostname="hausenfefr.com")

