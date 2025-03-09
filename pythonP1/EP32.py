# ตัวเลขขั้นบันได

"""
intput = 3 
1
12
123
"""

last = int(input("ป้อนตัวเลข :"))+1

for row in range(1,last):
    for column in range(1,row+1):
        # print("row : ",row)
        print(column,end='')
    print(" ") # เพื่อขึ้นต้นบรรทัดใหม่

# end='' คือการแสดงผลในแนวนอน

# for i in range(1,11):
#    print(i)
