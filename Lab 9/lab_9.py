#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:23:59 2020

@author: jwoo
"""
#Problem 1
text = open("gutenberg_excerpt.txt", encoding = "latin-1").read().split()

#Part (a)
word_counts = {}
for word in text:
    if word in word_counts.keys():
        word_counts[word] += 1
    else:
        word_counts[word] = 1

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

#Finding top 10 keys (frequency). Although we may not use all
#the words at the top 10 frequencies, this ensures that we always
#at least have 10 words.
top_10_keys = top10(freq.keys())
#Using the top 10 keys in decreasing order, we find the values
#at the frequencies in decreasing order.
top_10_words = []
for i in top_10_keys:
    words = freq[i].split()
    top_10_words.extend(words)

#The top 10 words are the first 10 words in that list
top_10_words = top_10_words[0:10]

print(word_counts,"\n")
print(freq,"\n")
print(top_10_keys,"\n")
print(top_10_words,"\n")

#Problem 3
import urllib.request
def number_of_results(search_term):
    '''Returns the number of search results for search_term
    on Yahoo
    '''
    url_term = search_term.split()
    url_term = "+".join(url_term)
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p="+url_term+"+&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
    page = f.read().decode("utf-8")
    f.close()

    text = page.split()
    number_of_results = text[text.index("results</span></div></div></li></ol></div></div><div")-1]
    number_of_results = number_of_results.replace('referrerpolicy="unsafe-url">Next<ins></ins></a><span>', "")
    number_of_results = number_of_results.replace(",","")
    return int(number_of_results)

def choose_variant(variants):
    '''Takes a list of usage variants and returns
    the variant which returns the most search results
    on Yahoo.com
    '''
    total_results = {}
    for variant in variants:
        total_results[variant] = number_of_results(variant)
    most_results = max(total_results.values())
    for key, value in total_results.items():
        if value == most_results:
            return key

test = ["top ranked school toronto", "top ranked school uwaterloo"]
f = choose_variant(test)

# if __name__ == "__main__":
#     L = [1,2,65,3,5,1,5,6,12,5,6,7,2,13,6,7,12]
#     print(top10(L))