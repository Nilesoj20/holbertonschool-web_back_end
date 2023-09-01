#!/usr/bin/env python3
""" Measures execution time """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """  Function that measure the total execution time """
    tiempo_inicio = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    tiempo_fin = time.perf_counter()
    total_time = tiempo_fin - tiempo_inicio
    return total_time / n
