class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}，年龄是{self.age}，性别是{self.gender}，我想说{msg}')


# 定义Student类（子类、派生类），继承自Person类（父类、超类、基类）
class Student(Person):
    def __init__(self, name, age, gender, sid, grade):
        # 在子类中，有两种方式去调用父类的初始化方法，来实现对继承属性：name, age, gender 初始化操作
        # 方式1（更推荐）
        super().__init__(name, age, gender)

        # 方式2
        # Person.__init__(self, name, age, gender)

        # 子类独有的属性，需要自己手动完成初始化
        self.sid = sid
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，我在努力的学习，争取做到{self.grade}年级的第一名')

# 创建Student类的实例对象
s1 = Student('李华', 16, '男', '2010001', '初三')
# print(s1.__dict__)
# print(type(s1))

# s1.speak('桀桀桀')
s1.study()