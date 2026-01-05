score_list = [62, 50, 84, 99, 60, 70, 90, 80]
index = 0
# while遍历
while index < len(score_list):
    print(score_list[index])
    index += 1

# for遍历
# 写法1
for item in score_list:
    print(item)

# 写法2
for index in range(len(score_list)):
    print(score_list[index])

# 写法3
# enumerate 的 start 参数，可以让计数从指定值开始（改变的是循环时的“编号”，不是真正的索引值）
for item, index in enumerate(score_list, start=5):
    print(index, item, score_list[0])