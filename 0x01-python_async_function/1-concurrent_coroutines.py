#!/usr/bin/env python3
""" An async function execute multiple
    coroutines at the same time with async
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ A couroutine that return random number n times """
    coroutine = [wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*coroutine)
    return sorted(result)
