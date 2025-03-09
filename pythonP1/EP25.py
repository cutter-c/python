# โครงสร้างข้อมูลแบบทำซ้ำ
"""
ทำจนกว่าจะเป็นเท็จ
while expession(ค่าความจริง):
    statement
"""


i = 1 # ตัวนับจำนวนรอบ

while i <= 3:
    print("Hello World"+" รอบที่ ",i)
    i += 1

o = 1
summation = 0
# 1+2+3+4+5
while o <= 10:
    summation += o
    #print(summation)
    o += 1
print("ผลรวมการบวกเลข = ",summation)
print("ค่าเฉลี่ย = ",summation/o)

"""
for in range(start,stop,step): # range()กำหนดรอบ

"""

summation = 0
for i in range(1,11):
    summation += i
    print("รอบที่ = ",i,"Hello World")
print(summation)