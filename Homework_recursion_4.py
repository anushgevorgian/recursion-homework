def recursive_sum(n):
    if n<=0:
        return
    if n == 1:
        return 1
    return recursive_sum(n-1) + n

print(recursive_sum(0))