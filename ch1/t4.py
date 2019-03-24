# 正弦和余弦（sin和cos）
# 输入正整数n（n<360) 输出n度的正弦、余弦值
import math


def main():
    value = int(input())
    if value > 360 or value < 0:
        print('invalid input')
        return False
    value_cos = math.cos(math.radians(value))
    value_sin = math.sin(math.radians(value))
    print('%.3f' % value_cos)
    print('%.3f' % value_sin)


if __name__ == '__main__':
    main()
