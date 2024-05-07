#!/usr/bin/env python3
"""
def index_range helper function
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing the start index and end index
    corresponding to the range of indexes to return in a list for the
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
