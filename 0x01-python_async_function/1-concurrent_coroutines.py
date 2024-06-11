#!/usr/bin/env python3

''' Let's execute multiple coroutines at the same time with async '''

import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list:
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
