#!/usr/bin/env python3
"""Module."""

from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Alot of annotation."""
    if key in dct:
        return dct[key]
    else:
        return default
