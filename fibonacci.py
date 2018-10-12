# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:53:02 2018

@author: Owner
"""
def fib(n):
    if n > 1:
    return fib(n-1) + fib(n-2)
    else:
    return 1
print(fib(4))