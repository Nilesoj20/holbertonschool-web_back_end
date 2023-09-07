#!/usr/bin/env python3
"""  Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """ Python function that returns the school list """
    filtro = {"topics": topic}
    buscar = mongo_collection.find(filtro)
    lista = []
    for x in buscar:
        lista.append(x)
    return lista
