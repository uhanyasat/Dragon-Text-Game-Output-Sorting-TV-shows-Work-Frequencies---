# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:20:45 2021

@author: Sathish
"""


            
# Python code to find frequency of each word
def freq(str):

	# break the string into list of words
	str = str.split()		
	str2 = []

	# loop till string values present in list str
	for i in str:			

		# checking for the duplicacy
		if i not in str2:

			# insert value in str2
			str2.append(i)
			
	for i in range(0, len(str2)):

		# count the frequency of each word(present
		# in str2) in str and print
		print(str2[i], ' ', str.count(str2[i]))	
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        ele=" "+ele
        str1 += ele  
    
    # return string  
    return str1 

def main():
    import csv

    with open('input1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            #print(row)
            data=row
    print('-----------------Input-------------------')
    print(data)
    print('-----------------Output-------------------')
    s = data
    str =listToString(s)
    #print(str)
    freq(str)					

if __name__=="__main__":
	main()			 # call main function
