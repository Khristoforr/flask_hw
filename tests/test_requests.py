import requests
import pytest

URL = 'http://127.0.0.1:5000'


class TestSomething:
    def test404(self):
        response = requests.get(URL)
        assert response.status_code == 404

    def test_get_info(self):
        response = requests.get(f'{URL}/info')
        assert response.status_code == 200
        assert response.json()['status'] == 'ok'


