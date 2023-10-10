#########
# Name: Kenneth Granger
# Assignment: Programming Assignment 01
# File: wordcount.py
# Purpose: Implement a word counter and a top word indicator
#
# Development Computer: Intel 4790k x64 16GB
# Operating System: Windows 11 21H2
# Environment: Python 3.11.4
# IDE: JetBrains PyCharm 2023.2.1
# Operational status: Functional
#########


# !/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
import string
import sys


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

#########
# Function: print_words()
# Parameters:
#  filename        A path to a file within the present working directory
# Returns: void
# Algorithm:
#   1. Output table header
#   2. For every word and count pair in the dictionary returned by get_words after sorting:
#   3.      Output the formatted word and count pair
# Assumptions: Assumes file exists
# Limitations: Some visual inconsistencies exist when dealing with punctuation
# Operational Status: Fully functional
#########
def print_words(filename):
    print('{1:{0}} {2}'.format(15, 'Words', 'Count'))
    # Sort on keys and print word with associated count
    for word, count in sorted(get_words(filename).items()):
        print('{1:{0}} {2}'.format(15, word, count))


#########
# Function: print_top()
# Parameters:
#  filename        A path to a file within the present working directory
# Returns: void
# Algorithm:
#   1. Output table header
#   2. For every word and count pair in the first 20 elements of the dictionary returned by get_words after sorting by
#   key, then reverse-sorting by value:
#   3.      Output the formatted word and count pair
# Assumptions: Assumes file exists
# Limitations: None known
# Operational Status: Fully functional
#########
def print_top(filename):
    print('{1:{0}} {2}'.format(15, 'Words', 'Count'))
    # Inner sort on keys, then sort reversed using lambda on values and print first 20 elems
    for word, count in sorted(sorted(get_words(filename).items()), key=lambda j: j[1], reverse=True)[:20]:
        print('{1:{0}} {2}'.format(15, word, count))


#########
# Function: get_words()
# Parameters:
#  filename        A path to a file within the present working directory
# Returns:
#  word_dict       A dictionary with words (keys) and counts (values) representing the occurrences of each word
# Algorithm:
#   1. Open the file and read lines into the raw word list
#   2. For each line in the raw word list:
#   3.      Lowercase the line and split each word into a list
#   4.      For each word in the line:
#   5.              Strip punctuation from the word and append it to the cleaned word list
#   6. For each word in the cleaned word list:
#   7.      If the word has not been seen before, add to the word dictionary
#   8.      Else, get the word from the dictionary and increment its count
#   9. Return the word dictionary
# Assumptions: Assumes file exists
# Limitations: Cannot strip punctuation from the middle of a string, so whole strings containing punctuation will
#              still be added as a separate entry to the dictionary.
# Operational Status: Fully functional
#########
def get_words(filename):
    file = open(filename, "r")
    word_list_raw = file.readlines()
    word_list = []

    # Split lines into words, then strip punctuation from words and append to word list
    for line in word_list_raw:
        line = line.lower().split()
        for word in line:
            word_list.append(word.strip(string.punctuation))

    # Append word to dictionary or increment count if previously seen
    word_dict = dict()
    for word in word_list:
        if word not in word_dict:
            word_dict.update({word: 1})
        else:
            word_dict[word] += 1

    return word_dict


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
