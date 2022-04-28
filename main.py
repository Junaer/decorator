import time
import requests

def loger_decorator(path):
    def _loger_decorator(some_function):
        def log_dec(*args, **kwargs):
            start_time = []
            result = some_function(*args, **kwargs)
            start_time.append([time.asctime(), some_function.__name__, args, kwargs, result])
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{start_time}\n')
            return result
        return log_dec
    return _loger_decorator

TOKEN = 2619421814940190
hero_list = ['Hulk', 'Captain America', 'Thanos']

def get_id(heros):
    id_list = []
    for hero in hero_list:
        url = f'https://superheroapi.com/api/{TOKEN}/search/{hero}'
        response = requests.get(url)
        id_list.append(response.json()['results'][0]['id'])
    return id_list

def _get_hero_dict_():
    i = []
    for id in get_id(hero_list):
        url = f'https://superheroapi.com/api/{TOKEN}/{id}/powerstats'
        response = requests.get(url)
        i.append(response.json()['intelligence'])
    hero_dict = dict(zip(hero_list, i))
    return hero_dict



@loger_decorator('log.txt')
def get_top_1_intelligence():
    hero_dict = _get_hero_dict_()
    inte = 0
    valu = 0
    name = ''
    for key, value in hero_dict.items():
        valu = int(value)
        if int(inte) < valu:
            inte = value
            name = key
        else:
            pass
    result = (f'В самый умный с Тиной Канделаки победил {name} с результатом {inte}')
    return result

get_top_1_intelligence()







