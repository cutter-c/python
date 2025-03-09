# return

def randomNumber(x):
    if len(x) < 3:#เช็คจำนวนหลัก
        return
    if x == "100":
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0

i = str(input("ป้อนตัวเลขหวยของคุณ ="))
money = randomNumber(i)
print("เงินรางวัล =",money,"บาท")