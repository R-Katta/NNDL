def main():
    word_count = {}
    
    with open("D:\\Neural Networking\\NNDL\\Assignment-2\\input.txt" , "r") as file:
        lines = file.readlines()
        
        for line in lines:
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    
    with open("output.txt", "w") as output_file:
        for line in lines:
            output_file.write(line)
        output_file.write("Word_Count:\n")
        for word, count in word_count.items():
            output_file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    main()
