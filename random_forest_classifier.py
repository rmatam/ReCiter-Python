# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:46:19 2016

@author: Jie
"""
import pymongo

from sklearn.ensemble import RandomForestClassifier
# from numpy import genfromtxt, savetxt
from numpy import savetxt
from sklearn.cross_validation import train_test_split


def main():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.reciter
    # print(db.name)
    # print(db.pubmedarticle)
    # print(db.pubmedarticle.find_one())

    cursor = db.pubmedarticlefeature.find({"cwid": "aas2004"})

    target = []
    train = []
    for document in cursor:
        for feature in document['features']:
            training_data = []
            train.append(training_data)
            for key, value in feature.items():
                if key != 'pmid' and key != 'isGoldStandard':
                    training_data.append(value)
                elif key == 'isGoldStandard':
                    target.append(value)

    # print(target)
    # print(train)
    X_train, X_test, y_train, y_test = train_test_split(train, target, test_size=0.33, random_state=42)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    #    target = [x[0] for x in dataset]
    #    train = [x[1:] for x in dataset]
    #    test = genfromtxt(open('Data/test.csv','r'), delimiter=',', dtype='f8')[1:]
    #
    #    #create and train the random forest
    #    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    #    rf = RandomForestClassifier(n_estimators=100)
    #    rf.fit(train, target)
    #
    # savetxt('submission2.csv', rf.predict(X_test), delimiter=',', fmt='%f')
    score = rf.score(X_test, y_test)
    print(score)


if __name__ == "__main__":
    main()
