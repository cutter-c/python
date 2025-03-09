# min , max
number = {3,4,5,100,80,900,100,500,300,-100,-8,-150}

print(min(number))
print(max(number))

#frozen set เป็นการ fix ข้อมูลเอาไว้ไม่สามารถเปลี่ยนแปลงได้เลย
#กำหนดได้แต่ข้อมูลเริ่มต้นและแสดงผล
fruit = frozenset(["มะม่วง","มะยม","มะนาว"])
#fruit.add("ทุเรียน")
#fruit.discard("มะยม")
print(fruit)
for i in fruit:
    print(i)