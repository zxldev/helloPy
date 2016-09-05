# -*- coding: utf-8 -*-

def is_palindrome(n):
    str1 = str(n)
    str2 = str1[::-1]
    return str2 == str1


print(list(filter(is_palindrome,list(range(10000)))))