#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random


async def async_generator():
    """ coroutine called async_generator that does not require arguments """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.random()
