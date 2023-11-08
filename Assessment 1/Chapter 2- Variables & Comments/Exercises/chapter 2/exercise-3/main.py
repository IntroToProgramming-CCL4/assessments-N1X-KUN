# Use a variable to represent a person’s name, and include some whitespace characters at the 
# beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

NAME = "\tGerard Matthew\n"

print("Default:")
print(NAME)

print("\nLstrip format:")
print(NAME.lstrip())

print("\nRstrip format:")
print(NAME.rstrip())

print("\nStrip format:")
print(NAME.strip())

# "Had a bit trouble understanding the instructions but got it..."