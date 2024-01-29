import json
import xF_vkapi as vk
import xF_yadapi as ya

def load_cfg(filename = '__pycache__/config.json'):
    with open(filename) as f:
        cfg = json.load(f)
    return cfg

vk_token = load_cfg()['vk_token']
ya_token = load_cfg()['ya_token']
print(vk_token, ya_token)
# vk.test_function()
# ya.test_function()