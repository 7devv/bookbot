def get_file_text(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(text):
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


def main():
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    lower_words = text.lower()
    counted = letter_count(lower_words)
    word_count(text)
    letter_list = create_list(counted)
    letter_list.sort(reverse=True, key=sort_on)
    

main()