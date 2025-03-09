#union ทั้งหมด
fruitA = {"กล้วย","มะยม","มะนาว","แอปเปิล","ทุเรียน"}
fruitB = {"แอปเปิล","สตอว์เบอร์รี่","ทุเรียน","กีวี","มะม่วง"}
'''
# สร้าง set ใหม่
allfruit = fruitA.union(fruitB)
# ไม่ต้องสร้าง set ใหม่
fruitA.update(fruitB)
print(allfruit)
print(fruitA)
# copy set
fruitC = fruitA.copy()
print(fruitC)
'''
# difference ตัวที่ไม่อยู่ใน set เดียวกัน(แตกต่างกันจากอีก set)
fruitC = fruitA.difference(fruitB)
#แทนที่ใน set fruitA เลย
#fruitA.difference_update(fruitB)
print(fruitC)
# intersection ตัวที่เหมือนกันทั้งสอง set
fruitC = fruitA.intersection(fruitB)
#แทนที่ใน set fruitA เลย
#fruitA.intersection_update(fruitB)
print(fruitC)

#subset
fish = {"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา","ปลาฉลาม","ปลาตะเพียน"}
x = {"ปลาดุก","ปลาฉลาม"}
y = {"ปลาวาฬ","ปลาฉลาม"}

print(fish.issuperset(x))