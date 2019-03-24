# 打折 discount
# 一件衣服95元， 若消费满300元，可以打八五折。
# 输入购买衣服数量，输出需要支付的金额（单位：元），保留两位小数


def m_count(num):
    total = 95 * num
    if total >= 300:
        total = total * 0.85
    return total


def main():
    num = int(input())
    if num < 0:
        print('invalid input')
        return False
    total = m_count(num)
    total = '%.2f' % total
    print(total)


if __name__ == '__main__':
    main()
