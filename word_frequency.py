import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
# """- remove punctuation"""
# """- normalize all words to lowercase"""
# """- remove "stop words" -- words used so frequently they are ignored"""
# """- go through the file word by word and keep a count of how often each word is used""" (use .count)

    with open(file,'r') as file_contents:
        contents_string = file_contents.read()
        contents_lower = contents_string.lower()
        for character in string.punctuation:
            contents_lower = contents_lower.replace(character, '')

        contents_split = contents_lower.split()
        for word in contents_split:
            if word in STOP_WORDS:
                contents_split.remove(word)
            if word in contents_split:
                contents_split.count(word)

#        contents_count = contents_split.count(word)
#        for word_count in contents_count:
#            if word_count in contents_split:
#                contents_split.count(word)

    print(contents_split)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
