#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Return the total runtime """
    start = time.time()
    [await asyncio.gather(*[async_comprehension() for i in range(4)])]
    end = time.time()
    run_time = end - start
    return run_time
