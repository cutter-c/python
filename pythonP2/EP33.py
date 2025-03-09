# Tower of Hanoi

"""
n = จำนวนจาน
เสา => A,B,C

จำนวนจาน
ืn = 1
n = 2 (n-1)
n = 3 (ใหญ่สุด)

A => 3 => C => ใหญ่ => เล็ก
B (จุดพักจาน)

A => เล็ก กลาง ใหญ่
B => เล็ก กลาง
C => เล็ก กลาง ใหญ่
"""

def hanoi(n,a,b,c):
    # a => c
    if (n==0):
        return
    hanoi(n-1,a,c,b)# ย้าย a (ล,ก) => b|c จุดพัก
    print("จานที่ =",n,"จาก =",a,"ไป =",c)
    hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")