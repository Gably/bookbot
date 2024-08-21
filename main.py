def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
    
    num_of_words = count_words(book)
    character_count_dict = count_char(book)
    #print(character_count_dict)
    character_count_list = list(character_count_dict.items())
    #print(character_count_list)
    character_count_list.sort(reverse = True, key = sort_on)
    #print(character_count_list)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")
    for character in character_count_list:
        print(f"The '{character[0]}' character was found {character[1]} times")
    print("--- End report ---")


def count_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    char_count = {}
    a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z = 0
    book_in_lowercase = book.lower()
    
    for char in book_in_lowercase:
        if char == 'a':
            a += 1
        elif char == 'b':
            b += 1
        elif char == 'c':
            c += 1
        elif char == 'd':
            d += 1
        elif char == 'e':
            e += 1
        elif char == 'f':
            f += 1
        elif char == 'g':
            g += 1
        elif char == 'h':
            h += 1
        elif char == 'i':
            i += 1
        elif char == 'j':
            j += 1
        elif char == 'k':
            k += 1
        elif char == 'l':
            l += 1
        elif char == 'm':
            m += 1
        elif char == 'n':
            n += 1
        elif char == 'o':
            o += 1
        elif char == 'p':
            p += 1
        elif char == 'q':
            q += 1
        elif char == 'r':
            r += 1
        elif char == 's':
            s += 1
        elif char == 't':
            t += 1
        elif char == 'u':
            u += 1
        elif char == 'v':
            v += 1
        elif char == 'w':
            w += 1
        elif char == 'x':
            x += 1
        elif char == 'y':
            y += 1
        elif char == 'z':
            z += 1

    char_count['a'] = a
    char_count['b'] = b
    char_count['c'] = c
    char_count['d'] = d
    char_count['e'] = e
    char_count['f'] = f
    char_count['g'] = g
    char_count['h'] = h
    char_count['i'] = i
    char_count['j'] = j
    char_count['k'] = k
    char_count['l'] = l
    char_count['m'] = m
    char_count['n'] = n
    char_count['o'] = o
    char_count['p'] = p
    char_count['q'] = q
    char_count['r'] = r
    char_count['s'] = s
    char_count['t'] = t
    char_count['u'] = u
    char_count['v'] = v
    char_count['w'] = w
    char_count['x'] = x
    char_count['y'] = y
    char_count['z'] = z

    return char_count

def sort_on(list):
    return list[1]


main()