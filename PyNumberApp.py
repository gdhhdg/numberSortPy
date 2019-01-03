import os
import re
#path = './numbers.txt'
highest = {}
lowest = {}

def get_file(file_name):
    path = file_name
    number_file = open(path, 'r')  
    number_read = number_file.readlines()
    linenumber = 1
    for line in number_read:
        line = line.strip("\n")
        line = line.strip('')
        line = line.replace("\n","")
        line = line.split(" ")
        line = filter(bool, line)
        line = list(map(int, line))
        check_size(line)
        print("line number: " + str(linenumber))
        check_text(line)
        add_numbers(line)
        average_numbers(line)
        get_highest(line, linenumber)
        get_lowest(line, linenumber)
        print(highest)
        print(line)
        linenumber+=1
    return_highest(highest)
    return_lowest(lowest)
    number_file.close()
    
def add_numbers(file):
    count = int(0)
    for n in file:
        if n == "":
            pass
        else:
            #line = re.sub(r"[\n\t\s]*", "", line)
            count = int(n) + int(count)
    print( " Toal is: " + str(count))
    return count
def average_numbers(line):
    amount = 0
    count = 0
    for n in line:
        amount = amount + 1
        if n == "":
            pass
        else:
            count = int(n) + int(count)
    average = int(count)/int(amount)
    print("Average is " + str(round(average)))
    return round(average)

def get_highest(line, line_num):
        highest[line_num]= max(line)
        return max(line)

def return_highest(list):
    maximum = max(list, key=list.get)
    print("highest is Line " + str(maximum) + " : " + str(list[maximum]))
    return list[maximum]

def get_lowest(line, line_num):
    lowest[line_num] = min(line)
    return min(line)

def return_lowest(list):
    minimum = min(list, key=list.get)
    print("Lowest is line " + str(minimum) + " : " + str(list[minimum]))
    return list[minimum]
def check_size(list):
    for n in list:
        if int(n) > 99999999:
            raise Exception("Number too big")
    else:
        return
def check_text(list): ### doesn't matter. map to int will throw error.
    for n in list:
        if type(n) is str:
            raise Exception("Text inside document")


get_file('./numbers.txt')
