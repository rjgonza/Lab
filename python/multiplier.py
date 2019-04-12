#!/usr/bin/python
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
