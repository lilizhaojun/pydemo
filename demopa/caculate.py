'''这是一个计算器'''


def add(a, b):
    """
    这是一个加法函数
    :param a: 
    :param b: 
    :return: 
    """
    return a + b


def sub(a, b):
    """
    这是一个减法函数
    :param a: 
    :param b: 
    :return: 
    """
    return a - b


def cheng(a, b):
    """
    这是一个乘法
    :param a: 
    :param b: 
    :return: 
    """
    return a * b


def chu(a, b):
    """
    这是一个除法
    :param a: 
    :param b: 
    :return: 
    """
    assert b != 0
    return a / b


if __name__ == "__main__":
    # 加法
    c = add(1, 6)
    print('加法的运算结果')
    print(c)

    # 减法
    jf = sub(4, 3)
    print('减法的运算结果')
    print(jf)

    # 乘法
    cf = cheng(2, 4)
    print('乘法的运行结果')
    print(cf)

    # 除法
    cuf = chu(6, 2)
    print('除法的运行结果')
    print(cuf)

    ip = input('请输入值')
    print(ip)
