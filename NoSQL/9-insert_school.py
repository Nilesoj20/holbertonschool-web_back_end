#!/usr/bin/env python3
""" Inserting a document in Python """


def insert_school(mongo_collection, **kwargs):
    """  insert a new document in a kwargs-based collection """
    documento = {}
    for clave, valor in kwargs.items():
        documento[clave] = valor
    insertar = mongo_collection.insert_one(documento)
    if insertar.acknowledged:
        return insertar.inserted_id
    return {}
