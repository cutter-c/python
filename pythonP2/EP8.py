# Assingnment จับคู่ทักทาย / บุคคล

"""
Hi , Hello
ก้อง , แก้ม

Hi ก้อง , Hi แก้ม , Hello ก้อง , Hello แก้ม

"""

greeting = ["สวัสดี","Hi","Hello","Good Bye"]
people = ["ก้อง","แก้ม","โจ้"]
result=[]
# nomal
for x in greeting:
    for y in people:
        result.append(x+y)
print(result)

#ลดรูป
result = [x+y for x in greeting for y in people] # ผลลัพธ์ for and for
print(result)
