# การนิยาม , constructor

tup = tuple((1,2,3,4,"cutter","มะม่วง",True,3.99)) # tuple = ()
#lis = list([1,2,3,4,"cutter","มะม่วง",True,3.99]) # list  = []
# ใช้แปลงชนิดข้อมูลได้ => tuple((" "," "))  
# เปลี่ยนเแปลงข้อมูลได้ list
# ไม่สามารถเปลี่ยนแปลงข้อมูลได้ tuple
'''
lis[0] = "กรุงเทพ"
# tup[0] = "bankok" ไม่สามารถเปลี่ยนได้
print(tup)
print(lis)
'''

'''
#การเช้าถึงข้อมูลได้ tup[]
print(tup[-1])
print(tup[-3:-1]) # ถ้าจะเอาตัวสุดท้ายด้วยใช้ [-2:เว้นว่าง]
'''
'''
# วิธีการเปลี่ยนแปลงข้อมูล tuple
lis =list(tup)
lis[0] = "กรุงเทพ"
print("ก่อนแก้ไข =",tup)
tup = tuple(lis)
print("หลังแก้ไข =",tup)
'''

for item in tup:
    print("สมาชิก = ",item)
# เช็คสมาชิก
if "มะม่วง" in tup:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")
# การนับสมาชิก
print(len(tup))
# ใช้ idex มาอ้างอิง
for item in range(len(tup)): 
    print(tup[item]) # tup[0],tup[1],tup[2],tup[3],....

# tuple ไม่มีสมาชิก
x = ()
print(x)
y = tuple()
print(type(y))
# การจะเป็น tuple ต้องมีสมาชิกเป็น 0 และ มากกว่า 1 อย่างเช่น
# y = ("abc",) y = () y = tuple((2))

name = ("cutter","jojo")
new = ("nut","nack")
# tuple + tuple ต้องบวกกับ tuple 
allGroup = name + new # name=name+(new,) and name=name+tuple(new)
print(allGroup)

# รวม list กับ tuple
city = ["กรุงเทพ","ชลบุรี","อุุบล"]

tup += tuple(city)
print(tup)
# del tup ลบตัวแปรทิ้ง
lis = list(tup)
print("ก่อน = ",tup)
lis.pop() # นำข้อมูลต้วสุดท้ายออก
lis.remove("มะม่วง") # เลือกข้อมูลที่จะนำออก
tup = tuple(lis)
print("หลัง =",tup)

# การค้นหาและนับจำนวนสมาชิก ???.count
x = tup.count(4)
print(x)
# ค้นหาด้วย ???.index บอกเป็นลำดับ 0,1,2,3
x = tup.index(4)
print(x)
'''
# tuple ไม่มี funsion sort and revarse
print("ก่อน = ",tup)
lis = list(tup)
lis.sort()
tup = tuple(lis)
print("หลัง = ",tup)
'''

# นำค่าใน tuple => ตัวแปร
tup = (10,20,30)
a,b,c = tup
print(a,b,c)
d = a + c
print(d)
# สลับ tuple
x = (50,60)
y = (88,99)
print("Before =","x",x,"y",y)
x,y = y,x
print("After","x",x,"y",y)
# tuple => string
character = ('k','o','n','g')
name = "".join(character) #เชื่อม string เช้าด้วยกัน
print(name)
# reversed tuple
x = (100,20,30,15,10,5,500)
y = tuple(reversed(x)) #ต้องเปลี่ยนเป็น list or tuple
print(tuple(y))
i = "cutter"
print(tuple(i))
j = tuple(reversed(i))
print(tuple(j))