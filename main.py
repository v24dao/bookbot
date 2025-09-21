from stats import get_num_words, get_char_counts

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(get_char_counts(text))
    
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
main()