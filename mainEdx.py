from datetime import datetime

from tribe.ai.edx.SortingAlgorithms import sort_with_bubbles, sort_with_select, mergesort
# rule of thumb for big O notation : the number of nested loops (nested!) on the same list is power of n
# e.g. O(n^2) - there are 2 nested loops, O(n) [linear] - one nested loop. Or there can be several loops on the same list
# but if loops are not nested - the complexity is O(n) [linear]
from tribe.ai.edx.SearchAlgorithms import linear
from tribe.ai.edx.Exam import *

from tribe.ai.edx.ExamClasses import Name, Meeting

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: [1, 2, 3, 4, 5]
#print(sort_with_bubbles([5, 3, 1, 2, 4]))

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
#print(sort_with_select([5, 3, 1, 2, 4]))

#Let's try it out!
#print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

#It works! To see more about how it works, check out
#MergesortwithPrints.py. To get a succinct version of
#this algorithm, checkout MergesortShort.py.


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
a_list = [5, 1, 3, 7, 3, 1, 7, 8, 3, 6]
#print(linear(a_list, 6))

some_number = 17

#print("fibonacci(", some_number, ") : ", end = "")
#print(fibonacci(some_number))

#print("collatz(", some_number, ") : ", end = "")
#print(collatz(some_number))

#print("collatz2(", some_number, ") : ", end = "")
#print(collatz2(some_number))

test_name = Name("David", "Joyner")
#print(test_name.first_name)
#print(test_name.last_name)
#print(test_name.find_printed_name()) # prints "None" on the last line for some reason
#print(test_name.find_sortable_name())

#print(joynernacci(3))
#print(joynernacci(5))
#print(joynernacci(12))

meetings = [Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
            Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
            Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
#print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
#print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))

#print(check_horse_winner(("HOR", "HORS", "H", "HO")))
#print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
#print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))

print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))