import requests
import json
from pprint import pprint

def test_function():
    print('vk test function')

class VKAPIClient:
    api_base_url = 'https://api.vk.com/method'
    def __init__(self, token, user_id = '86301318'):
        self.token = token
        self.user_id = user_id
    
    def _build_url(self, method):
        return f'{self.api_base_url}/{method}'
    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.199'
        }
    def get_proile_photos_info(self):
        params = self.get_params()
        params.update({'owner_id': self.user_id, 'album_id': 'profile'})
        response = requests.get(self._build_url('photos.get'), params=params)
        return response.json()