#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This shows an example of using the subscribe.callback helper function.

import os
import paho.mqtt.subscribe as subscribe

def print_msg(client, userdata, message):

    if message.topic == "/runner":
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
subscribe.callback(print_msg, "#", hostname="hausenfefr.com")

