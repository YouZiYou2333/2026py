# 作者：叶子多
# 2026年04月28日11时29分28秒
# yexixi2333@gmail.com

import os


def use_rename():
    # os.rename("dir1\\file1","dir1\\file2")
    os.remove("dir1\\file2")


def use_dir_func():
    mylist = os.listdir('.')
    print(mylist)


def use_change_dir():
    print(os.getcwd())
    os.chdir("dir1")
    print(os.getcwd())

def scan_dir(current_path):
    file_list=os.listdir(current_path)
    for file in file_list:
        print(file)
        if os.path.isdir(file):
            scan_dir(file)



if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # use_change_dir()
    scan_dir(os.curdir)