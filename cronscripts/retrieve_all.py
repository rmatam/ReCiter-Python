
import pymongo


def main():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.reciter.authenticate('reciter', 'reciter123', mechanism='SCRAM-SHA-1')
    db = client.reciter
    cursor = db.identity.distinct("cwid")

    for document in cursor:
        if document is not None and len(document) > 0:
            print(document)


if __name__ == "__main__":
    main()