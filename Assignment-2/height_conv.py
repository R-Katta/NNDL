# Nested Interactive loop approach
def convert_heights_nested(heights):
    converted_heights = []
    for height in heights:
        cm = height * 2.54
        converted_heights.append(cm)
    return converted_heights

# List comprehensions approach
def convert_heights_comprehension(heights):
    return [height * 2.54 for height in heights]

def main():
    heights = []
    n = int(input("Enter the number of heights: "))
    for _ in range(n):
        height = float(input("Enter height in inches: "))
        heights.append(height)
    
    converted_nested = convert_heights_nested(heights)
    converted_comprehension = convert_heights_comprehension(heights)
    
    print("Converted Heights using Nested Loop:", converted_nested)
    print("Converted Heights using List Comprehensions:", converted_comprehension)

if __name__ == "__main__":
    main()
