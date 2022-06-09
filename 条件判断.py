# 简单 if [else]

a = 1

if a > 5:
    print("hi")
else:
    print("hello")

# if ... else if ...else if ... else
if a < 0:
    print(1)
elif a > 3:
    print(2)
else:
    print(0)


def printnum9():
    total = 0
    for i in range(1, 101):
        if i % 9 == 0:
            print(i)
            total += i

    print("total is " + str(total))


printnum9()


def test_result(score):
    if score == 100:
        print("小明得到了一辆BWM")
    elif 80 < score <= 99:
        print("小明得到了一台iphone")
    elif 60 <= score <= 80:
        print("小明得到了一台ipad")
    else:
        print("什么奖励都没有，请再接再厉")


i = input("please input score")
s = int(i)
test_result(s)
