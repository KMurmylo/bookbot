from stats import print_report
import sys


def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        print_report(sys.argv[1],file_contents)
    

main()



