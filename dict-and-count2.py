#!/usr/bin/env python
# -*- coding: utf-8 -*-
dosya = open("deneme.txt", "r") 
icerik = dosya.read().split()
yaz = {}
for kelime in icerik:
    if kelime not in yaz:
        yaz[kelime] = 1
    else:
        yaz[kelime] += 1
for key in yaz.keys():
   print ("%s %s " %(key , yaz[key] * '*'))

