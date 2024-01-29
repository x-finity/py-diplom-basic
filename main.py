import json
import xF_vkapi as vk
import xF_yadapi as ya

def load_cfg(filename = 'config.json'):
    with open(filename) as f:
        cfg = json.load(f)
    return cfg

vk.test_function()
ya.test_function()