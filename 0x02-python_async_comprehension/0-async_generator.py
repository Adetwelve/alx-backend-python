#!/usr/bin/env python3
""" Asynchronous generator """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ A coroutine that loops 10 times """
    for i in range(10):
        await asyncio.sleep(1)
        r = random.uniform(0, 10)
        yield r
