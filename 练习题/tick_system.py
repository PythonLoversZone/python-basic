# 终极编程测试（分类判断） `练习题`

# 设计一个出票系统，根据淡旺季来年龄来计算票价

# - 旺季： (11月-1月)
# - 成人（`18-60`)：60
#     - 儿童（`< 18`）：半价
#     - 老人(`> 60`)：1/3

#     - 其他时间为淡季：
#     - 成人(`18~`)：全价
#     - 其他：半价

# 票价 100元
TICK_PRICE = 100

month = 0
age = 0


monthStr = input("请输入月份：")
ageStr = input("请输入年龄：")

month = int(monthStr)
age = int(ageStr)

if month == 11 or month == 12 or month == 1:
    print("旺季")
    if 18 < age <= 60:
        print("票价为:", TICK_PRICE)
    elif age > 60:
        print("票价为:", TICK_PRICE/3)
    elif age < 18:
        print("票价为:", TICK_PRICE/2)
    else:
        print("请输入正确的年龄")
else:
    print("淡季")
    if age > 18:
        print("票价为:", TICK_PRICE)
    else:
        print("票价为:", TICK_PRICE/2)
