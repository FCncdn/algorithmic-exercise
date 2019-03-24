# 输入华氏温度f，输出对应摄氏温度c，保留三位小数


def f_to_c(value):
    return ((value - 32)*5)/9


def main():
    f_value = float(input())
    c_value = f_to_c(f_value)
    c_value = '%.3f' % c_value
    print(c_value)


if __name__ == '__main__':
    main()
