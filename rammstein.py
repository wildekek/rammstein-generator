#!/usr/bin/env python
# -*- coding: utf-8 -*-
lyrics = ['Du, du hast Mich gefragt und ich hab nichts gesagt', 'Willst du bis der Tod euch scheidet', 'Treu ihr sein für alle Tage?', 'Nein, nein!']

def makeLine(lyric='', start=0, stop=False):
    lyricParts = lyric.split(' ')
    if stop == False:
        stop = len(lyricParts)
    return ' '.join(lyricParts[start:stop]).capitalize()

for x in range(2):
    print makeLine(lyrics[0], 0, 3)+'\n'+makeLine(lyrics[0], 1, 4)
print
for x in range(2):
    for y in range(2):
        print makeLine(lyrics[0], 0, 3)+'\n'+makeLine(lyrics[0], 1, 4)
    print
    print makeLine(lyrics[0], 0, 3)
    for y in range(2):
        print makeLine(lyrics[0], 1, 4)
    print
    for y in range(3):
        print makeLine(lyrics[0], 1, 5)
    print makeLine(lyrics[0], 5, 10)+'\n'
    for y in range(2):
        print makeLine(lyrics[1], 0)+'\n'+makeLine(lyrics[2], 0)+'\n'+makeLine(lyrics[3], 0)+'\n'
print makeLine(lyrics[1], 0)+'\n'+makeLine(lyrics[2], 0)+'\n'+makeLine(lyrics[3], 0)