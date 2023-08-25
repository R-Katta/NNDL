
def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(input_string):
    return input_string[::2]

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    full_name = fullname(first_name, last_name)
    print("Full Name:", full_name)
    
    alternate_chars = string_alternative(full_name)
    print("Alternate Characters:", alternate_chars)

if __name__ == "__main__":
    main()
