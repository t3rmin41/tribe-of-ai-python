def fibonacci(some_number):
    if some_number <= 2 :
        return 1
    else:
        return fibonacci(some_number - 1) + fibonacci(some_number - 2)

def collatz(current_number):
     print(current_number, " ", end = "")
     if current_number % 2 == 0:
         return collatz(current_number // 2)
     else:
         if current_number != 1:
             return collatz(current_number * 3 + 1)

def collatz2(current_number):
    print(current_number, " ", end = "")
    if current_number % 2 == 0:
        return collatz(current_number // 2)
    elif current_number % 2 == 1 :
            return collatz(current_number * 3 + 1)
    else :
        #pass
        return 1 # Though the correct answer - None of these will work with the remainder of the code as written.

def joynernacci(index):
    if index <= 2 :
        return 1
    if index % 2 == 0 :
        return joynernacci(index - 1) + joynernacci(index - 2)
    if index % 2 == 1 :
        return abs(joynernacci(index - 1) - joynernacci(index -2))

from typing import List
from datetime import datetime

from tribe.ai.edx.ExamClasses import Meeting

#def check_availability(meetings, tstamp):
def check_availability(meetings: List[Meeting], tstamp: datetime):
    for meeting in meetings:
        if tstamp.ctime() >= meeting.start_time.ctime() and tstamp.ctime() <= meeting.end_time.ctime() :
            return False
    return True

#def check_horse_winner(players_data):
def check_horse_winner(players_data: List[str]):
    players_index = []
    for index, player_data in enumerate(players_data) :
        if len(player_data) < 5 :
            players_index.append(index)
    if len(players_index) == 1 :
        return "Player " + str(players_index[0]) + " wins!"
    if len(players_index) > 1 and len(players_index) < len(players_data) :
        return "Players " + ", ".join(map(str, players_index)) + ": keep playing!"
    else: return "Everyone: keep playing!"

def count_capital_consonants(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in input_str :
        if letter.lower() not in vowels and letter.isupper() :
            count += 1
    return count

def are_anagrams(first, second):
    first = [char for char in first.replace(" ", "").lower()]
    second = [char for char in second.replace(" ", "").lower()]
    first.sort()
    second.sort()
    #return first == second # also returns True if list elements are equal - does Python check equality element by element when '==' operator is used?
    return str(first) == str(second)

def alter_list(str_list, int_list):
    for index in int_list :
        for i in range(0, len(str_list)):
            if i == index and str_list[i].islower():
                str_list[i] = str_list[i].upper()
            elif i == index and str_list[i].isupper():
                str_list[i] = str_list[i].lower()
    return str_list

def alter_list2(str_list, int_list): # doesn't work with enumerate() as enumerate() creates local variables which are not assigned to parameter list elements or because i, word is tuple?
    for index in int_list:
        for i, word in enumerate(str_list) :
            if i == index and word.islower() :
                #word = word.upper()
                word.upper()
            elif i == index and word.isupper() :
                #word = word.lower()
                word.lower()
    return str_list

def rabbit_hole(d: dict, key):
    value_tuple = (key, d.get(key))
    while value_tuple[1] != None :
        if d.get(value_tuple[1]) == key :
            return False
        value_tuple = (value_tuple[1], d.get(value_tuple[1]))
    return value_tuple[0]