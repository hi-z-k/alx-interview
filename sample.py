def recursive(n):
    if (n == 1):
        return 1
    else:
        return 2 + recursive(n - 1)
    
print(recursive(2))