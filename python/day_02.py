# -*- coding: utf-8 -*-
"""
Created on 2025-12-02 21:38

@author: David Bahena
"""

# =============================================================================
# TODO Notes
# =============================================================================
# Search for invalid IDs only
# Invalid Ids are sequence of any digits repeated twice

from typing import List

example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

def has_invalid_id(product_id:str) -> List:
    """ Returns a list of invalid ID patterns """
    for ix, _ in enumerate(product_id):
        print(product_id[:0])

def get_invalid_ids(product_ids:List) -> int:
    """ Gets all invalid Ids """
    invalid_ids:List = list()
    for ix, product_id in enumerate(product_ids):
        first, second = product_id.split('-')
        invalid = has_invalid_id(product_id=first)
        break

invalid_ids = get_invalid_ids(product_ids=example.split(","))
print(f"Invalid Ids: {invalid_ids}")