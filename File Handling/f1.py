# writing a file
f = open("dog", "w")
str = input("Enter text to add:\n")
f.write(str)
f.close()