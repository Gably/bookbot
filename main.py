def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    num_of_words = len(words)
    print(num_of_words)

main()