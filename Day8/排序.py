# 作者：叶子多
# 2026年05月03日01时35分43秒
# yexixi2333@gmail.com

import random
class Sort:
    def __init__(self, n):
        """
        n是排序的数的数量
        :param n:
        """
        self.len=n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i]=random.randint(0,99)

if __name__ == '__main__':
    my_sort=Sort(10)
    print(my_sort.arr)