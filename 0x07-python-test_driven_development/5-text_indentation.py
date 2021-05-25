#!/usr/bin/python3
"""
This module identifies a predefined text, changes the characters ".", "?" and ":" by line breaks
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Arg:
        text (string): text to be indent  
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    switch = 0
    while i < len(text):
        if switch == 0:
            if text[i] == " ":
                i += 1
            else:
                switch = 1
        else:
            print(text[i], end="")
            if text[i] == "." or text[i] == "?" or  text[i] == ":":
                print("\n")
                i += 1
                switch = 0 
                continue
            i += 1
            