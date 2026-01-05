class Person:
    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类内部、子类内部、类外部，都可访问
        self._age = age         # 受保护属性：当前类内部、子类内部，可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类内部访问

    def speak(self):
        print(f'我叫{self.name}，年龄是{self._age}，身份证是{self.__idcard}')

class Student(Person):
    def hello(self):
        print(f'我是学生 ({self.name}-{self._age}-{self.__idcard})')


p1 = Person('张三', 18, '410106199908168888')
# print(p1.name)
# 如果在类的外部，强制访问【受保护的属性】，也能访问，但最好别这么做
# print(p1._age)
# 如果在类的外部，强制访问【私有属性】会报错
# print(p1.__idcard)

# Python底层是通过重命名的方式，实现私有属性的
# print(p1.__dict__)
# print(p1._Person__idcard)
