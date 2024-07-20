def recursive_factorial(n):
    if n<0:
        return
    elif n==1 or n == 0:
        return 1

    return n * recursive_factorial(n-1)

print(recursive_factorial(3))

