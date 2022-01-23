#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:13:56 2021

@author: eylul
"""

set1=set([1,3,5])
set2=set([1,2,3])
set1.difference(set2)
set2.difference(set1)


set1.symmetric_difference(set2)
set1-set2
set2-set1