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
    _chat    = None 
    _words   = []
    _dates   = []
    _hours   = []
    _names   = []
    _content = []

    def __init__(self, textfile):
        # Receives a .txt file as a input 
        with open(textfile, 'r') as f: self._chat = f.readlines()


    def getWords(self):
        # Appends all the words in a array
        if len(self._words) != 0: return self.words 
        regexp = r':\s(.*)|(^\D+)'

        for lines in self._chat:
            try:
                lineWords = re.search(regexp, lines.rstrip()).group(1)
                self._words += lineWords.split(" ", len(lineWords))
            except: pass
        return self._words

    def getDate(self):
        # Mines the data searching for dates about the received messages
        if len(self._dates) != 0 : return self._dates
        regexp = r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}\,\s'
        for lines in self._chat:
            actualTime = re.findall(regexp, lines.rstrip())
            self._dates.append(actualTime) 
        return self._dates
      
    def getHour(self):
        # Returns an array of times
        if len(self._hours) != 0: return self._hours
        regexp = r'([0-9]{1,2})\:([0-9]{1,2})\s(AM|PM)' 
        for lines in self._chat:
            try:
                time = re.findall(regexp, lines.rstrip())
                self._hours.append(time)
            except: pass
        return self._hours
    
    def getMessageContent(self):
        # Returns the content of the message
        if len(self._content) != 0: return self._content
        regexp = r'\:\s(.*?)(?=\s*\d{2}\/|$)'
        for lines in self._chat:
            try:
                content = re.findall(regexp, lines.rstrip()).group(1)
                self._content.append(content)
            except: pass
        return self._content

    def getNames(self):
        # Extracts the last name of the person who sent the message
        if len(self._names) != 0: return self._names
        regexp = r'[AM|PM]\s\-\s([^:]*):\s\w'
        for line in self._chat:
            try:
                name = re.search(regexp, line.rstrip()).group(1)
                self._names.append(name)
            except: pass
        return self._names

    def runRegex(self, regexp):
        # Runs an custom regex 
        result = []
        for line in self._chat:
            try:
                resultLine = re.findall(regexp, line.rstrip())
                result.append(resultLine)
            except: pass
        return result
