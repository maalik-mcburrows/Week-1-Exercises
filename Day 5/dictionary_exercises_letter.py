# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# $ python letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}
import string
from collections import Counter
user_word = input("Please enter a word: ")
# d = {}
# # for letter in string.ascii_letters:
# #     for elem in input:
# #         if spec_letter in elem:
# #             d[elem] += 1
# #         else:
# #             d[elem] = 1
# # print(d)
# for letter in string.ascii_letters:
#     for i in user_word:
#         if letter in string.ascii_letters:
#                 print(letter, Counter[letter])
            # d[letter] += 1 
        # else:
            # d = 1
# print(d)
# print(string.ascii_letters)
letter_frequency={}

def count_letter_frequency(word_list):
    for word in user_word:
        for letter in string.ascii_letters:
            # keys=letter_frequency.keys()
            if letter in user_word:
                letter_frequency[letter]+=1
            else:
                letter_frequency[letter]=1
print(letter_frequency)