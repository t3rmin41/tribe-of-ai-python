def evenDigitsOnly(n):
    while n >= 10:
        current_digit = n % 10
        if current_digit % 2 != 0:
            return False
        n = n // 10
    if n < 10 :
        return n % 2 == 0
    return True
