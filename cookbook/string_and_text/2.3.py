#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""利用shell通配符做字符匹配
    *代表多位
    ?代表一位
"""

from fnmatch import fnmatch, fnmatchcase

a = "aaabbbccc"

print(fnmatch(a, "*cc"))
print(fnmatch(a, "aa*"))
print(fnmatch(a, "?cc"))

names = ["gaojiuli", "hewen", "wuqiang", "xusanduo"]

# 把名字中最后一位含i的找出来
new_names = [name for name in names if fnmatch(name, "*i")]
print(new_names)

# 把名字中中间含i的找出来
new_names2 = [name for name in names if fnmatch(name, "*i*")]
print(new_names2)

# windows不识别大小写, mac识别大小写
# 需要识别的话使用fnmatchcase

nick_names = ["PIG", "egg", "KG", "UG"]

new_lst1 = [n for n in nick_names if fnmatch(n, "*g")]
print(new_lst1)

new_lst2 = [n for n in nick_names if fnmatchcase(n, "*g")]
print(new_lst2)
