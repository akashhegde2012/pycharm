import re

pattern=re.compile('this')
string='Search inside of this text please!'
a=re.search('this',string)
b=pattern.search((string))
c=pattern.findall(string)
d=pattern.match(string)
print(d)
# print(c)
# print(a)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())