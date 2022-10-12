#!/usr/bin/python3

def suiteSyracuse(n):
  suite = [n]
  while n > 1:
    if n % 2 == 0:
      suite.append(n:= n//2)
    else:
      suite.append(n:=n*3+1)
  return suite
print(suiteSyracuse(15))
