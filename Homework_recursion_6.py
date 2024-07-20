def recursive_len(ls):
    if not ls:
        return 0
    return recursive_len(ls[1:])+1
print(recursive_len([32,5]))
