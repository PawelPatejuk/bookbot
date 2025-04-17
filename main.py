import sys
from stats import get_books_text, get_num_words, get_num_characters, print_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])
        sys.exit(0)

main()
