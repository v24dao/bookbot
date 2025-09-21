def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
    
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)

main()