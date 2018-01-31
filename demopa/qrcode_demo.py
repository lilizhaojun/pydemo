'''
生成二维码
'''
import qrcode
from PIL import Image


def set_list():
    """
    生成名单列表
    :return: 
    """
    output_file = open('name_list', mode='w', encoding='utf-8')
    for names in range(20):
        print(names)
        output_file.writelines('张小%s,13392946407' % str(names) + '\n')
    output_file.close()


def get_list():
    """
    得到每个数据，并生成二维码保存在本地文件夹
    :return: 
    """
    num = 1
    input_file = open('name_list', mode='r', encoding='utf-8')
    for line in input_file.readlines():
        img = qrcode.make(line)
        img.save('/Users/lizhaojun/profession/py_test/pydemo/demopa/qrcodes/%s.jpg' % num)
        num += 1


if __name__ == '__main__':
    in_file = open('name_list', mode='r', encoding='utf-8')
    # 如果name_list为空，则重新建立
    str_name = in_file.readlines()
    if len(str_name) == 0:
        set_list()
    get_list()
