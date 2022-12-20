# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:36:04 2021

@author: Sathish
"""


 
# Using readlines()
file1 = open('file1.txt', 'r')
Lines = file1.readlines()
 

lst=[]
# Strips the newline character
for line in Lines:
    #print(line)
    lst.append(line.strip())

count = 1
class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
        
dict_obj = my_dictionary()
x=len(lst)
#file1 = open('output_keys.txt', 'w')
for i in range(1,x+1):
    if count%2!=0:
        print(lst[i],lst[i-1])
        
        dict_obj.add(lst[i],lst[i-1])
    count+=1
    
print(dict_obj)
file2 = open('Output_Titles.txt', 'w')

bad_chars = ['[', ']']
for key in sorted(dict_obj):
    print("%s" % (key))
    x=("%s\n" % (key))
    for i in bad_chars :
        x = x.replace(i, '')
    file2.writelines(x)
    

file2.close()

flipped = {}
  
for key, value in dict_obj.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
  
# printing result
print("final_dictionary", str(flipped))

file1 = open('Output_keys.txt', 'w')

bad_chars = ['[', ']']
for key in sorted(flipped):
    print("%s: %s" % (key, str(flipped[key])))
    x=("%s: %s \n" % (key, str(flipped[key])))
    for i in bad_chars :
        x = x.replace(i, '')
    file1.writelines(x)
    

file1.close()


