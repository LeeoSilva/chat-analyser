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
    chat = None 

    def __init__(self, textfile):
        # Receives a .txt file as a input 
        with open(textfile, 'r') as f: self.chat = f.readlines()


    def getWords(self):
        # Appends all the words in a array
        words = []
        regexp = r':\s(.*)|(^\D+)'

        for lines in self.chat:
            try:
                lineWords = re.search(regexp, lines.rstrip()).group(1)
                words += lineWords.split(" ", len(lineWords))
            except: pass
        return words

    def getDate(self):
        # Mines the data searching for dates about the received messages
        actualTime = ""
        date = []
        regexp = r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}\,\s'
        for lines in self.chat:
            actualTime = re.findall(regexp, lines.rstrip())
            date.append(actualTime) 
        return date
  
    def getHour(self):
        # Returns an array of times
        streak = int(0)
        hours = []
        regexp = r'([0-9]{1,2})\:([0-9]{1,2})\s(AM|PM)' 
        for lines in self.chat:
            time = re.findall(regexp, lines.rstrip())
            hours.append(time)
        return hours
    
    def getMessageContent(self):
        # Retturns the content of the message
        regexp = r'\:\s(.*?)(?=\s*\d{2}\/|$)'
        content = []
        try:
            for lines in self.chat:
                content = re.findall(regexp, lines.rstrip())
                print(content.group(1))
                content.append(content.group(1))
        finally: return content

    def getNames(self):
        # Extracts the last name of the person who sent the message
        regexp = r'\-\s([^:]*):\s'
        names = []
        try: 
            for line in self.chat:
                name = re.search(regexp, line.rstrip())
                names.append(name.group(1))
        finally: return names


    def runRegex(self, regexp):
        # Runs an custom regex 
        result = []
        try:
            for line in self.chat:
                resultLine = re.findall(regexp, line.rstrip())
                result.append(resultLine)
        finally: return result

