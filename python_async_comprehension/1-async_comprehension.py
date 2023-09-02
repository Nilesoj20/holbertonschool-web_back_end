#!/usr/bin/env python3
""" Asynchronous compressions """
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """ corutina will collect 10 random numbers """
    async_num = [num async for num in async_generator()]
    return async_num
