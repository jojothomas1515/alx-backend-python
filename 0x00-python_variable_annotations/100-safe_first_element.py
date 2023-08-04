#!/usr/bin/env python3
"""Module."""

# The types of the elements of the input are not know
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safe first element for."""
    if lst:
        return lst[0]
    else:
        return None
