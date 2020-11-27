#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:23:59 2020

@author: jwoo
"""
def frequency(word, text):
    '''Determines the number of times word appears in text
    '''
    count = 0
    for i in range(len(text)):
        if word == text[i]:
            count += 1
            
    return count

#Problem 1
text = open("gutenberg_excerpt.txt", encoding = "latin-1").read().split()

#Part (a)
word_counts = {}
test_text = set(text)
for word in test_text:
    word_counts[word] = frequency(word, text)
    
#Part (b)
def top10(L):
    '''Takes a list L of 100 different integers, and returns
    a list of the 10 largest integers in L
    '''
    return(sorted(L, reverse = True)[:10])

#Part (c)    
#Start by switching the key and values
freq = {}
temp_list = []
for key, value in word_counts.items():
    if value not in freq.keys():
        freq[value] = key
    else:
        freq[value] = freq[value] + " " + key

#Finding top 10 keys (frequency)
top_10_keys = top10(freq.keys())
#appending top 10 values to list top_10_words.
top_10_words = []
for i in top_10_keys:
    words = freq[i].split()
    top_10_words.extend(words)

top_10_words = top_10_words[0:10]
    
print(word_counts,"\n")
print(freq,"\n")
print(top_10_keys,"\n")
print(top_10_words,"\n")
    
# if __name__ == "__main__":
#     L = [1,2,65,3,5,1,5,6,12,5,6,7,2,13,6,7,12]
#     print(top10(L))