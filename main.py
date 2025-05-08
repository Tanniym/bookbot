
import sys
from stats import words_in_book, chars_in_book, sort_chars


def get_book_text(file_path):
    with open(file_path) as f:
        result = f.read()
    return result




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        input_path = sys.argv[1]
        book_path = "./" + input_path
        wordcount = words_in_book(get_book_text(book_path))
        char_count = sort_chars(chars_in_book(get_book_text(book_path)))


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {input_path}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        
        for item in char_count:
            if list(item.keys())[0].isalpha():
                print(f"{list(item.keys())[0]}: {list(item.values())[0]}")

        print("============= END ===============")


main()



