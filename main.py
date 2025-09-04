from stats import get_word_count, count_characters,character_sorted
import sys

def get_boot_text(path_url):
    with open(path_url, "r") as f:
        return f.read()

path =""
if len(sys.argv)>1:
    path=sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main() :    
   text=get_boot_text(path)
   count=get_word_count(text)
   character_counts=count_characters(text)
   sorted_characters=character_sorted(character_counts)
   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   print (f"Found {count} total words")
   print("--------- Character Count -------")  
   for char in sorted_characters:
        if char["char"].isalpha():
            print(f"{char ['char']}: {char['num']}")
   

main()