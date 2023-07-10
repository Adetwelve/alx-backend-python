#!/usr/bin/env python3
""" Asynchronous coroutine that takes a random integer argument and
    delay for some second and eventually returns a random float value
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ corountine function that takes returns random number """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
