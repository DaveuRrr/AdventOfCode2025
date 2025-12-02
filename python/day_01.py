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
combination = """L68
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
    position:int = 50
    password:int = 0
    for ix, rotation in enumerate(combination):
        clicks = int(findall(r'\d+', rotation)[0])
        if "L" in rotation:
            position = position - clicks
        if "R" in rotation:
            position = position + clicks

        position = position % 100 # Modulo Operator...feels like cheating. :(
        # print(position)
        if position == 0: password += 1

    return password


password = get_password(combination=combination.split("\n"))
print(f"Password: {password}") #TODO 3

# =============================================================================
# First Attempt...
# =============================================================================
# with open("./puzzle_input/day_01.txt") as puzzle:
#     for ix, rotation in enumerate(puzzle.readlines()):
#         clicks = int(findall(r'\d+', rotation)[0])
#         if clicks > 99: 
#             print(clicks, "vs", clicks % 99)
#             clicks = clicks % 99

#         if "L" in rotation:
#             position = position - clicks
#             if position < 0: position = position + 99

#         if "R" in rotation:
#             position = position + clicks
#             if position > 99: position = position - 99
        
#         if position < 0 or position > 99: raise
#         if position == 0: 
#             print(f"{position} Found!")
#             password += 1
#         else: print(position)

# =============================================================================
# Second Attempt
# =============================================================================
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