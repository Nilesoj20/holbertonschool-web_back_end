#!/usr/bin/env python3
""" Execution time for four parallel compressions """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ run async_comprehension four times in parallel """
    tiempo_inicio = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    tiempo_fin = time.perf_counter()
    total_time = tiempo_fin - tiempo_inicio
    return total_time
