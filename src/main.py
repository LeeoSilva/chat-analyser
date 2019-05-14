#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from dataHandler import * # Imported file
import vectorMath # Imported file 
import statistic # imported file 

def printUsage():
    print("Usage: chat-analyser <chat-file>")
    exit()

def getArgFile():
    if len(sys.argv) == 2: return sys.argv[1]
    else: printUsage()

if __name__ == "__main__":
    chat  = data(getArgFile())
    date  = chat.getDate()
    hours = chat.getHour()
    names = chat.getNames()
    words = chat.getWords()
    messagePerDay  = statistic.getMessagePerDay(date)
    messagePerHour = statistic.getMessagePerHour(hours)
    content = chat.getMessageContent()
    #vectorMath.getRepeatedElements()
    averageWordLength =  statistic.getAverageWordLength(words)
    averageReadTime   =  statistic.getAverageReadTime(words)
    messagesPerUser   =  statistic.getMessagesPerUser(names) 
    print("Most occured sender: {}".format(statistic.getMostSended(names)))
    print("Average of messages send per day by both users: {:.2f}".format(messagePerDay))
    print("Average of messages send per hour by both users: {:.2f}".format(messagePerHour))
    print("Average word length: {:.2f}".format(averageWordLength))
    print("Average read time of the conversation: {:.2f} minutes".format(averageReadTime))
