# 平均数（average）
# 输入3个整数，输出他们的平均值，保留3位小数


def average(value1, value2):
    ave = (value1 + value2)/2
    ave = '%.3f' % ave
    return ave


def main():
    try:
        value1, value2 = map(float, input().split())
    except ValueError as e:
        return False
    ave = average(value1, value2)
    print(ave)


if __name__ == '__main__':
    main()
