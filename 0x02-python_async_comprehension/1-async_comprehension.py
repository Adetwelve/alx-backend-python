#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """ A function that collect random number """
    return [a async for a in async_generator()]
