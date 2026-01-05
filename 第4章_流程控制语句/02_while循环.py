num = int(input('你想让我打几次招呼？请输入次数：'))
n = 1
while n <= num:
    print(f'第{n}次你好啊')
    n += 1
print(f'打招呼结束，n={n}')