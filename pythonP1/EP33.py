# สร้างภาพวาด 4 เหลี่ยมจตุรัส

"""
xxx
xxx
xxx

xx
xx

xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
"""

number = int(input("ป้อนขนาด = "))

for row in range(number):
    for column in range(number):
        print("x",end='')
    print(" ")