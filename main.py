from stats import get_num_words, get_num_alpha, my_report, print_report
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

if len(sys.argv) == 2:
    path_to_file = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

print_report(path_to_file)

