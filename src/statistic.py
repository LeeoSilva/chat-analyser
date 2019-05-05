#!/usr/bin/python3

def getMessagePerHour(hour)
    # Returns an value of messages per hour 
    occurances = []
    sum = int(0)
    streak = int(0)

    if hour == None: print("[ERROR] Information missing"); exit() 
   
    for i in range(len(hour)):
        if hour[i] == hour[i-1]: streak+=1
        elif(streak != 0): occurances.append(streak); streak = int(0)
    
    for i in range(len(occurances)): sum += occuraces[i] # Summation of the entire vector 
    result = (sum / len(occurances))
    print("Average of messages per hour: {}".format(result))
    return result
    
def getMessagePerDay(dates):
    # returns an value of messages per day
    occurances = []
    sum = 0
    streak = int(0)

    if dates == None: print("[ERROR] Information missing"); exit()
    for i in range(len(dates)):
        if dates[i] == dates[i-1]: streak+=1 
        elif(streak != 0): occurances.append(streak); streak = int(0)

    for i in range(len(occurances)): sum += occurances[i] # Summation of the entire vector  
    result = (sum / len(occurances)) # Average of messages per day
    return result
