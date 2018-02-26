
#ps7pr1.py

#Tayfun Turanligil




import random
import math

def throw_dart():
    """simulates a randomdart trow to a 2 by 2 square with a circile inside.
       returns True if dart hits circle."""
    
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    return (x**2 + y**2) <= 1.0

def for_pi(n):
    """calculates and returns an estimate of pi, using throw_dart() function."""

    number_trown = 0
    number_hit = 0
    pi = 0
    for x in range(n):
        
        if throw_dart():
            number_hit += 1

        print(number_hit, "hits out of ", end = '')
        number_trown += 1
        print(number_trown, "throws so that pi ", end = '')

        pi = (number_hit * 4)/number_trown
        print(pi)
        
    return pi

def while_pi(error):
    """takes a positive floating-point input error and returns the number of
       dart throws needed to produce an estimate of π that is less than error
       away from the “actual” value of π"""
    real_pi = math.pi
    number_trown = 0
    number_hit = 0
    pi = 0

    while abs(error) <= abs(real_pi - pi):
        if throw_dart():
            number_hit += 1

        print(number_hit, "hits out of ", end = '')
        number_trown += 1
        print(number_trown, "throws so that pi ", end = '')

        pi = (number_hit * 4)/number_trown
        print(pi)
    return number_trown
    
