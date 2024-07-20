def new_line(string):
    if not string or len(string) == 1:
        return string
    print(string[0])
    new_line(string[1:])

new_line("mystring")
