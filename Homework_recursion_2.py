def number_to_one(n):
    if n > 0:
        print(n)
        n = n-1
        number_to_one(n)

number_to_one(5)
