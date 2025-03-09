# การส่งค่าเข้ามาที่ function

def myData(name,lastname,c) :
    print("ชื่อ =",name,"นาสกุล =",lastname,"อายุ = ",c)
'''
myData("Jojo","Jaja")
myData("Nut","O")
myData(5,6)
'''
fname = "Piyapon"
lname = "Thabua"
age = 20
myData(fname,lname,age) 

# Arguments => ค่าที่ส่งเข้าไปใน function => fname , lame , age (ตอนที่เรียกใช้ฟังก์ชั่น)
# Parameter => ค่าตัวแปรที่รับข้อมุที่ส่งมาทำงาน (Arguments) => name , lame , c

# อาส่ง(Arguments) - พารับ(Parameter)
def addition(a,b):
    print("ผลรวม = ",a+b)

addition(5,9)