from flask_pymongo import PyMongo

from data.biografia import FEITOS


pym = PyMongo()


def configure_app(app):
    pym.init_app(app)


def add_data():
    try:
        ...
    except ImportError:
        print("import error")
        return

    doc = pym.db["biografia"]
    if find_all("biografia"):
        print("de boa já")
        return

    doc.insert_many(
        []
    )


def load_data(mongo_doc_name):
    doc = pym.db[mongo_doc_name]
    # doc.


def find_all(mongo_doc_name:str) -> dict:
    doc = pym.db[mongo_doc_name]
    return {_["component_name"]: _ for _ in doc.find()}


def delete_all(mongo_doc_name):
    doc = pym.db[mongo_doc_name]
    doc.delete_many({})
    _ = [_ for _ in doc.find()]
    return _ == [] or _
