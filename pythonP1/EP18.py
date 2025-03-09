#เขียนโปรแกรมหาตัวเลข มาก / น้อย

a = int(input("ป้อนตัวเลขตัวที่ 1 : "))
b = int(input("ป้อนตัวเลขตัวที่ 2 : "))

if a > b :
    print(str(a)+" มากกว่า "+str(b))
else :
    print(str(b)+" มากกว่า "+str(a))

# , มองชนิดข้อมูลว่าเป็น string
if a > b :
    print(a," มากกว่า ",b)
else :
    print(b," มากกว่า ",a)
