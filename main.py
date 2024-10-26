def get_file_text(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    count = len(words)
    print(f"Word count: {count}")
    return words
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    word_count(text)

main()