#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys # For executable arguments
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
    chat    = data(getArgFile())
    date    = chat.getDate()
    hours   = chat.getHour()
    names   = chat.getNames()
    content = chat.getMessageContent()
    words   = chat.getWords()
    #vectorMath.getRepeatedElements()
    messagePerDay  = statistic.getMessagePerDay(date)
    messagePerHour = statistic.getMessagePerHour(hours)
    averageWordLength =  statistic.getAverageWordLength(words)
    messagesPerUser   =  statistic.getMessagesPerUser(names) 
    averageReadTime   =  statistic.getAverageReadTime(words)
   # print("Most occured sender: {}".format(statistic.getMostSended(names)))
    print("Average of messages send per day by both users: {:.2f}".format(messagePerDay))
    print("Average of messages send per hour by both users: {:.2f}".format(messagePerHour))
    print("Average word length: {:.2f} characters".format(averageWordLength))
    print("Average read time of the conversation: {:.2f} hours".format(averageReadTime))
    print("")
    for x in messagesPerUser: print("{} sent {} messages in total".format(x,  messagesPerUser[x]))

