#!/usr/bin/env python3

def return_evens(num_list):
    evens_in_list = [num for num in num_list if num % 2 == 0]
    return evens_in_list

def make_exclamation(sentence_list):
    exclamation_mark =[sentence + '!' for sentence in sentence_list]
    return exclamation_mark