import sys
from stats import ( 
    word_count, 
    character_count,
    sorted_dictionary
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    count = word_count(text)
    characters = character_count(text)
    sorted_list = sorted_dictionary(characters)

    get_report(path, count, sorted_list)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def get_report(path, count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for line in sorted_list:
        if not line["char"].isalpha():
            continue

        print(f"{line['char']}: {line['num']}")

    print("============= END ===============")

main()