import requests
import pytest

@pytest.fixture()
def obj_id():
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
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response}')


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
    response = requests.post('https://api.restful-api.dev/objects', json=obj).json()
    assert response['name'] == obj['name']
    assert response['data']['year'] == obj['data']['year']
    assert response['data']['price'] == obj['data']['price']
    assert response['data']['CPU model'] == obj['data']['CPU model']
    assert response['data']['Hard disk size'] == obj['data']['Hard disk size']

def test_get_object(obj_id):
    print(obj_id)
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert response['id'] == obj_id

def test_put_object(obj_id):
    obj = {
        "name": "Apple MacBook Pro 16",
        "data": {
          "year": 2020,
          "price": 1999.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}',json=obj).json()
    assert response['name'] == obj['name']
    assert response['data']['year'] == obj['data']['year']
    assert response['data']['price'] == obj['data']['price']
    assert response['data']['CPU model'] == obj['data']['CPU model']
    assert response['data']['Hard disk size'] == obj['data']['Hard disk size']

def test_delete_object(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404