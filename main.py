import sys
from stats import get_num_words, character_counter, sort_list

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        return f.read()

def print_character_counter(text):
	result = character_counter(text)
	print(result)
def print_report(text):
	chara_dict = character_counter(text)
	sorted_list = sort_list(chara_dict)
	for item in sorted_list:
		if item['char'].isalpha():
			print(f"{item['char']}: {item['num']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    print_character_counter(text)
    print(f"Found {num_words} total words")
    print_report(text)
if __name__ == "__main__":
    main()
