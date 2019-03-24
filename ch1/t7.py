# 年份 year
# 输入年份，判断是否为闰年。如果是则输出yes，否则输出no


def is_leap_year(value):
    if value % 4 == 0 and value % 100 != 0:
        return 'yes'
    else:
        return 'no'


def main():
    year = int(input())
    if year < 0:
        return False
    result = is_leap_year(year)
    print(result)


if __name__ == '__main__':
    main()
