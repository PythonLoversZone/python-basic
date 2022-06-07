def calc(a, b, o):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "/":
        return a / b
    if o == "*":
        return a * b
    else:
        print("wrong operator")


if __name__ == '__main__':
    print("please input first number")
    first = input()
    print("please input second number")
    second = input()
    print("please input operator")
    operator = input()
    print(calc(int(first), int(second), operator))
