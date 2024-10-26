def get_file_text(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    count = len(words)
    print(f"Word count: {count}")
    return words
    

def letter_count(text):
    letter_count = {}
    
    for word in text:
        for char in word:
            if char.isalpha():
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1
    
    print(letter_count)
    
            
        


def main():
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    lower_words = text.lower()
    letter_count(lower_words)
    word_count(text)

main()