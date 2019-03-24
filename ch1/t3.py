# 连续和 sum
# 输入正整数n， 输出1 + 2 + ... + n的值


def m_sum(value):
    result = ((1 + value) * value) / 2
    return result


def main():
    value = int(input())
    if value <= 0:
        print('invalid input')
        return False
    sum_value = m_sum(value)
    print(sum_value)
    return sum_value


if __name__ == '__main__':
    main()
