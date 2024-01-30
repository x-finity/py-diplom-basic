import json
from pprint import pprint
import xF_vkapi as vk
import xF_yadapi as ya

def load_cfg(filename = '__pycache__/config.json'):
    with open(filename) as f:
        cfg = json.load(f)
    return cfg

vk_token = load_cfg()['vk_token']
ya_token = load_cfg()['ya_token']

#user_id = input('user_id: ') #4957073 86301318
vk_client = vk.VKAPIClient(vk_token)
ya_client = ya.YandexDiskAPIClient(ya_token)

# pprint(vk_client.get_proile_photos_info())
def get_vk_photo_url(quantity = 5):
    photos = vk_client.get_proile_photos_info().get('response', {})['items']
    # pprint(photos)
    urls = []
    n = 0
    if len(photos) < quantity:
        quantity = len(photos)
    while n < quantity:
        urls.append(photos[n]['sizes'][-1]['url'])
        n += 1
    return urls

# print(get_vk_photo_url())
test_img_url = 'https://cdnn21.img.ria.ru/images/148651/95/1486519535_0:55:1100:1155_1920x0_80_0_0_29a1904b98600954160c6658aa820868.jpg'
# ya_client.create_folder(2)
# ya_client.upload_file(test_img_url, 'test_img.jpg')

file_path = '123/test_img.jpg'
print(file_path.split('/')[0])