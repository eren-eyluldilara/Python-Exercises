#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:20:43 2021

@author: eylul
"""

set1=set([7,8,9])
set2=set([5,6,7,8,9,10])

#iki kümeninin kesişiminin boş olup olmaması
set1.isdisjoint(set2)

#bir kümenin bütün elemanlarının başka bir küme içinde yer alıp almadığı
set1.issubset(set2)

#bir kümenin diğer bir kümeyi kapsayıp kapsamadığı
set2.issuperset(set1)
set1.union(set2)
