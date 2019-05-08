#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np

def even_magic_square(n):
    magic_square = [[0 for x in range(n)]
                      for y in range(n)]
    k = 1
    i, j = 0, n//2
    while k<= n**2:
        magic_square[i][j] = k
        k+=1
        ni, nj = (i-1)%n, (j+1)%n
        #print('ni ', ni, 'nj ', nj)
        if magic_square[ni][nj]:
            i+=1
        else:
            i, j = ni, nj
    return magic_square

def encrypt(text): #выглядит как будто кого-то тошнит
    result = ''
    l_text = len(text)
    n = math.ceil(math.sqrt(l_text))
    if n % 2 == 0:
        n+=1
    #print("Длина ", n)
    magic_square = even_magic_square(n)
    #print(magic_square)
    for i in range(len(magic_square)):
        for j in range(len(magic_square)):
            for k in range(l_text):
                if (k+1) == magic_square[i][j]:
                    #print(text[k])
                    magic_square[i][j] = text[k]
    #print(magic_square)
    for i in range(len(magic_square)):
        for j in range(len(magic_square)):
            if type(magic_square[i][j]) == int:
                magic_square[i][j] = '*'
                result+=magic_square[i][j]
            else:
                result += magic_square[i][j]
    #print(magic_square)
    return result

def decrypt(text):
    result = ''
    l_text = len(text)
    n = math.ceil(math.sqrt(l_text))
    if n % 2 == 0:
        n+=1
    #print("Длина ", n)
    text_m = []
    magic_square = even_magic_square(n)
    i = 0
    while i < len(text):
    # for i in range(len(text)):
        #print(text[i:i+n])
        text_m.append(list(text[i:i+n]))
        i = i+n
    k = 1
    while k <= n**2:
        for i in range(len(magic_square)):
            for j in range(len(magic_square)):
                if k == magic_square[i][j]:
                    result+=text_m[i][j]
        k+=1
    result = result.rstrip('*')
    return result


#
# # Works only when n is odd
# text = input("Ввести текст ")
# key = int(input("Ключ 1 или ключ 2 "))
# ms = encrypt(text, key)
# print("Зашифровано ", ms)
# rs = decrypt(ms, key)
# print("Дешифровано ", rs)
