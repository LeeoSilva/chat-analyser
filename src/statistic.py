#!/usr/bin/python3
from collections import Counter # Local import 

def getMostSaidWords(words):
    # Returns all the most said words 
    return max(words, key=words.count)

def getMessagePerHour(hour):
    # Returns an value of messages per hour 
    if len(hour) == 0: print("[ERROR] Information 'hour' missing"); return  
    occurances = []
    sum = int(0)
    streak = int(0)
   
    for i in range(len(hour)):
        if hour[i] == hour[i-1]: streak+=1
        elif(streak != 0): occurances.append(streak); streak = int(0)
    
    for i in range(len(occurances)): sum += occurances[i] # Summation of the entire vector 
    return sum / len(occurances)
    
def getMessagePerDay(dates):
    # returns an value of messages per day
    if len(dates) == 0: print("[ERROR] Information 'dates' missing"); return
    occurances = []
    sum = 0 # Used in the summation of the entire vector  
    streak = int(0)
    try:
        for i in range(len(dates)):
            if dates[i] == dates[i-1]: streak+=1 
            elif(streak != 0): occurances.append(streak); streak = int(0)
        for i in range(len(occurances)): sum += occurances[i] # Summation of the entire vector                           
    finally: return (sum / len(occurances)) # Average of messages per day

def getMessagesPerUser(names):
    # Returns the number of times each element in the array appears
    # Obs: Used to get the number of messages each user sended
    if len(names) == 0: print("[ERROR] Information 'names' missing"); return
    return Counter(names) 

def getRepeatedElements(arr):
    # Returns the repeated numbers of an array
    streak = int(1)
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            streak+=1
        else: streak = int(1)
 
def getTotalMessages(names):
    # Returns the total of messages of the entire chat
    if len(names) == 0: print("[ERROR] Information 'names' missing"); return
    return int(len(names))

def getMostSended(names): 
    # Returns the most occured name in a list
    # Obs: Used to get the statistic of the user who most
    # sended messages of the conversaion (The guy who flood everything)
    if len(names) == 0: print("[ERROR] Information 'names' missing"); return
    return Counter(names).most_common(1)
    #print(len(names))
    #return max(names,key=names.count)
 
def getAverageWordLength(words):
    # Returns the average of word lenght of
    # a word vector
    if len(words) == 0: print("[ERROR] Information 'words' missing"); return
    wordLenght = int(0)
    sum = int(0)
    for i in range(len(words)): sum += len(words[i]) # Get the sum of all the characters in the vector
    return sum / len(words)

def getAverageReadTime(words, average=200):
    # The average human reads roughly 200-250 words per/minute 
    # Now considering the wost average (that being 200wpm)
    # This function just returns the average time
    # of the hole file
    return (len(words) / average) / 60 # Converting the time from minutes to hours 
