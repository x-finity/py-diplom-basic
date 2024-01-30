import requests
import json
from pprint import pprint

def test_function():
    print('yad test function')

class YandexDiskAPIClient:
    base_url = 'https://cloud-api.yandex.net/v1/disk'
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return {
            'Authorization': self.token
        }

    def create_folder(self, folder_name):
        response = requests.put(f'{self.base_url}/resources', headers=self.get_headers(), params={'path': folder_name})
        if response.status_code == 409:
            print(f'Папка {folder_name} уже существует')
        # дополнить обработчик ошибок/статусов
        elif response.status_code == 201:
            print(f'Папка {folder_name} создана')

    def upload_file_by_url(self, file_url, file_name):
        api_upload_url = f'{self.base_url}/resources/upload'
        response = requests.post(api_upload_url, headers=self.get_headers(), params={'path': file_name, 'url': file_url})
        if response.status_code == 202:
            print(f'Файл {file_name} успешно загружен')
        if response.status_code == 409:
            print(f'Указанного пути {file_name} не существует. Cоздаем папку')
            self.create_folder(file_name.split('/')[0])
            self.upload_file_by_url(file_url, file_name)
        # pprint(response.json())

