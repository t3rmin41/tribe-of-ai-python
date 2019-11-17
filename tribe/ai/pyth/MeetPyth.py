def countBits(n):
    return n.bit_length()

def countBitsInLoop(n):
    i = 0
    while n > 0:
        n = n // 2
        i += 1
    return i

def modulus(n):
    if isinstance(n, int) :
        return n % 2
    else:
        return -1

def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

def baseConversion(n, x):
    return hex(int(str(n), x))[2::]

def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found