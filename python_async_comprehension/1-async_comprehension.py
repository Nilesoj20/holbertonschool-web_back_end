#!/usr/bin/env python3
""" Asynchronous compressions """
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """ corutina will collect 10 random numbers """
    async_num = [num async for num in async_generator()]
    return async_num
