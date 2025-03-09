name = " piyapon piyapon cutter " # index(start) => 0

print(name[0:4]) # ก่อนถึงจุดสุดท้าย (ใช้ตัวเท่านั้น[0:0])
# index นับจากด้านหลัง ใช้ -1,...

# len function หาความยาวของ string
print(len(name))

# strip()ลบช่องว่างซ้ายขวา
print(name.strip())

# เปลี่ยนเป็นพิมพ์เล็กพิมพ์ใหญ่
print(name.lower())
print(name.upper())

# ตััวแรกสุดเป็นตัวพิมใหญ่
print(name.capitalize())

# เปลี่ยนแทนที่ตัวเดิม("1","2",1)("ตัวเดิม","ตัวใหม่",ตำแหน่ง(ตัวที่...))
print(name.replace("piyapon","shut up!!",1))

# เช็คข้อความ จะได้ค่าที่ออกเป็น => True or False
x = "on" in name
print(x)
if x:
    name = name.replace("on","in")
print(name)

# การต่อ string (Concatinate)
fname = "cutter"
lname = "piyapon"
age = "20"
salary = 500.98765
fullname = fname + lname
#print("ชื่อต้น :"+fname+"\tนามสกุล :"+lname+"\tอายุ :"+age)
# :.2f แสดงทศนิยม สองตำแหน่ง
text = "ชื่อต้น :{0}\tนามสกุล :{1} อายุ :{2} อาชีพ :{3} เงินเดือน :{4:.2f}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary))

# การนับจำนวนคำในประโยค
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
# fruit.count() <= นับจำนวนคำที่ใส่ลงไปว่่ามีกี่ตัว
print(fruit.count("ทุเรียน"))

# เช็คคำขึ้นต้น
nname = "นายกอไก่ ใจดี"
if nname.startswith("นาย"):
# if nname.endswith("ดี") : (คำสั่งเช็คคำลงท้าย)
    print("เป็นเพศชาย")
else :
    print("เป็นบุคคลอื่น")
