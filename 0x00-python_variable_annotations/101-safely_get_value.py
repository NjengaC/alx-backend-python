#!/usr/bin/env python3
"""
This module provides a function to safely retrieve values from a dictionary
with a specified default value.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary to retrieve the value from.
        key (Any): The key whose value is to be retrieved.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if the key exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

