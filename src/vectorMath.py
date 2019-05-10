#!/usr/bin/python3

def getRepeatedElements(arr):
    # Returns the repeated numbers of an array
    streak = int(1)
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            streak+=1
            print("{} counter: {}".format(arr[i], streak))
        else: streak = int(1)

    
