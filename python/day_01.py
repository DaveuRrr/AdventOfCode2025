# -*- coding: utf-8 -*-
"""
Created on 2025-12-01 22:48

@author: David Bahena
"""

# =============================================================================
# TODO Notes
# =============================================================================
# - Dial is 0-99
# - Rotation or Direction is L (Left/Lower) or R (Right/Higher)
# - Each Click is 1 int
# - Dial starts at 50

# Actual password is n times the dial is at 0 after any rotation squences.

# =============================================================================
#
# =============================================================================
# Python Standard Library 3.11
from re import findall
from typing import List

# =============================================================================
# Example Input
# =============================================================================
example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

# =============================================================================
#
# =============================================================================
def get_password(combination:List) -> int:
    """ Gets Password from Day 01 Part 01 """
    position:int = 50
    password:int = 0
    for ix, rotation in enumerate(combination):
        clicks = int(findall(r'\d+', rotation)[0])
        if "L" in rotation:
            position = position - clicks
        if "R" in rotation:
            position = position + clicks

        position = position % 100 # Modulo Operator...feels like cheating. :(
        # print(f"{rotation} --> {position}")
        if position == 0: password += 1

    return password

password = get_password(combination=example.split("\n"))
print(f"Example Password: {password}") # TODO Must equal 3

with open("./puzzle_input/day_01.txt") as puzzle:
    password = get_password(combination=puzzle.readlines())
    print(f"Password: {password}")

# =============================================================================
# Thoughts
# =============================================================================
# What if we didn't have the modulo operator? We would need the following
# Floor Division
#   quotient = dividend // divisor
# Return Remainder
#   remainder = dividend - (quotient * divisor)

# Since we are doing rotations we are grabbing what is left from the dial,
# with numbers only between 0 - 99 we would need to use 100 as the modulo since
# there are 100 numbers we are dealing with.  

# =============================================================================
# Part 2
# =============================================================================
def get_any_clicks(combination:List) -> int:
    """ Gets Any Clicks that point to 0 """
    position:int = 50
    password:int = 0
    for ix, rotation in enumerate(combination):
        clicks = int(findall(r'\d+', rotation)[0])
        dial = position
        if "L" in rotation:
            position = position - clicks
            # Any Clicks...
            for x in range(clicks):
                dial = dial - 1
                if dial < 0: dial = 99
                if dial == 0:
                    # print("--> 0 Once!")
                    password += 1

        if "R" in rotation:
            position = position + clicks
            # Any Clicks...
            for x in range(clicks):
                dial = dial + 1
                if dial > 99: dial = 0
                if dial == 0: 
                    # print("--> 0 Once!")
                    password += 1
            
        # Updates to the absolute position
        position = position % 100
        # print(f"{rotation} --> {position}")
    
    return password

password = get_any_clicks(combination=example.split("\n"))
print(f"Any Clicks: {password}") # TODO Must equal 6

with open("./puzzle_input/day_01.txt") as puzzle:
    password = get_any_clicks(combination=puzzle.readlines())
    print(f"Any Clicks: {password}")