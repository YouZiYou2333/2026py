# 作者：叶子多
# 2026年04月30日13时15分09秒
# yexixi2333@gmail.com


import sys


# print(type(sys.argv))
# print(sys.argv)

def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write("hello")
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1])
