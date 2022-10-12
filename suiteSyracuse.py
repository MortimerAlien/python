#!/usr/bin/python3

def suiteSyracuse(n:int)->list[int]:
  suite = [n]
  while n > 1:
    if n % 2 == 0:
      n = n // 2
      suite.append(n)
    else:
      n = n * 3 + 1
      suite.append(n)
  return suite


print(suiteSyracuse(15))
