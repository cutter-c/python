# ตารางหมากฮอต

number = int(input("ป้อนตัวเลข : "))

for row in range(number):
    for column in range(number):
        if (column+row) % 2 == 0:
            print("x",end="")
        else :
            print("o",end="")
            # print("x",end="") if (row+column) % 2 == 0: else : print("o",end="")
    print(" ")