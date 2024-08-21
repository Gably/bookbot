def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    num_of_words = count_words(words)
    print(f"Number of words: {num_of_words}")

def count_words(words):
    return len(words)



main()