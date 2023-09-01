#!/usr/bin/env python3
""" Let's run multiple coroutines at the same time with async """
import asyncio
import typing
modulo_importar = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ return the list of all delays """
    retrasos = []
    tarea = [modulo_importar(max_delay) for x in range(n)]
    tareas_completa = asyncio.as_completed(tarea)
    for t in tareas_completa:
        esperar = await t
        retrasos.append(esperar)

    return sorted(retrasos)
