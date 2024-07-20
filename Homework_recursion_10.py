def recursive__ispalindrome(string):
    if not string or len(string) == 1:
        return True
    recursive__ispalindrome(string[1:-1])
    return string[-1] == string[0]

print(recursive__ispalindrome("g"))