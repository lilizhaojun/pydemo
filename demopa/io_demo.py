'''
输入输出
'''


def hello():
    """
    hello_world
    :return: 
    """
    print('hello world')


def io_input():
    """
    输入输出
    :return: 
    """
    a = input('请输入一段文字或数字：')
    print(a)


def file_io_input():
    """
    文件的输入输出
    :return: 
    """
    str_line = ''
    input_file = open('input',mode='r',encoding='utf-8')
    for line in input_file.readlines():
        str_line += line
    print(str_line)

    output_file = open('output',mode='a',encoding='utf-8')
    output_file.writelines(str_line)

    for i in range(100):
        output_file.writelines(str(i)+'\n')

    output_file.writelines('这是文件输出的内容')

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    #io_input()
    file_io_input()
