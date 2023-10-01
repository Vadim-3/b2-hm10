import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://bezhukvadim56:VVBXIIBVTdILQpyb@cluster0.ssxsfik.mongodb.net/?retryWrites=true&w=majority")

db = client.dz_10

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    author = db.authors.find_one({"name": quote["author"]})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'author': ObjectId(author['_id']),
            'tags': quote['tags'],
        })
