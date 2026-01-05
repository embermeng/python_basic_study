from datetime import datetime

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 0
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.sid = f'{datetime.now().year}{Student.count:03d}'
        self.scores = {}

    # 给当前学生添加成绩
    def add_score(self, sub, score):
        self.scores[sub] = score

    def cal_avg(self):
        if len(self.scores):
            return sum(self.scores.values()) / len(self.scores)
        else:
            return f'{self.name}还没考过试！'

    def __str__(self):
        return f'{self.name}({self.age}-{self.gender}), 成绩：{self.scores}, 平均分：{self.cal_avg():.1f}'



class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_stu(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')
        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f'添加成功！学号是：{stu.sid}')

    # 删除学生
    def del_stu(self):
        sid = input('请输入学号：')
        target = None
        for stu in self.stu_list:
            if stu.sid == sid:
                target = stu
        if target:
            self.stu_list.remove(target)
            print('删除成功！')
        else:
            print('学号错误，删除失败！')

    # 展示所有学生
    def show_all_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('暂无学生！')

    # 给指定学生设置成绩
    def set_score(self):
        sid = input('请输入学号：')
        for stu in self.stu_list:
            if stu.sid == sid:
                score_str = input('请输入成绩（学科-分数，学科-分数）：')
                score_list = score_str.replace('，', ',').split(',')
                for item in score_list:
                    sub, score = item.split('-')
                    sub = sub.strip()
                    score = float(score.strip())
                    stu.add_score(sub, score)
                print('添加成功！')
                return
        print('学号错误！')

    # 提供主菜单
    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            choose = input('请输入操作编号：')
            if choose == '1':
                self.add_stu()
            elif choose == '2':
                self.del_stu()
            elif choose == '3':
                self.show_all_stu()
            elif choose == '4':
                self.set_score()
            elif choose == '5':
                print('拜拜！')
                break
            else:
                print('输入错误！')


m1 = Manager()
m1.run()