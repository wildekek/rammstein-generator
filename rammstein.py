#!/usr/bin/env python
# -*- coding: utf-8 -*-
a='Du hast mich'
b='Du, du hast'+'\n'+a
c=a+' gefragt'
def j(i):
 return '\n'.join(i)
d=j([b,b,''])
e=j(['Willst du bis der Tod euch scheidet','Treurig sein für alle Tage?','Nein, nein!',''])
f=j([d,b,a,'',j([c,c,c,'Und ich hab nichts gesagt','']),e,e])
print j([d,f,f,e])