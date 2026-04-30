# 作者：叶子多
# 2026年04月27日18时32分57秒
# yexixi2333@gmail.com
from 导入 import main


def open_r():
    file = open("file2.txt", "r", encoding="utf-8")
    text = file.read()
    print(text)
    file.close()


if __name__ == '__main__':
    open_r()
