from stats import get_num_words, get_char_counts, char_dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_list = char_dict_to_sorted_list(char_counts)
    print_report(book_path, num_words, sorted_list)
    
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_list:
        if x["char"].isalpha():
            print(f"{x['char']}: {x['num']}")
    print("============= END ===============")

main()