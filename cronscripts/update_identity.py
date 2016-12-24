# -*- coding: utf-8 -*-
import requests


url = 'http://localhost:8080/reciter/ldap/retrieve/test'


def send_request():
    response = requests.get(url)
    print(response.json())


def main():
    send_request()


if __name__ == "__main__":
    main()
