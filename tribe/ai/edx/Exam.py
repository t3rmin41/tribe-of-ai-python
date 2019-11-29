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

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def find_printed_name(self):
        return self.first_name+" "+self.last_name
    def find_sortable_name(self):
        return self.last_name + ", " + self.first_name[0]

def joynernacci(index):
    if index <= 2 :
        return 1
    if index % 2 == 0 :
        return joynernacci(index - 1) + joynernacci(index - 2)
    if index % 2 == 1 :
        return abs(joynernacci(index - 1) - joynernacci(index -2))