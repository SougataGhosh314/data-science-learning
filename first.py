# import matplotlib
# import math
import calendar
import modules.area_functions as f


def operations():
    # print(calendar.month(2022, 2))
    print("Area of square with side 5: ", f.area_square(5), "square units")
    print("Area of rectangle with length 5, width 6: ", f.area_rectangle(5, 6), "square units")
    print("Area of triangle with base 5, height 6: ", f.area_triangle(5, 6), "square units")
    # print(f'Hi, {name}')
    # print(math.sqrt(16))
    # print(dir(math))


if __name__ == '__main__':
    operations()
