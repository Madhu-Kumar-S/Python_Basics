# You are given a string s.
# Your task is to find out if the string s contains any: alphanumeric characters,
# alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))