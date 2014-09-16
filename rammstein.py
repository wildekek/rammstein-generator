#!/usr/bin/env python
# -*- coding: utf-8 -*-
lyrics = ['Du, du hast Mich gefragt und ich hab nichts gesagt', 'Willst du bis der Tod euch scheidet', 'Treu ihr sein für alle Tage?', 'Nein, nein!']

def makeLine(lyric='', start=0, stop=False):
    lyricParts = lyric.split(' ')
    if stop == False:
        stop = len(lyricParts)
    return ' '.join(lyricParts[start:stop]).capitalize()

def verse():
    text = ''
    for x in xrange(2):
        text += makeLine(lyrics[0], 0, 3)+'\n'
        text += makeLine(lyrics[0], 1, 4)+'\n'
    return text

def bridge1():
    text = makeLine(lyrics[0], 0, 3)+'\n'
    for x in xrange(2):
        text += makeLine(lyrics[0], 1, 4)+'\n'
    return text

def bridge2():
    text = ''
    for x in xrange(3):
        text += makeLine(lyrics[0], 1, 5)+'\n'
    text += makeLine(lyrics[0], 5, 10)+'\n'
    return text

def chorus():
    return makeLine(lyrics[1], 0)+'\n'+makeLine(lyrics[2], 0)+'\n'+makeLine(lyrics[3], 0)+'\n'

def song():
    return verse()+'\n'+verse()+'\n'+bridge1()+'\n'+bridge2()+'\n'+chorus()+'\n'+chorus()+'\n'+verse()+'\n'+bridge1()+'\n'+bridge2()+'\n'+chorus()+'\n'+chorus()+'\n'+chorus()

print song()