import requests
# import pytest

def post_object():
    obj = {
        "name": "Apple MacBook Pro 16",
        "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
        }
    }

    response = requests.post('https://api.restful-api.dev/objects',json = obj).json()
    print(response)

def get_object():
    response = requests.get('https://api.restful-api.dev/objects/ff8081819782e69e01990b2a51d82201',json = object).json()
    print(response)

def put_object():
    obj = {
        "name": "Apple MacBook Pro 16",
        "data": {
          "year": 2020,
          "price": 1999.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
        }
    }
    response = requests.put('https://api.restful-api.dev/objects/ff8081819782e69e01990b2a51d82201',json = obj).json()
    print(response)

def delete_object():
    requests.delete('https://api.restful-api.dev/objects/ff8081819782e69e01990b2a51d82201',json = obj).json()