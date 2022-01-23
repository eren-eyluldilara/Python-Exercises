#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:54:43 2021

@author: eylul
"""

sozluk={"REG":"Regresyon modeli",
        "LOJ":"Lojistik Regresyon",
        "CART":"Classification and Reg"}
sozluk["GBM"]="Gradient Boosting Mac"
sozluk
sozluk["REG"]="Çoklu Doğrusal Regresyon"
sozluk
sozluk[1]="Yapay Sinir Ağları"
sozluk

l=[1]
l
sozluk[l]="Yeni Bir Şey"
#diclerde keyler sabit veri yapıları ile oluşturulur
#string ve int sabit olduğu için key olur
#liste sabit değil değiştirilebilir, bu yüzden key olamaz

t=("tuple",)
sozluk[t]="yeni bir şey"
#key tuple olabilir çünkü tuplelar değiştirilemez
