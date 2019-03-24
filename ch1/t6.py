# 三角形
# 输入三角形的三条边的长度值（均为正整数），判断是否能为直角三角形的三个边长
# 如果可以，则输出yes，如果不能，则输出no。如果无法形成三角形，输出not 啊triangle


def is_right_triangle(a, b, c):
    triangle = [a, b, c]
    if triangle[0] < triangle[1]:
        tmp = triangle[1]
        triangle[1] = triangle[0]
        triangle[0] = tmp
    if triangle[0] < triangle[2]:
        tmp = triangle[2]
        triangle[2] = triangle[0]
        triangle[0] = tmp
    if triangle[1] + triangle[2] < triangle[0]:
        print('not a triangle')
        return False
    if triangle[1] ** 2 + triangle[2] ** 2 == triangle[0] ** 2:
        print('yes')
    else:
        print('no')


def main():
    a, b, c = map(int, input().split())
    if a <= 0 or b <= 0 or c <= 0:
        return False
    is_right_triangle(a, b, c)


if __name__ == '__main__':
    main()
