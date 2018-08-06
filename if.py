# _*_ coding=utf-8 _*_

num0 = num1 = num2 =11 #赋值语句
num1 = num0 + 1 #加和
num2 += 1 # 自加
num3 = num0 / 3 #除法
num4 = num0 // 3 #整除
num5 = num0 % 2 #取模

print(num0,num1,num2,num3,num4) #输出

bol0 = num3 == num4 # 布尔值为0
bol1 = num3 != num4 # 布尔值为1

if num3 == num4: #if语句举例
    print("相等")
else:
    print('不相同')

if bol0 == 0: #布尔值判断（也可以一使用false或者true代替此处的0和1）
    print("不相同")
else:
    print('相同')
'''
if bol1 :
    print("相同")
else:
    print('不同')
'''
bol2 = 0
if bol2:
    print('test')
else:
    print('testtest')
'''
之后的列表也是有这种操作的
'''