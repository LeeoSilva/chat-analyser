#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys chat.getHour()
from dataHandler import * # Imported file

def printUsage():
    print("Usage: chat-analyser <chat-file>")
    exit()

def getArgFile():
    if len(sys.argv) == 2: return sys.argv[1]
    else: printUsage()

if __name__ == "__main__":
    chat = data(getArgFile())
    chat.getDate()
    messagePerDay = chat.getMessagePerDay()
    chat.getHour()
    


    print("Average of messages send per day by both users: {:.2f}".format(messagePerDay))
