# Python program to split and join a string

s = input("enter a names:")
print("string is:",s)

splitting_char = input("enter splitting_char:")

print("\non splitting:",s.split(splitting_char))

d = input("enter delimiter:")

print("\non rejoining:",d.join(s.split(splitting_char)))




