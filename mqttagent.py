#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import paho.mqtt.subscribe as subscribe

def inmsg(client, userdata, message):

    if message.topic == "/run":
        
        if message.payload == "exit":
            os._exit(1)
        if os.path.isfile(message.payload + '.bat'):
            os.startfile(message.payload + '.bat')
        if os.path.isfile(message.payload + '.lnk'):
            os.startfile(message.payload + '.lnk')
        if os.path.isfile(message.payload + '.url'):
            os.startfile(message.payload + '.url')
            
subscribe.callback(inmsg, "#", hostname="hausenfefr.com")

