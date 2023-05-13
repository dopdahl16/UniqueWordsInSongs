import re

def CleanLyrics(file_to_open_name):
    f = open(file_to_open_name, "r")
    all_lyrics = f.read()
    all_lyrics = all_lyrics.replace('(', '')
    all_lyrics = all_lyrics.replace(')', '')
    all_lyrics = re.sub("\(.*?\)|\[.*?\]","", all_lyrics)
    all_lyrics = all_lyrics.replace('?', '')
    all_lyrics = all_lyrics.replace('.', '')
    all_lyrics = all_lyrics.replace(',', '')
    all_lyrics = all_lyrics.replace('!', '')
    f.close()
    f = open(file_to_open_name, "w")
    f.write(all_lyrics)
    f.close()