#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys, os 
import matplotlib.pyplot as plt
from dataHandler import *

def printUsage():
    print("Usage: chat-analyser <chat-file>")
    exit()

def getArgFile():
    if len(sys.argv) == 2: return sys.argv[1]
    else: printUsage()

if __name__ == "__main__":
    chat = data(getArgFile())
    chat.getDate()
    chat.getMessagePerDay()
    chat.getHour()
