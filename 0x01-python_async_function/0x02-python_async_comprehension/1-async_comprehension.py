import asyncio
import random
from typing import List

"""
Coroutine that generates random numbers asynchronously.
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]
