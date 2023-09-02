#!/usr/bin/env python3
""" Execution time for four parallel compressions """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ run async_comprehension four times in parallel """
    tiempo_actual = asyncio.get_event_loop()
    tiempo_inicio = tiempo_actual.time()
    tareas = [async_comprehension() for x in range(0, 5)]
    resultado = await asyncio.gather(*tareas)
    tiempo_fin = tiempo_actual.time()
    total_time = tiempo_fin - tiempo_inicio
    return total_time
