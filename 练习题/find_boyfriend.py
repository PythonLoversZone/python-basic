# 一个女生在找对象时提出一定的条件：

# - `高`：** 180cm以上**
# - `富`：** 年收千万以上**
# - `**帅 **`：**是**

# 条件从控制台输入

# 1. 如果`三个条件同时满足`，则：“我一定要嫁给他！!！”
# 2. 如果`三个条件有为真的情况`，则：“考虑一下。”
# 3. 如果`三个条件都不满足`，则：“滚！”

height = 0
rich = 0
handsome = False

heightStr = input("请输入你的身高：")
richStr = input("请输入你的年收入：")
handsomeStr = input("你是否帅气：")

height = int(heightStr)
rich = int(richStr)
handsome = (handsomeStr == "是")


if height >= 180 and rich >= 10000000 and handsome:
    print("我一定要嫁给他！！")
elif height >= 180 or rich >= 10000000 or handsome:
    print("考虑一下。")


else:
    print("滚！")
