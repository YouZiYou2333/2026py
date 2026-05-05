# 作者：叶子多
# 2026年05月05日13时31分45秒
# yexixi2333@gmail.com

import re

result=re.match('he.lo','hello world')
if result:
    print(result.group())
else:
    print("No match found")