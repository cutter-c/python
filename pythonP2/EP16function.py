# สาเหตุที่เราต้องเขียน function

#a,b,c,d = 10,23,40,50


#if a % 2 == 0:
#    print("เลขคู่")
#else :
#    print("เลขคี่")


# การสร้าง function / เรียก function
# def ชื่อฟังก์ชั่น () :
#       statement(กลุ่มคำสั่ง)

def sayHi():
    print("Hello Function")

def sayThailand():
    print("สวัสดี")

def sayEngland():
    print("Hello / Hi")

def add():
    x = 3+1
    print(x)

# โปรแกรมหลัก
sayHi()
sayThailand()
sayEngland()
add()

# Global Variable / Local Variable

def displayNumber():
    #statement
    x = 10
    a = 100

    print("Hello = ",x,"ใน")
    print("ใน = ",a)


# โปรแกรมหลัก
x = 20
displayNumber()
a = 100

print("Hello = ",x,"นอก")
print("นอก = ",a)

# x ดารา => x ทั่วประเทศรู้จัก (Global)
# นาย x หมู่บ้านแสนสุข => x ในหมู่บ้าน (Local)
