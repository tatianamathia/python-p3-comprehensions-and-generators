#!/usr/bin/env python3

def return_evens(num_list):
    return [item for item in num_list if item % 2 == 0]

 
 
def make_exclamation(sentence_list):
    return[sentence_list + '!' for sentence_list in sentence_list]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))    