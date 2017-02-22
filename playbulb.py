#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ver 0.0.1
import subprocess
class Playbulb():
    def __init__(self,adress):
        self.adress=adress
        
    def getColor(self):
        cmd = 'gatttool -b {} --char-read -a 0x0018'.format(self.adress)
        try:
            x = subprocess.check_output(cmd.split(" "))
            color = [int(x[33:35],16),int(x[36:38],16),int(x[39:41],16),int(x[42:44],16)]
        except subprocess.CalledProcessError:
            color = [0,0,0,0]
        return color
    def setColor(self,color):
        cmd = 'gatttool -b {} --char-write -a 0x0018 -n {}'.format(self.adress,color)
        x = subprocess.check_output(cmd.split(" "))