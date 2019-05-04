#!/usr/bin/python3

import re # Regular expression library


class data:
    chat = 0
    primaryChat = []
    secondaryChat = []
    dates = []


    def __init__(self, textfile):
        with open(textfile, 'r') as f:
            self.chat = f.readlines()

    def getDate(self):
        actualTime = ""
        date = []
        for lines in self.chat:
            actualTime = re.findall('^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{1,2}\, ', lines.rstrip())
            self.dates.append(actualTime) 

    def getMessagePerDay(self):
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
        for i in range(len(occurances)):
            sum += occurances[i]

        result = sum / len(occurances)
        print("Average of messages send per day by both users: {:.2f}".format(result))
   
    def getHour(self, ="full"):
        streak = int(0) 
        
        for lines in self.chat:
            time = re.findall('(([0-9]{1,2})\:([0-9]{1,2})\s(AM|PM))', lines.rstrip()) 
            if get == "full": return time 
            

    # def extractNames(self):

