import requests
import pytest

def test_get_method():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    
    code = response.status_code
    
    assert code == 200