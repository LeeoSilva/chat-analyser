#!/usr/bin/python3


# The data should be formated in the following setting to be data mined:  
# (The default format of WhatsApp export chat function) 
#
# Day/Mouth/Year, Hour:Minute Period - Name: Message
#
# For example:
# 4/6/18, 11:12 AM - Looh: Oi, tudo bem? 
# 4/6/18, 11:13 AM - Leonardo: tudo, e vc? 

import re # Regular expression library

class data:
    chat = 0
    primaryChat = []
    secondaryChat = []
    dates = []


    def __init__(self, textfile):
        # Receives a .txt file as a input 
        with open(textfile, 'r') as f: self.chat = f.readlines()


    def getDate(self):
        # returns 
        actualTime = ""
        date = []
        for lines in self.chat:
            actualTime = re.findall('^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}\, ', lines.rstrip())
            self.dates.append(actualTime) 
        return self.dates

    def getMessagePerDay(self):
        # returns an value of messages per day
        occurances = []
        sum = 0
        streak = int(0)

        if self.dates == None:
            print("cant get messages per day")
            exit()

        for i in range(len(self.dates)):
            if self.dates[i] == self.dates[i-1]: streak+=1
            else:
                if(streak != 0): occurances.append(streak)
                streak = int(0)

        for i in range(len(occurances)): sum += occurances[i]

        result = sum / len(occurances)
        print("Average of messages send per day by both users: {:.2f}".format(result))
   
    def getHour(self, FLAG="string"):
        # Returns an array of times
        streak = int(0) 
        for lines in self.chat:
            time = re.findall('(([0-9]{1,2})\:([0-9]{1,2})\s(AM|PM))', lines.rstrip()) 
            if   FLAG == "string":   return time[0] 
            elif FLAG == "hour":   return time[1]  
            elif FLAG == "minute": return time[2] 
            elif FLAG == "period": return time[3] 
            elif FLAG == "vector": return time  
            else: print("[ERROR] FLAG not found"); exit()

    # def extractNames(self):

