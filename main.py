import json
from datetime import datetime
from pprint import pprint
import xF_vkapi as vk
import xF_yadapi as ya

def load_cfg(filename = 'config.json'):
    with open(filename) as f:
        cfg = json.load(f)
    return cfg

vk_token = load_cfg()['vk_token']
ya_token = input('ya token (Enter for load from config): ')
if ya_token == '':
    ya_token = load_cfg()['ya_token']

user_id = input('user_id (Enter default (4957073): ') #4957073 86301318
if user_id == '':
    user_id = '4957073'
# print(user_id)
vk_client = vk.VKAPIClient(vk_token, user_id)
ya_client = ya.YandexDiskAPIClient(ya_token)

# pprint(vk_client.get_proile_photos_info())
def get_photo_url_n_likes(quantity = 5):
    """
    Get photo URLs and their respective like counts from VK client.

    Args:
        quantity (int): The number of photos to retrieve. Defaults to 5.

    Returns:
        tuple: A tuple containing a list of photo URLs, like counts, epoch dates and photo types.
        set: A set of unique like counts.
    """
    photo_info = vk_client.get_proile_photos_info()
    photos = photo_info.get('response', {})['items']
    # pprint(photos)
    photo_tuples = []
    likes_pool = []
    n = 0
    if len(photos) < quantity: quantity = len(photos)
    while n < quantity:
        photo_tuples.append((photos[n].get('sizes', [])[-1]['url'], 
                             vk_client.get_likes_count(photos[n].get('id', 0)), 
                             photos[n].get('date', 0),
                             photos[n].get('sizes', [])[-1]['type']))
        likes_pool.append(vk_client.get_likes_count(photos[n].get('id', 0)))
        n += 1
    uniq_likes_pool = set([i for i in likes_pool if likes_pool.count(i) > 1])
    return photo_tuples, uniq_likes_pool

def backup_photos(vk_id, quantity = 5):
    def progress_bar(n, width = 50, file = ''):
        percent = n / quantity
        filled = int(width * percent)
        bar = '*' * filled + '-' * (width - filled)
        print(f'\r[{bar}] {percent * 100:.2f}% {file}', end = '')
    def fill_json(filename, size):
        return [{'filename': filename, 'size': size}]
    def upload_photo_and_json(filename, type):
        ya_client.upload_file_by_url(url, f'{filename}.jpg')
        ya_client.upload_var(f'{filename}.json', json.dumps(fill_json(f'{filename}.jpg', type)))
    
    url_and_likes, likes_pool = get_photo_url_n_likes(quantity)
    url_and_likes.sort(key=lambda x: x[1])
    n = 0
    progress_bar(n)
    for url, likes, date, type in url_and_likes:  
        if likes in likes_pool:
            date = datetime.fromtimestamp(date).strftime('%Y-%m-%d_%H-%M-%S')
            # print(date)
            filename = f'backup_{vk_id}/{likes}-{date}'
            upload_photo_and_json(filename, type)
        else:
            filename = f'backup_{vk_id}/{likes}'
            upload_photo_and_json(filename, type)
        progress_bar(n, file = f'{filename}.jpg')
        n += 1
    progress_bar(quantity)

backup_photos(user_id)