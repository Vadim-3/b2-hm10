from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        'mongodb+srv://bezhukvadim56:VVBXIIBVTdILQpyb@cluster0.ssxsfik.mongodb.net/?retryWrites=true&w=majority')

    db = client.dz_10
    return db
