# _*_ coding=utf-8 _*_

'''
以下是for循环部分
'''

a = [1,2,3,4,'85',3.33333]
for a0 in a:
    a0 += a0
    print(a0)
#列表输出演示

b = {'10':'q','20':'w','30':'e','40':'r'}
for b0 in b:
    print(str(b0)+' '+str(b[b0]))
#字典输出演示

c = (5,6,7,8)
for c0 in c:
    print(c0)
#元组输出演示

d = 1
for i in range(1,2019):
    d *= i
print(d)
#大数运算演示，从1乘到2018。C语言很难直接输出

'''
以下为while循环部分
'''