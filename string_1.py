#input string contains list of characters
input_string = list(input("Enter the string: "))

# Delete at least 2 characters from string
if len(input_string) >= 2:
    del input_string[:2]
else:
    print("String is too short to delete 2 characters.")

# Reversing the result string
resultant_string = ''.join(input_string[::-1])

# Printing the reversed resultant string
print(resultant_string)
