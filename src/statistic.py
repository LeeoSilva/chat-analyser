#!/usr/bin/python3

def getMostSaidWords(words):
    # Returns all the most said words 
    return max(words, key=words.count)

def getMessagePerHour(hour):
    # Returns an value of messages per hour 
    occurances = []
    sum = int(0)
    streak = int(0)

    if hour == None: print("[ERROR] Information missing"); exit() 
   
    for i in range(len(hour)):
        if hour[i] == hour[i-1]: streak+=1
        elif(streak != 0): occurances.append(streak); streak = int(0)
    
    for i in range(len(occurances)): sum += occurances[i] # Summation of the entire vector 
    result = (sum / len(occurances))
    return result
    
def getMessagePerDay(dates):
    # returns an value of messages per day
    occurances = []
    sum = 0 # Used in the summation of the entire vector  
    streak = int(0)
    if dates is None: print("[ERROR] Information missing"); exit()
    try:
        for i in range(len(dates)):
            if dates[i] == dates[i-1]: streak+=1 
            elif(streak != 0): occurances.append(streak); streak = int(0)
        for i in range(len(occurances)): sum += occurances[i] # Summation of the entire vector                           
    finally: return (sum / len(occurances)) # Average of messages per day

def getMessagesPerUser(names):
    # Returns the number of times each element in the array appears
    # Obs: Used to get the number of messages each user sended
    print([[x, names.count(x)] for x in set(names)]) 

def getMostSended(names): 
    # Returns the most occured name in a list
    # Obs: Used to get the statistic of the user who most
    # sended messages of the conversaion (The guy who flood everything)
    return max(names,key=names.count)

def getAverageWordLength(words):
    # Returns the average of word lenght of
    # a word vector

    wordLenght = int(0)
    sum = int(0)

    for i in range(len(words)): sum += len(words[i]) # Get the sum of all the characters in the vector
    return sum / len(words)

def getAverageReadTime(words, average=200):
    # The average human reads roughly 200-250 words per/minute 
    # Now considering the wost average (that being 200wpm)
    # This function just returns the average time
    # of the hole file
    return len(words) / average # Obviously the time is in minutes 
