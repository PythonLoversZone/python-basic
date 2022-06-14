list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
#        0  1  2  3  4  5  6

print(list1[0])
print(list1[1:3])
print(list1[-1])


# add
list2.append(8)
print(list2)

# delete
del(list2[3])
print(list2)


# 运算


print(list1 + list2)
print(list2 * 2)

print(3 in list2)

# 循环
for i in list2:
    print(i, end="\n")
print("\n")

# 常用函数
print(len(list2))
print(max(list2))
print(min(list2))

print(list2.index(3))

list2.insert(3, 4)
print(list2)


result = list2.pop(3)
print(result)
print(list2)


list2.reverse()
print(list2)


list2.sort()
print(list2)


print()
print()
print()
print()


# 元组
tup1 = ('physics', 'chemistry', 1997, 2000)

tup2 = (1, 2, 3, 4, 5)

tup3 = "a", "b", "c", "d"


tup4 = (4,)


print(tup1)
print(tup2)
print(tup3)
print(tup4)

print(type(list1))
print(type(tup1))


print(list(tup1))
print(tuple(list1))

print(type(list(tup1)))
print(type(tuple(list1)))


print()
print()
print()
print()
# set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

basket2 = set("なす野菜")
basket3 = set()

print(basket2)

set1 = set("abcdefg")
print(set1)


basket.add("plum")
print(basket)

basket.update(["plum", "watermelon"])
print(basket)


# basket.remove("orange")
# basket.remove("orange")


basket.discard("orange")
basket.discard("orange")
print(basket)
