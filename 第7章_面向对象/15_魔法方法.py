# 类中以双下划线开头和结尾的方法，叫魔法方法（魔术方法）。
# 魔法方法不需要手动调用，Python会在特定场景自动调用。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # __str__ 方法，执行时机：当调用 print(对象)或str(对象) 时
    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}'

    # __str__ 方法，执行时机：当调用 len(对象) 时
    def __len__(self):
        return len(p1.__dict__)

    # __lt__ 方法，执行时机：当执行 对象1 < 对象2 时
    # 如果执行 > 操作，Python会先查找有没有定义 __gt__ 方法，如果有就执行，如果没有，就执行 __lt__ 方法
    def __lt__(self, other):
        print('执行了__lt__方法')
        return self.age < other.age

    # __gt__ 方法，执行时机：当执行 对象1 > 对象2 时
    # 如果执行 < 操作，Python会先查找有没有定义 __lt__ 方法，如果有就执行，如果没有，就执行 __gt__ 方法
    def __gt__(self, other):
        print('执行了__gt__方法')
        return self.age > other.age

    # __eq__方法，执行时机：当执行 对象1 == 对象2 时
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # __getattr__方法，执行时机：当访问了对象不存在的属性时
    def __getattr__(self, item):
        return f'您访问的{item}属性不存在'

p1 = Person('张三', 18, '男')
p2 = Person('李华', 17, '女')
p3 = Person('张三', 18, '男')

print(p1)
print(p2)
print(len(p1))
print(p1 < p2)
print(p1 > p2)
print(p1 == p3)
print(p1.address)