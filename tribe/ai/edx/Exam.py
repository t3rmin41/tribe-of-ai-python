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