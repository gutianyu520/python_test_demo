# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 12:24
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_summary.py
# @Software: PyCharm

"""概述"""
"""
    正则表达式（正规表达式，正规表示法，规则表达式，常规表示法）
"""

import re

#使用match匹配
# regx = re.match('正则表达式','需匹配的字符串')
#使用group获取元素
# regx.group(0)

result = re.match('itcast', 'itcast.cn')
print(result.group())

"""
    表示字符
        字符	功能
        .	匹配任意1个字符（除了\n）
        [ ]	匹配[ ]中列举的字符
        \d	匹配数字，即0-9
        \D	匹配非数字，即不是数字
        \s	匹配空白，即 空格，tab键
        \S	匹配非空白
        \w	匹配单词字符，即a-z、A-Z、0-9、_
        \W	匹配非单词字符
"""
print(re.match('h','hello Python').group())
# print(re.match('H','hello Python').group())
print(re.match('[h]','hello Python').group())
print(re.match('[hH]','hello PytHon').group() if re.match('[hH]','hello PytHon') != None else None)
print(re.match('[0123456789]','7hello PytHon').group() if re.match('[0123456789]','7hello PytHon') != None else None)
print(re.match('[0-9]','hello 1PytHon').group() if re.match('[0-9]','hello 1PytHon') != None else None)

print(re.match('hh\daa','hh7aaaaa').group())

"""
    原始字符串
        正则表达式里使用"\"作为转义字符
"""
mm = 'c:\\a\\b\\c'
print(mm)

print(re.match(r'c:\\a', mm).group())

"""
    表示数量
        字符	    功能
        *	    匹配前一个字符出现0次或者无限次，即可有可无
        +	    匹配前一个字符出现1次或者无限次，即至少有1次
        ?	    匹配前一个字符出现1次或者0次，即要么有1次，要么没有
        {m}	    匹配前一个字符出现m次
        {m,}	匹配前一个字符至少出现m次
        {m,n}	匹配前一个字符出现从m到n次 
"""
print(re.match('[A-Z][a-z]*','Mn').group())
print(re.match('[A-Za-z_]+[\w_]*','_name').group())
print(re.match('[1-9]?[0-9]','09').group())
print(re.match('[\w]{8,20}','1111w1Z_11109').group())
print(re.match('[a-zA-Z0-9]{4,20}@163\.com','hel1@163.com').group())

"""
    表示边界
        字符	功能
        ^	匹配字符串开头
        $	匹配字符串结尾
        \b	匹配一个单词的边界
        \B	匹配非单词边界
"""
print(re.match('[\w]{4,20}@163\.com$','hel1@163.com').group())
print(re.match(r'.*\bver\b', '111ho ver abc').group())
print(re.match(r'.*\Bver\B', '111hovera bc').group())

"""
    匹配分组
        字符	        功能
        |	        匹配左右任意一个表达式
        (ab)	    将括号中字符作为一个分组
        \num	    引用分组num匹配到的字符串
        (?P<name>)	分组起别名
        (?P=name)	引用别名为name分组匹配到的字符串    
"""
print(re.match(r'[1-9]?\d$|100', '18').group())
print(re.match(r'\w{4,20}@(163|126|qq)\.com', '7771@126.com').group())
print(re.match(r'<([a-zA-Z]*)>\w*</\1>', '<html>11</html>').group())
re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")

"""
    re模块的高级用法
"""
"""
    search
"""
print(re.search(r'\d+', '阅读次数为 9999').group())

"""
    findall
"""
print(re.findall(r'\d+', 'python = 9999, c = 7890, c++ = 12345'))

"""
    sub 将匹配到的数据进行替换
"""
print(re.sub(r'\d+', '998', 'python = 9999'))
def add(num):
    s = num.group()
    re = int(s) +1
    return str(re)

print(re.sub(r'\d+', add, 'python = 9999'))


"""
    split 根据匹配进行切割字符串，并返回一个列表
"""
print(re.split(r':| ', 'info:xiaoZhang 33 shandong'))

"""
    python贪婪和非贪婪
    python中数量词默认是贪婪的，会尽量匹配更多的字符，非贪婪与之相反
    在 * ? + {m,n} 的后面加上?,使贪婪变非贪婪
"""
print(re.match(r"aa(\d+?)","aa2343ddd").group(1))

"""
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""

print(re.match(r'http://.+[^/](com|cn)/', 'http://www.interoem.com/messageinfo.asp?id=35').group())
print(re.match(r'http://.+[^/](com|cn)/', 'http://3995503.com/class/class09/news_show.asp?id=14').group())
print(re.match(r'http://.+[^/](com|cn)/', 'http://lib.wzmc.edu.cn/news/onews.asp?id=769').group())
print(re.match(r'http://.+[^/](com|cn)/', 'http://www.zy-ls.com/alfx.asp?newsid=377&id=6').group())
print(re.match(r'http://.+[^/](com|cn)/', 'http://www.fincm.com/newslist.asp?id=415').group())
print(re.split(r' ','hello world ha ha'))