def get_file_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    count = len(words)
    return words, count
    

def letter_count(text):
    letter_count = {}
    
    for word in text:
        for char in word:
            if char.isalpha():
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1
    
    return letter_count
    
    
def create_list(letter_count):
    letters = []
    
    for key in letter_count:
        letters.append({"char": key, "count": letter_count[key]})
    return letters
        
        
def sort_on(dict):
    return dict["count"]


def report(book_path, letter_list, word_count):
    print(f"--- START OF THE REPORT IN {book_path} ---\n"
    f"The total amount of words was {word_count}")
    
    for letter in letter_list:
        print(f"The {letter['char']} character appeared {letter['count']} times")
    
    
    print("--- END OF THE REPORT ---")


def main():
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    lower_words = text.lower()
    counted = letter_count(lower_words)
    words, word_count = count_words(text)
    letter_list = create_list(counted)
    letter_list.sort(reverse=True, key=sort_on)
    report(book_path, letter_list, word_count)

main()