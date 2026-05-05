# 作者：叶子多
# 2026年05月04日18时08分43秒
# yexixi2333@gmail.com
import copy


def copy_prac1():
    a = [1, 2, 3, 4, 5]
    b = a.copy()
    b[0] = 6
    print(a)
    print(b)


# 浅拷贝 = 最外层对象新建；里面的元素引用沿用原来的
# 深拷贝 = 外层对象新建；里面嵌套的可变对象也递归新建
# copy.copy(c) / c.copy()都是浅拷贝

def copy_prac2():
    a = [1, 2, 3, 4, 5]
    b = copy.deepcopy(a)
    b[0] = 6
    print(a)
    print(b)


class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.equipments = ['鞋子','帽子']

def use_copy():
    old_h=Hero('猪猪',90)
    new_h=copy.deepcopy(old_h)
    new_h.hp=80
    new_h.equipments.append('衣服')
    print(old_h.hp)
    print(old_h.equipments)

if __name__ == '__main__':
    use_copy()