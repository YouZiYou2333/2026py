# 作者：叶子多
# 2026年04月30日13时25分32秒
# yexixi2333@gmail.com

def read_config():
    text=open('file5','r+',encoding='utf-8')
    text_info=text.read()
    print(text_info)
    print(eval(text_info))
    print(type(eval(text_info)))
    text.close()

if __name__ == '__main__':
    read_config()