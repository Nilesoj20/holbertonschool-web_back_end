#!/usr/bin/env python3
"""list all documents in a collection"""


def list_all(mongo_collection):
    """ collectible to be listed """
    doc = mongo_collection.find()
    lista_colec = list(doc)
    if lista_colec:
        return lista_colec
    else:
        return []
