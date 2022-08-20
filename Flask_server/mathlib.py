def AtMax35To36(n):
    if n < 10:
        return str(n)
    elif n < 36:
        return chr(n + 55)

def to36(n):
    result = ""
    if n < 36:
        result = AtMax35To36(n)
        n = 0
    while n != 0:
        if n < 36:
            result = AtMax35To36(n) + result
            n = 0
        else:
            result = AtMax35To36(n % 36) + result
            n = n // 36
        #print(num, "    ", risultato)
    return result
