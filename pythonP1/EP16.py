# pass (ให้คำสั่งผ่านไปก่อนรอให้คิดได้ค่อยมาเติม)

age = int(input("ป้อนอายุของคุณ : "))

if age <= 15:
    if age == 15:
        pass
    elif age == 14:
        pass
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")