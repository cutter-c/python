# เขียนแบบ primitive

a  = 1
a1 = 2
a2 = 3 
a3 = 4
a4 = 5
a5 = 6
a6 = 7

# non primitive : list
number = [] # list ว่าง
number = [1,2,3,4,5,6] # list มีสมาชิก 1,2
name = ["นาย A","นาย B","นาย C"] # list name มีสมาชิก
all = [10,"นายไข่",True,3.14,-10]
#name =list(["นาย A","นาย B","นาย C"])
'''
print(all[1:4]) # 0,1,2
print(all[-3:-1]) #กำหนดค่าลบตัวแรกไว้ด้านขวา True,3.14
print(name[1])
'''
# การแก้ไขข้อมูล
# ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"

#print("ก่อนแก้ไข =>",number)
'''
number[2] = 9
number[-1] = "นายไข่" #ใช้ 5 or -1 ก็ได้ 
print("หลังแก้ไข =>",number)
'''
'''
sum = 0
for x in number:
    print("สมาชิก = ",x)
    sum += x
print(sum)
'''

fruit = ["มะม่วง","มะนาว","มะยม","มะละกอ"]
number = [1,2,3,4,5,6,7,8,9,10]
name = ["ก","ข"]

"""
if "มะยม" in fruit:
    print("เป็น")
else:
    print("ไม่เป็น")
"""
'''
for i in range(len(fruit)):
    print(fruit[i])

for item in fruit:
    print(item)
    '''

'''
print("ก่อนเพิ่ม =",fruit)
# append() นำสมาชิกใหม่ มาต่อท้ายเพื่อน
fruit.append("มะปราง")
fruit.append("แตงโม")
# insert(index,สมาชิกใหม่) นำมาแทรกแทนตัวเดิม index
print("หลังเพิ่ม =",fruit)
fruit.insert(1,"ทุเรียน")
print("หลังแทรก =",fruit)
'''
'''
# นำออก
fruit.remove("มะยม") # ระบุข้อมูลเพื่อลบออก
print("Remove =>",fruit)
fruit.pop() # นำตัวสุดท้ายออก
fruit.pop()
print("Pop =>",fruit)


del fruit[1] # ระบุ index เพื่อลบออก
del fruit # เคลียร์หน่วยความจำ(ลบออกทั้งหมด(ตัวแปรด้วย))
fruit.clear() #ลบสมาชิกออก(ตัวแปรยังใช้ได้เหลือแค่ list เปล่าๆ)
print(fruit)
'''
number = [1,2,3,4,5,6,7,8,9,10,5,6,5,3]
# copy list
x = []
print(x)
x = fruit.copy()
print(x)

# รวมสมาชิกของ list
allGroup = number + fruit
print(allGroup)

# แสดงจำนวนสมาชิก ???.count()
x = number.count(5)
print(x) # มีซ้ำกันทั้งหมด 3 ตำแหน่ง

number = [1,2,3,4,5,6,7,8,9,10]
# รวม list
number.extend(fruit)
print(number)