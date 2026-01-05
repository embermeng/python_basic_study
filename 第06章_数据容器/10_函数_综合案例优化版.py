def calc_total(*nums):
    """
    计算总运动量（个）
    :param nums: 每一天的运动量
    :return: 总运动量（个）
    """
    # nums是元组，sum可对元组求和
    return sum(nums)


def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量
    :param days: 总天数（默认7天）
    :return: 平均值
    """
    return total / days


def check_success(total, goal=120):
    """
    判断挑战是否成功
    :param total: 总运动量
    :param goal: 目标数量（默认120）
    :return: 返回成功或失败的信息
    """
    if total >= goal:
        return '✅恭喜！挑战成功'
    else:
        return '❌抱歉！挑战失败！'


def main(title, days, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param days: 比赛持续天数
    :param goal: 目标运动量
    :return: None
    """
    print(f'【{title}】【{days}】天挑战赛✊️（请输入每天的数量）')
    num1 = int(input('第1天: '))
    num2 = int(input('第2天: '))
    num3 = int(input('第3天: '))
    num4 = int(input('第4天: '))
    num5 = int(input('第5天: '))
    num6 = int(input('第6天: '))
    num7 = int(input('第7天: '))
    # 计算总量
    total = calc_total(num1, num2, num3, num4, num5, num6, num7)
    # 计算平均值
    avg = calc_avg(total, days)
    # 判断挑战是否成功
    res = check_success(total)
    print(f'【{title}】【{days}】天健身总结')
    print(f'总数: {total}, 平均值: {avg:.1f}')
    print(res)


main('仰卧起坐', 7, 120)
