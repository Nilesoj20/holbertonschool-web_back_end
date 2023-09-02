#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
import typing

async def async_generator() -> typing.Generator[float, None, None]:
    """ coroutine called async_generator that does not require arguments """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.random()
