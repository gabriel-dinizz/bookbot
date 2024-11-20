book_path = "/Users/gabrieldiniz/workspace/github.com/gabrieldiniz/bookbot/books/frankestein.txt"

def main():
    with open(book_path) as f:
        return (f.read())

# main()

def count_word():
    with open(book_path) as words:
        return (len(words.read().split()))

# count_word()

def count_characters():
    with open(book_path, 'r') as book:
        myString = book.read().lower()
        freq = {}
        for c in myString:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq

# count_characters()


def generate_report():
    counted_words = count_word()
    character_counts = count_characters()
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{counted_words} words found in the document")
    for char, count in sorted_characters:
        if char.isalpha(): 
            print(f"The '{char}' character was found {count} times.")
    

    

generate_report()
