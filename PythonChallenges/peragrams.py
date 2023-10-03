# Super-short hack solution for - https://open.kattis.com/problems/peragrams 
#
# * Sketch of algorithm:
#  1. do a frequency count of the letters used in the words
#  2. see how many of the frequencies are odd
#  3. it's okay to have 0 or 1 odd frequencies to make a palindrome,
#     but every odd frequency beyond that will require removing one letter.
#
# Author: Forrest Stonedahl

from collections import Counter

print(max(0,sum(v % 2 for k,v in Counter(input()).items()) - 1))

