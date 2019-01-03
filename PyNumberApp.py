import os
import re
import operator
#path = './numbers.txt'
sums = {}
highest = {}
lowest = {}
averages = {}

class NumberCheck():
    def __init__(self):
        self = self
    def get_file(file_name):
        path = file_name
        number_file = open(path, 'r')  
        number_read = number_file.readlines()
        lines = []
        for line in number_read:
            line = line.strip("\n")
            line = line.strip('')
            line = line.split(" ")
            line = filter(bool, line)
            line = list(map(int, line))
            lines.append(line)
        return lines
        number_file.close()
class AddNumber():
    def __init__(self):
        self = self
    def add_numbers():
        lineNumber = 1
        for eachNumber in numberlist:
            sums[lineNumber] = sum(eachNumber)
            lineNumber+=1
        print("Sums are :" + str(sums))
        return sums
class AverageNumbers():
    def __init__(self):
        self = self
    def average_numbers():
        lineNumber = 1
        for eachNumber in numberlist:
            total = sum(eachNumber)
            average = round(total/(len(eachNumber) + 1))
            averages[lineNumber] = average
            lineNumber+=1
        print("averages are " + str(averages))
        return averages

class HighestNumber():
    def __init__(self):
        self = self
    def highest_number():
        current = 0 
        lineNumber = 1
        maxnumbers = {}
        for eachNumber in numberlist:
            maxnumbers[lineNumber] = max(eachNumber)
            lineNumber+=1
        highest = max(zip(maxnumbers.keys(), maxnumbers.values()))
        print("Highest number is on line: " + str(highest[0]) + " and the highest number is " + str(highest[1]))
        return highest
class LowestNumber():
    def __init__(self):
        self = self
    def lowest_number():
        current = 0 
        lineNumber = 1
        minnumbers = {}
        for eachNumber in numberlist:
            minnumbers[lineNumber] = min(eachNumber)
            lineNumber+=1
        lowest = min(zip(minnumbers.keys(), minnumbers.values()))
        print("Lowest number is on line: " + str(lowest[0]) + " and the lowest number is " + str(lowest[1]))
        return lowest
numberlist = NumberCheck.get_file('./numbers.txt') 
AddNumber.add_numbers()
AverageNumbers.average_numbers()
HighestNumber.highest_number()
LowestNumber.lowest_number()


