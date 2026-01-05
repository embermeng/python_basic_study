age = int(input('请输入你的年龄：'))
report = input('是否提交体检报告（是/否）：')
level = input('请输入你的会员等级（1/2/3）：')
print('******⬇️程序的识别结果如下⬇️：******')
if 18 <= age <= 45:
    print('✅️你的年龄符合参赛要求！')
    if report == '是':
        print('✅️你已提交体检报告！')
        print('✅️恭喜，你可以参赛了！')
        if level == '1':
            print(f'😊尊敬的{level}级会员，比赛结束后，你可以领取一件纪念T恤！')
        elif level == '2':
            print(f'😊尊敬的{level}级会员，比赛结束后，你可以领取一双专业跑鞋！')
        elif level == '3':
            print(f'😊尊敬的{level}级会员，比赛结束后，你可以领取一个运动耳机！')
        else:
            print('❌比赛结束后，你啥都领不到，快去办会员！')
    elif report == '否':
        print('❌你还没提交体检报告，提交了才能参赛，快去提交！')
    else:
        print('❌你提交的体检报告有误！')
else:
    print('❌你的年龄不在18到45岁间，不符合参赛要求！')