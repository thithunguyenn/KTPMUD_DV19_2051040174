# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:30:49 2021

@author: Admin
"""

import pytest

def isPrimeNumber(n):
    if(n<2):
        return False
    else:
        for x in range(2,n):
            if(n%x ==0):
                return False
    return True

primeNumberArr = [3, 7, 13, 12]

count = 0
for member in primeNumberArr:
    if(isPrimeNumber(member)):
        count +=1
print("Tong cac  so nguyen to la: ", count)

def test_isPrimeNumber():
    assert isPrimeNumber(7) == True
def test_isPrimeNumber_1():
    assert isPrimeNumber(9) == False