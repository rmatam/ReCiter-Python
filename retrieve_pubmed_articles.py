# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:46:19 2016

@author: Jie
"""
import pymongo
import requests

url = 'http://localhost:8080/reciter/retrieve/article/by/cwid'
def send_request(cwid):
    data = {'cwid': cwid}
    response = requests.get(url, data)
    print(response.json())

def main():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.reciter
    send_request('paa2013')

if __name__ == "__main__":
    main()
