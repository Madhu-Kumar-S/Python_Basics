# Python3 program for removing i-th
# indexed character from a string

# Removes character at index i
def remove(string, i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    return string


string = "geeksFORgeeks"

# Remove nth index element
i = 5

# Print the new string
print(remove(string, i))