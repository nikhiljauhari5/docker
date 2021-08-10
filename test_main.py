import requests


#swapi calling
base_url = 'https://swapi.dev/api/people/1/'
resp = requests.get(base_url)

def test_first() :
    data = resp.json()
    assert data['name'] =='Luke Skywalker'

    data = resp.json()
    assert data['height'] == '172'

base_url2 = 'https://swapi.dev/api/planets/3/'
resp2 = requests.get(base_url2)

def test_third():
    data = resp2.json()
    assert data['name'] == 'Yavin IV'


def test_fourth():
    data = resp2.json()
    assert data['climate'] == 'temperate, tropical'