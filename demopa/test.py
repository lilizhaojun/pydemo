'''鸡蛋问题'''


def egg_chick():
    """
    鸡蛋数量
    :return: 
    """
    out_file_name='output'
    out_file=open(out_file_name,mode='a')
    out_file.writelines('-------------鸡蛋智力问题的答案--------------'+'\n')
    x = range(5000)

    for egg_total in x:
        if (egg_total % 4) != 1:
            continue
        if (egg_total % 5) != 4:
            continue
        if (egg_total % 6) != 3:
            continue
        if (egg_total % 7) != 5:
            continue
        if (egg_total % 8) != 1:
            continue
        if (egg_total % 9) != 0:
            continue

        print(egg_total)
        out_file.writelines(str(egg_total)+'\n')

    print('author method')



    r = range(5000)

    for egg_tt in r:
        if (egg_tt % 4) == 1 and (egg_tt % 5) == 4 and (egg_tt % 6) == 3 and (egg_tt % 7) == 5 and (
            egg_tt % 8) == 1 and (egg_tt % 9) == 0:
            print(egg_tt)


    out_file.close()



if __name__ == '__main__':
    egg_chick()
