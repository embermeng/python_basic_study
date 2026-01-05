class Person:
    max_age = 120
    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类内部、子类内部、类外部，都可访问
        self._age = age         # 受保护属性：当前类内部、子类内部，可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类内部访问

    # 注册 age 属性的 getter 方法：当访问 Person 实例的 age 属性时，下面的age方法会自动调用
    @property
    def age(self):
        return self._age

    # 注册 age 属性的 setter 方法：当修改 Person 实例的 age 属性时，下面的age方法会自动调用
    @age.setter
    def age(self, val):
        if val <= Person.max_age:
            self._age = val
        else:
            print('年龄非法，修改失败')

    # 注册 idcard 属性的 getter 方法：当访问 Person 实例的 idcard 属性时，下面的idcard方法会自动调用
    @property
    def idcard(self):
        return self.__idcard[:6] + '********' + self.__idcard[-4:]

    # 注册 idcard 属性的 setter 方法：当修改 Person 实例的 idcard 属性时，下面的idcard方法会自动调用
    @idcard.setter
    def idcard(self, val):
        print('抱歉，身份证号码不允许修改，如有特殊需求，请联系管理员！')

p1 = Person('张三', 18, '410106199908168888')
print(p1.name)
print(p1.age)
p1.age = 1000
print(p1.age)
print(p1.idcard)
p1.idcard = '410106199908161234'