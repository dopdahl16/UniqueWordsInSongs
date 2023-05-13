#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:53:16 2023

@author: Daniel Opdahl
"""

import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from collections import deque
import FetchLyricsWithAZLyricsAPI
import FetchLyricsWithGPT



def GatherLyrics(url):
    lyricDump = ""
    table_df = ScrapeWikiTable(url)
    indices_of_songs_to_fetch = deque(table_df.index.tolist())

    fetch_lyrics_attempts_record = {}
    for i in table_df.index:
        fetch_lyrics_attempts_record[i] = 0

    while indices_of_songs_to_fetch:
        current_idx = indices_of_songs_to_fetch.popleft()

        artist = table_df['Artist(s)'][current_idx]
        title = table_df['Title'][current_idx]

        try:
            newLyrics = FetchLyricsWithAZLyricsAPI.FetchLyrics(artist, title)

            if newLyrics in lyricDump:
                raise Exception("API could not locate lyrics")
            print(f"{title} by {artist} added")
            print(f"{newLyrics}")
            lyricDump += '\n' + newLyrics

        except:
            print("Unable to fetch lyrics with AZLyrics API")
            fetch_lyrics_attempts_record[current_idx] += 1

            if fetch_lyrics_attempts_record[current_idx] >= 1:
                try:
                    newLyrics = FetchLyricsWithGPT.FetchLyrics(artist, title)
                    if not "\n" in newLyrics:
                        raise Exception("ChatGPT did not provide lyrics")
                    print(f"{title} by {artist} added")
                    print(f"{newLyrics}")
                    lyricDump += '\n' + newLyrics
                except:
                    print("Unable to fetch lyrics with ChatGPT API")
                    fetch_lyrics_attempts_record[current_idx] += 1
                    indices_of_songs_to_fetch.append(current_idx)
            time.sleep(10)

    return lyricDump


def ScrapeWikiTable(url):
    response=requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    indiatable=soup.find('table',{'class':"wikitable"})
    df=pd.read_html(str(indiatable))
    df=pd.DataFrame(df[0])
    print(df.head())
    return df