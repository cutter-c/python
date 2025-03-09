# ฟังก์ชั่นบวกเลข

'''
def sumthree(x,y,z):
    print("มีค่าเท่ากับ =",x+y+z)

def sumfour(x,y,z,a):
    print("มีค่าเท่ากับ =",x+y+z+a)

def sumfive(x,y,z,a,b):
    print("มีค่าเท่ากับ =",x+y+z+a+b)
'''
# *(agrs)เป็นชื่ออะไรก็ได้แต่ต้องมี * ข้างหน้า  ระบุ Parameter ได้ไม่จำกัด
def add(*number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    print(sum)

add(10,20)
add(10,5,10,15)

'''
sumthree(10,20,5)
sumfour(10,20,5,10)
sumfive(10,20,5,10,20)
'''