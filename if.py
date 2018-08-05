# _*_ coding=utf-8 _*_

num0 = num1 = num2 =11
num1 = num0+1
num2 += 1
num3 = num0 / 3
num4 = num0 // 3
num5 = num0 % 2

print(num0,num1,num2,num3,num4)

bol0 = num3 == num4
bol1 = num3 != num4
bol2 = 0

if num3 == num4:
    print("相等")
else:
    print('不相同')

if bol0 == 1:
    print("不相同")
else:
    print('相同')

if bol1 :
    print("相同")
else:
    print('不同')

if bol2:
    print('test')
else:
    print('testtest')