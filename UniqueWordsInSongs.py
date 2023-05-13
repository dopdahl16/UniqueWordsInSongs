#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 6 2023

@author: danielopdhal
"""


import CleanUpLyrics
import GatherLyrics

def FindNumUniqueWords(file):
    unique_words = set()
    f = open(file, "r")
    for i in f:
        i = i.split()
        for j in i:
            unique_words.add(j)
    return unique_words

def WriteToFile(string_to_write, file_to_write_name):
    f = open(file_to_write_name, "a")
    f.write(string_to_write)
    f.close()
        

urls_to_scrape = []
record_files_names = []
url_stem = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"
file_name_stem = "LyricDump.txt"

for i in range(1980, 2023):
    year = str(i)
    urls_to_scrape.append(url_stem + year)
    record_files_names.append(year + file_name_stem)


for url in urls_to_scrape:
    WriteToFile(GatherLyrics.GatherLyrics(url), record_files_names[urls_to_scrape.index(url)])


for file in record_files_names:
    CleanUpLyrics.CleanLyrics(file)
    unique_words = FindNumUniqueWords(file)
    # print(g)
    print()
    print(str(file) + " " + str(len(unique_words)))