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
    #statistic.getRepeatedElements(names)
    #print("Most occured sender: {}".format(statistic.getMostSended(names)))
    print("Average of messages send per day by both users: {:.2f}".format(statistic.getMessagePerDay(date)))
    print("Average of messages send per hour by both users: {:.2f}".format(statistic.getMessagePerHour(hours)))
    print("Average word length: {:.2f} characters".format(statistic.getAverageWordLength(words)))
    print("Average read time of the conversation: {:.2f} hours".format(statistic.getAverageReadTime(words)))
    print("")
    print("Total of {} messages sent".format(statistic.getTotalMessages(names)))
    messagesPerUser   = statistic.getMessagesPerUser(names) 
    for x in messagesPerUser: print("{} sent {} messages in total".format(x,  messagesPerUser[x]))
    sum = int(0)
    mostSended = statistic.getMessagesPerUser(names)
    for i in mostSended: sum += int(mostSended[i])
    print("Total messages sent: {}".format(sum))
