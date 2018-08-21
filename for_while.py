# _*_ coding=utf-8 _*_

'''
以下是for循环部分
'''

a = [1,2,3,4,'85',3.33333]
for a0 in a:
    a0 += a0
    print(a0)
#列表输出演示
#对于a列表内每个元素都自加

b = {'10':'q','20':'w','30':'e','40':'r'}
for b0 in b:
    print(str(b0)+' '+str(b[b0]))
#字典输出演示
#列表型输出，只输出索引，输出内容需要诸如b[b0]形式，即字典[索引]形式

c = (5,6,7,8)
for c0 in c:
    print(c0)
#元组输出演示

d = 1
for i in range(1,2019):
    d *= i
print(d)

e = 0
i = 0
while e == 0:
    i += 1
    e = d % (10 ** i)

i -= 1
print('一共有'+str(i)+'个0')

#一道经典的数学题，求从1乘到2018，结尾一共有多少个0
#大数运算演示，从1乘到2018。C语言很难直接输出
#python可以利用两个不同的循环来解决这个问题

'''
以下为while循环部分
'''
cot = 1
while cot <= 5:
    cot +=1
    print(cot)
