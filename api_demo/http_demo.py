'''
requests/json网络数据获取相关
'''
import json
import requests


def get_url():
    """
    获取baidu的status
    :return: 
    """
    url = "http://www.baidu.com"
    res = requests.get(url)
    print(res.url)
    print(res.status_code)


def get_json_demo():
    """
    获取json的方法
    :return: 
    """
    url = 'https://api.github.com/events'
    res = requests.get(url)
    print(res.url)
    print(res.status_code)

    res_str = res.text
    res_list = json.loads(res_str)
    print(len(res_list))
    for my_dict in res_list:
        print(my_dict['id'])


if __name__ == '__main__':
    get_url()
    get_json_demo()
    pass
