# ตัวดำเนินการทางตรรกศาสตร์

# AND = และ
# OR = หรือ
# NOT = ไม่

# คำตอบที่ได้ => จริง / เท็จ

x = (10>5) # ค่า x = bool
y = (10==5) # ค่า y = bool

# z = (10>5) and (10==5)
# i = (10>5) or (10==5)
z = x and y
i = x or y 

print(x)
print(y)
print(z)
print(not i)