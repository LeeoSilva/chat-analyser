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

def getMostSended(names): 
    # Returns the most occured name in a list
    # Obs: Used to get the statistic of the user who most
    # sended messages of the conversaion (The guy who flood everything)
    return max(names,key=names.count)
