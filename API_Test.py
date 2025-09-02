import requests
# import pytest

def create_object():
    obj = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=obj).json()
    return response['id']


def test_post_object():
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
    assert response['name'] == obj['name']
    assert response['year'] == obj['year']
    assert response['price'] == obj['price']
    assert response['CPU model'] == obj['CPU model']
    assert response['Hard disk size'] == obj['Hard disk size']

def test_get_object():
    obj_id = create_object()
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}',json = obj).json()
    assert response['id'] == obj_id

def test_put_object():
    obj_id = create_object()
    obj = {
        "name": "Apple MacBook Pro 16",
        "data": {
          "year": 2020,
          "price": 1999.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}',json = obj).json()
    assert response['name'] == obj['name']
    assert response['year'] == obj['year']
    assert response['price'] == obj['price']
    assert response['CPU model'] == obj['CPU model']
    assert response['Hard disk size'] == obj['Hard disk size']

def test_delete_object():
    obj_id = create_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}',json = obj)
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}',json = obj)
    assert response.status_code == 404

