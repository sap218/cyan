#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:47:43 2019

@author: samantha
"""

import re
import click


def textinput(file):
    text = open(file, "r") 
    text = " ".join(text)
    text = text.replace("\n "," ")
    text = text.lower()
    return text

def conceptinput(lists):
    words = open(lists, "r") 
    toHighlight = []
    for concept in words:
        concept = concept.lower()
        toHighlight.append(concept[:-1])
    return toHighlight

def highlighting(text, concepts):
    colours = ["\033[1;36;40m", # cyan
               "\033[0;30;48m" # plain
               ] # http://ozzmaker.com/add-colour-to-text-in-python/
    for item in concepts:
        text = (re.sub((r'\b%s\b' % item), ('%s%s%s' % (colours[0], item, colours[1])), text)) # https://stackoverflow.com/questions/31697043/replace-exact-substring-in-python
    return text


@click.command()
@click.option('--file', help='Text file.')
@click.option('--lists', help='List of words.')
def main(file, lists):
    #file = "test_text.txt"
    text = textinput(file)

    #lists = "test_words.txt"
    concepts = conceptinput(lists)

    output = highlighting(text, concepts)
    print(output)

if __name__ == "__main__":
    main()

