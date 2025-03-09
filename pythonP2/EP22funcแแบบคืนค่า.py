# function return ค่า

'''
1. ไม่มีการรับค่าและส่งค่า
def name():

2. มีการรับค่าเข้าไมปทำงาน
def name(a,b):

3. รับค่าเข้าไปทำงาน และส่งออกมา
def name(a,b):
    return a+b

4. ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป
def name():
    return 1
'''

def add(a,b):
    return a+b

def showNumber():
    return 500

print(add(10,20))
add(20,10)

x = showNumber()
print("ตัวเลข =",x)

def randomNumber(x):
    if x == '100':
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0

money = randomNumber('100')#ทำงาน
print(money)
i = 300
result = money - i
print("เงินรางวัล =",money)
print("เงินคงเหลือ =",result)