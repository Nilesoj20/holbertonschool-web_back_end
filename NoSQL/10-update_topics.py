#!/usr/bin/env python3
""" Change school subjects """


def update_topics(mongo_collection, name, topics):
    """ change all topics in a document """
    filtro = {"name": name}
    remplazo = {
            "$set": {"topics": topics}}
    actualizacion = mongo_collection.update_many(filtro, remplazo)
