# 作者：叶子多
# 2026年05月04日00时45分51秒
# yexixi2333@gmail.com

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def __str__(self):
        return 'test'


student=Student('yexixi',100,20)
print(student)