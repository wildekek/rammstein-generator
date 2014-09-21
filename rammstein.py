#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = 'Du hast mich'
b = 'Du, du hast'+'\n'+a
c = a+' gefragt'
d = '\n'.join([b,b,''])
e = '\n'.join(['Willst du bis der Tod euch scheidet','Treurig sein für alle Tage?','Nein, nein!',''])
f = '\n'.join([d,b,a,'','\n'.join([c,c,c,'Und ich hab nichts gesagt','']),e,e])
print '\n'.join([d,f,f,e])