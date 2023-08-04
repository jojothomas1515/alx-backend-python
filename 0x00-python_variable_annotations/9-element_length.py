#!/usr/bin/env python3
"""Module."""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return sequence."""
    return [(i, len(i)) for i in lst]
