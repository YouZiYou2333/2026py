# 作者：叶子多
# 2026年04月28日00时23分59秒
# yexixi2333@gmail.com
from IPython.utils import encoding


def seek_start():
    """
    相对于开头偏移
    :return:
    """
    file = open("file1", 'r+', encoding='utf-8')
    file.seek(5, 0)
    text = file.read()
    print(text)
    file.close()


def seek_end():
    """
    相对于文件尾部
    :return:
    """
    file = open("file1", 'rb+')
    file.seek(5, 0)
    file.seek(-2, 1)
    text = file.read()
    print(text)
    file.close()

def copy_file():
    file1=open("psc.png","rb+")
    file2=open("psc_copy.png",'wb')
    b=file1.read()
    file2.write(b)
    file1.close()
    file2.close()

if __name__ == '__main__':
    # seek_start()
    # seek_end()
    copy_file()