test = "That on the first day of January, in the year of our Lord one thousand eight hundred and sixty-three, all persons held as slaves within any State or designated part of a State, the people whereof shall then be in rebellion against the United States, shall be then, thenceforward, and forever free; and the Executive Government of the United States, including the military and naval authority thereof, will recognize and maintain the freedom of such persons, and will do no act or acts to repress such persons, or any of them, in any efforts they may make for their actual freedom."
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
from collections import Counter

for char in test:
    if char not in punctuations:
        no_punct = no_punct + char

no_case = no_punct.lower()

no_stop = no_case

for word1 in no_case.split():
    for word2 in STOP_WORDS:
        if word1 == word2:
            # print(word1)
            no_stop = no_stop.replace(" " + word1 + " ", " ")
        
for word in STOP_WORDS:
    if no_case.split()[0] == word:
        no_stop = no_stop.replace(word + " ", " ")

for word in STOP_WORDS:
    if no_case.split()[-1] == word:
        no_stop = no_stop.replace(" " + word, " ")

my_var = no_stop.split()

frequency_report = dict(Counter(my_var))

print(frequency_report)







    











# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     pass


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)