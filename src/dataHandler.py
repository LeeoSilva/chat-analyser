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
    words = []
    dates = []
    hours = []
    names = []
    content = []


    def __init__(self, textfile):
        # Receives a .txt file as a input 
        with open(textfile, 'r') as f: self.chat = f.readlines()


    def getWords(self):
        # Appends all the words in a array
        if len(self.words) != 0: return self.words 
        regexp = r':\s(.*)|(^\D+)'

        for lines in self.chat:
            try:
                lineWords = re.search(regexp, lines.rstrip()).group(1)
                self.words += lineWords.split(" ", len(lineWords))
            except: pass
        return self.words

    def getDate(self):
        # Mines the data searching for dates about the received messages
        if len(self.dates) != 0 : return self.dates
        regexp = r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}\,\s'
        for lines in self.chat:
            actualTime = re.findall(regexp, lines.rstrip())
            self.dates.append(actualTime) 
        return self.dates
  
    def getHour(self):
        # Returns an array of times
        if len(self.hours) != 0: return self.hours
        regexp = r'([0-9]{1,2})\:([0-9]{1,2})\s(AM|PM)' 
        for lines in self.chat:
            time = re.findall(regexp, lines.rstrip())
            self.hours.append(time)
        return self.hours
    
    def getMessageContent(self):
        # Returns the content of the message
        if len(self.content) != 0: return self.content
        regexp = r'\:\s(.*?)(?=\s*\d{2}\/|$)'
        try:
            for lines in self.chat:
                content = re.findall(regexp, lines.rstrip()).group(1)
                self.content.append(content)
        finally: return self.content

    def getNames(self):
        # Extracts the last name of the person who sent the message
        if len(self.names) != 0: return self.names
        regexp = r'\-\s([^:]*):\s'
        try: 
            for line in self.chat:
                name = re.search(regexp, line.rstrip()).group(1)
                self.names.append(name)
        finally: return self.names


    def runRegex(self, regexp):
        # Runs an custom regex 
        result = []
        try:
            for line in self.chat:
                resultLine = re.findall(regexp, line.rstrip())
                result.append(resultLine)
        finally: return result

