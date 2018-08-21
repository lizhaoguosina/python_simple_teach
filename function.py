# _*_ coding=utf-8 _*_

'''
以下为函数构造演示
'''

#无参函数
def pr_a():
    print('a')

#单参函数
def pr_in(a):
    print(a)

#多参函数
def pr_douin(a,b):
    c = a + b
    print(c)

#两个输入值
firin = input('第一个值')
secin = input('第二个值')

pr_a()
pr_in(firin)
pr_in(secin)
pr_douin(firin,secin)

'''
以下为列表及字典演示
'''

a = [1,2,3,4,'85',3.33333]

print(a)

for a0 in a:
    print(a0)

print(a[0])

b = {'10':'q','20':'w','30':'e','40':'r'}

for b0 in b:
    print(b0)
    print(b[b0])

thr = [] #构造空列表
thr.append('test') #在列表最后增加一个元素
thr.append(1)
thr.append(3.3333)
print(thr) #打印整个列表

lenthr = len(thr) #求列表thr的长度
lenthr -= 1
print(thr[lenthr]) #最后一个元素

print(thr[-1]) #最后一个元素