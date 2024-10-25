def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

    
def word_count(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    print(count)

word_count(main())