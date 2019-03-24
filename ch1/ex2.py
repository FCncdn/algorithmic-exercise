# 读取输入数据，根据读入数据计算结果


# 一次读取一行一个参数
def read_line():
    a = input('a:')
    print(a)


# 一次读取一行多个参数
def read_multi_lines():
    try:
        a, b = input('input two numbers:').split()
        print(type(a))
        print(type(b))
        print('first num:' + a + ', second num:' + b)
    except ValueError as e:
        print(e)
        print('input error')


# 一次读取一行多个参数并将参数转为整型
def read_multi_lines_to_int():
    try:
        a, b = map(int, input('input two numbers:').split())
        print(type(a))
        print(type(b))
        print('first num:' + str(a) + ', second num:' + str(b))
    except ValueError as e:
        print(e)
        print('input error')


def main():
    read_multi_lines_to_int()


if __name__ == '__main__':
    main()
