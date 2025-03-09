'''
จัดกลุ่มข้อมูลพื้นฐาน
List = [] , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Tuple = () , ข้อมูลต่างชนิดกัน , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Set = {} , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่แน่นอน
'''

# แบบปกติ
fruit = {"มะม่วง","มะขาม","มะยม",50,True}
print(type(fruit))
#print(fruit)
# constructor
fish = set({"ปลาดุก","ปลาหมอ"})
print(fish)
#เพิ่มข้อมูลสมาชิก
fruit.add("ทุเรียน")
fruit.add("สับปะรด")
fruit.add(999)
#เพิ่มสมาชิกหลายตัว
lis = ["ตะไคร","โหระพา","ชะอม"]
fruit.update(lis)
#fruit.update(["ตะไคร","โหระพา","ชะอม"])
print(fruit)

#Loop
for item in fruit:
    print("ข้อมูล =>",item)
#แสดงจำนวนสมาชิกใจ set
print(len(fruit))
'''
if "มะเฟือง" in fruit:
    print("มี")
else:
    print("ไม่มี")
    '''

fruit.remove("ทุเรียน")
# ???.discard ลบตัวที่ไม่มีในสมาชิกแล้วไม่มี error เหมือน ???.remove
fruit.discard("มะนาว")
fruit.add("ทุเรียนทอด")
# ???.clear ลบสมาชิกภายใน set
fruit.clear()
# del ??? ลบตัวแปรทิ้ง
#del fruit 
print(fruit)
