def recursive_fibo(n):
    if n == 0 or n ==1:
        return 1
    return recursive_fibo(n-1) + recursive_fibo(n-2)

print(recursive_fibo(4))