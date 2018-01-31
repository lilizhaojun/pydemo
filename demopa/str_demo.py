


def get_path():
    """
    根据文件的路径，获取文件的名称
    :return: 
    """
    path = '/home/anr/mytest'
    alist = path.split('/')
    print(alist[-1])

def get_join():
    """
    拼接
    :return: 
    """
    a = ['lili','Zhangming','Wangwu']
    b = '和'.join(a)
    print(b)
    print(b.upper())
    print(b.lower())

def get_strip():
    """
    去除空格
    :return: 
    """
    a = ' abc def jjj '
    b = a.strip()
    print(b)
    print(a.lstrip())

def get_change():
    """
    改变驼峰
    :return: 
    """
    #num = 0
    str_later = ''
    str_l = 'iLoveYou'
    print(len(str_l))
    for num in range(len(str_l)):
        if ord(str_l[num]) >= 90 :
            str_later += str_l[num]
        else:
            str_later += ('_'+ str_l[num].lower())
        num += 1
    print(str_later)



if __name__ =='__main__':
    #get_path()
    #get_join()
    #get_strip()
    get_change()