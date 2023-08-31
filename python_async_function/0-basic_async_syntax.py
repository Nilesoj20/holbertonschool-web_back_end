#!/usr/bin/env python3
"""  asynchronous function in Python """
import random
import asyncio


async def wait_random(max_delay=10):
    """  function that expects a random delay """
    aleatorio = random.uniform(0, max_delay)
    await asyncio.sleep(aleatorio)
    return aleatorio
