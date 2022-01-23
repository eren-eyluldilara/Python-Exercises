#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:40:37 2021

@author: eylul
"""

#dictionary  kapsayıcı,sırasız ,değiştirilebilir
#liste kapsayacı,sıralı,değiştirilebilri
#tuple kapsayıcı,sıralı,değiştirilemez

sozluk={"REG":"Regresyon modeli",
        "LOJ":"Lojistik Regresyon",
        "CART":"Classification and Reg"}
len(sozluk)

sozluk={"REG":["RMSE",10],
        "LOJ":["MSE",20],
        "CART":["SSE",30]}
sozluk