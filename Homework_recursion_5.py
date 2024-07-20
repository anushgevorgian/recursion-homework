def recursive_ls(ls):
    if not ls:
        return
    print(ls[0])
    recursive_ls(ls[1:])




(recursive_ls([1,2,3]))