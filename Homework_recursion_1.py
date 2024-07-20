def one_to_number(n):
    if n > 0:
        one_to_number(n-1)
        print(n)

one_to_number(5)