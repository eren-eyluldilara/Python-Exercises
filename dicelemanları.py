#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:48:50 2021

@author: eylul
"""

sozluk={"REG":"Regresyon modeli",
        "LOJ":"Lojistik Regresyon",
        "CART":"Classification and Reg"}
sozluk[0] #key error hatası çünkü dicler sırasız
sozluk["REG"]
sozluk["LOJ"]

sozluk={"REG":{"RMSE":10,
               "MSE":20,
               "SSE":30},
        
        "LOJ":{"RMSE":10,
               "MSE":20,
               "SSE":30},
        
        "CART":{"RMSE":10,
                "MSE":20,
                "SSE":30}}

sozluk
sozluk["REG"]["SSE"]
