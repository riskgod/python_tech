#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = int(input( "please input an integer::"))

if x < 10:
    print(x)
else:
    print("this integer is more than 10")


words = ['cat', 'window', 'defenestrate']

for x in words:
    print(x, len(x))    

for x in range(10):
    print x

range(5, 10)

for x in range(len(words)): 
    print x

def fib(n):
    a = 0;
    b = 1;
    if a < n:
        print(a, end=' ')
    a, b = b, a+b


def say_hi(a, b = "hi"):
    if a =     