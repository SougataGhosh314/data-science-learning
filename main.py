def divide():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = None
    try:
        z = x / y
        print(z)
    except ZeroDivisionError as ex:
        print(ex)
    except TypeError as ex:
        # print(ex)
        print("Exception type: " + type(ex).__name__)
    finally:
        print("division completed")


if __name__ == '__main__':
    divide()

