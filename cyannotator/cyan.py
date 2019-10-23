#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:47:43 2019

@author: samantha
"""

import re

text = input("Words:\t")
text = open(("%s.txt" % text), "r") 
text = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in text]
text = text.lower()

########################

words = input("Words:\t")
words = open(("%s.txt" % words), "r") 
toHighlight = []
for concept in words:
    concept = concept.lower()
    toHighlight.append(concept[:-1])

########################

# http://ozzmaker.com/add-colour-to-text-in-python/
colours = ["\033[1;31;40m",
           "\033[1;32;40m",
           "\033[1;33;40m",
           "\033[1;34;40m",
           "\033[1;35;40m",
           "\033[1;36;40m", # cyan
           "\033[1;37;40m",
           "\033[1;30;40m",
           "\033[0;30;48m" # plain
           ]

########################
########################

for item in toHighlight:
    text = (re.sub((r'\b%s\b' % item), ('%s%s%s' % (colours[5], item, colours[8])), text))
# https://stackoverflow.com/questions/31697043/replace-exact-substring-in-python

print(threads_list)

# outF = open("results.txt", "w")
# outF.write(threads_list)
# outF.close()

