def get_books_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_characters(text: str) -> dict:
    d = {}

    for c in text:
        if c.isalpha():
            c = c.lower()
            if c in d:
                d[c] += 1
            else:
                d[c] = 1    
    
    return d

def print_report(filepath: str) -> None:
    book_text = get_books_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    
    print("--------- Character Count -------")
    for k, v in sorted(get_num_characters(book_text).items(), key=lambda x:x[1], reverse=True):
        print(f"{k}: {v}")

    print("============= END ===============")
