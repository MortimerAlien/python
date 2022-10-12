#!/usr/bin/python3
def factorielleN(n):
    facto = 1
    for i in range(n,1,-1):
        facto *= i
    return facto
