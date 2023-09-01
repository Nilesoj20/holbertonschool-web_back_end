#!/usr/bin/env python3
""" regular function to return the task """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ return the task """
    tarea = asyncio.create_task(wait_random(max_delay))
    return tarea
