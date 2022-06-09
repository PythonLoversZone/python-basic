# 算术运算符

a = 3
b = 2
e = 3

e += 1
print(e)
#
# a = --a
# print(a)


total = a + b  # 5

minus = a - b  # -1

var1 = a * b  # 6
var2 = a / b  # 1.5

print(total)
print(minus)
print(var1)
print(var2)
print(a + b * a - 3 / 2)  # 7.5
print((a + b) * a - 3 / 2)  # 13.5

print(3 % 2)
print(31 % 2)

print("---------------------------")

# 赋值运算符
total = a + b  # 5

total += 1  # total = total + 1  6
print(total)

total -= 1  # total = total -1 5
print(total)

total *= 3  # 15
print(total)

total /= 2  # 7.5
print(total)

total %= 2  # 1.5
print(total)

print("---------------------------")

x = 4
print(x == 5)  # false
print(x == 4)  # true
print(x != 4)  # false
print(x > 1)  # true
print(x < 1)  # false
print(x >= 4)  # true
print(x <= 4)  # true

str1 = "abc"
str2 = "e"
str3 = "abcd"

print(str1 > str2)
print(str3 > str1)

print("------------------------")

x = 1
y = 2

condition1 = x > y  # false
condition2 = x == y  # false
condition3 = x < y  # true

print(condition1, condition2, condition3)

print(condition1 and condition3)  # false
print(condition1 or condition3)  # true
print(condition3 or condition1)  # true 执行效率更高

print(not condition1)  # true
