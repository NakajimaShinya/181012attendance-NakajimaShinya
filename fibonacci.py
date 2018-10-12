# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:53:02 2018

@author: Owner
"""
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
result = []
for n in range(1,100):
    result.append(fib(n))
print(result)
    