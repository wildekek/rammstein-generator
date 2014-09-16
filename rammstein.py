#!/usr/bin/env python
# -*- coding: utf-8 -*-
lyrics = 'Du, du hast mich gefragt und ich hab nichts gesagt. Willst du bis der Tod euch scheidet Treu ihr sein für alle Tage ? Nein, nein!'

def ucfirst(string):
    output=string[0].upper()+string[1:]
    return output

a = lyrics[0:11]
b = ucfirst(lyrics[4:16])
ab = a+'\n'+b
abab = ab+'\n'+ab+'\n'
c = ucfirst(lyrics[4:24])
d = ucfirst(lyrics[25:50])
cd=c+'\n'+c+'\n'+c+'\n'+d+'\n'
efg = lyrics[52:87]+'\n'+lyrics[88:118]+'\n'+lyrics[119:130]+'\n'
ababcdefg = abab+'\n'+ab+'\n'+b+'\n'+'\n'+cd+'\n'+efg+'\n'+efg
print abab+'\n'+ababcdefg+'\n'+ababcdefg+'\n'+efg