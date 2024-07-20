def recursive_reverse(string):
    if not string or len(string) == 1:
        return string
    return string[-1] + recursive_reverse((string[1:-1])) + string[0]

print(recursive_reverse("p"))
