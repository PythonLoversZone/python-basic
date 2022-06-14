def find_boyfriend(height: int, rich: int, handsome: bool):
    if height >= 180 and rich >= 10000000 and handsome:
        print("我一定要嫁给他！！")
    elif height >= 180 or rich >= 10000000 or handsome:
        print("考虑一下。")
    else:
        print("滚！")


def ticket_system(month, age):
    TICK_PRICE = 100
    if month == 11 or month == 12 or month == 1:
        print("旺季")
        if 18 < age <= 60:
            print("票价为:", TICK_PRICE)
        elif age > 60:
            print("票价为:", TICK_PRICE / 3)
        elif age < 18:
            print("票价为:", TICK_PRICE / 2)
        else:
            print("请输入正确的年龄")
    else:
        print("淡季")
        if age > 18:
            print("票价为:", TICK_PRICE)
        else:
            print("票价为:", TICK_PRICE / 2)


h = 180
r = 10000000
hs = True

find_boyfriend(h, r, hs)
