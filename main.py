def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
    
    num_of_words = count_words(book)
    print(f"Number of words: {num_of_words}")

def count_words(book):
    words = book.split()
    return len(words)



main()