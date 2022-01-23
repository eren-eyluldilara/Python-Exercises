#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:00:15 2021

@author: eylul
"""

#setler sırasız , tekrar eden değerlerden oluşamaz,değiştirilebilri
#setler daha hızlı ve sadece unique değerler

s=set()
s

l=[1,"a","ali",123]
s=set(l)
s

t=("a","ali")
s=set(t)

ali="lütfen ata bakma uzaya git"
type(ali)
s=set(ali)
s

l=["ali","lütfen","ata","bakma","uzaya","git","git","ali","git"]
s=set(l)
s
len(s)
l[0]
s[0] #setler sırasız bu yüzden bu işlem yapılamaz index yok

