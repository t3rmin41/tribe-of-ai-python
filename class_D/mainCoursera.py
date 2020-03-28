#Packing and unpacking
import sys

def sum_unknown_number_of_elements(*args): # *args means pack whatever number of arguments is into tuple
    sum = 0
    for e in args:
        sum = sum + e
    return sum

print("sum_unknown_number_of_elements(1,3,5,2) :", sum_unknown_number_of_elements(1,3,5,2))
print("sum_unknown_number_of_elements(1,3) :", sum_unknown_number_of_elements(1,3))

import csv

#

cvs_file = open("resources/mpg.csv")
mpg = list(csv.DictReader(cvs_file))

mpg[:3]

#print(mpg[0].keys())

cylinders = set(d['cyl'] for d in mpg)
print(cylinders)

print(sys.version)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#print(list(map(split_title_and_name, people)))

#option 1
for person in people:
    split_title_name = lambda x: x.split()[0] + " " + x.split()[-1]
    #print(split_title_name(person))
    #print(split_title_and_name(person) == split_title_name(person)) # prints if split_title_and_name and lambda output is the same
    #print(split_title_and_name(person) == (lambda x: x.split()[0] + " " + x.split()[-1])(person)) # define lambda and call with parameter in one line

#option 2
#list(map(split_title_and_name, people)) == list(map(???))

#List comprehension - manipulating list in one line with defining

comprehended_list = [str(i)+str(j) for i in range(6,10) for j in range(0,5)]
#print(comprehended_list)

'''
Many organizations have user ids which are constrained in some way. 
Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49). 
Your task at such an organization might be to hold a record on the billing activity for each possible user.

Write an initialization line as a single list comprehension which creates a list of all possible user ids. Assume the letters are all lower case.
'''

#lowercase = 'abcdefghijklmnopqrstuvwxyz'
lowercase = 'abcd'
digits = '0123456789'

#answer = [e1+e2+str(d1)+str(d2) for e1 in lowercase for e2 in lowercase for d1 in digits for d2 in digits]
#print(answer)

import numpy as np

my_list = [1, 2, 3]
x = np.array(my_list)

print(x)

old = np.array([[1, 1, 1],
                [1, 1, 1]])

print("\n", sep="")
print(old)
print("\n", sep="")
new = old
new[0, :2] = 0
print(new)
print("\n", sep="")
print(old)