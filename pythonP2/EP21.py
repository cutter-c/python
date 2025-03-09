#

def displayFruit(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ",i+1,"คือ ",item[i])
    print("")

def displayFruitTup(item):
    for i in range(len(item)):
        print("ผักชนิดที่ ",i+1,"คือ ",item[i])
    print("")

fruit = ["มะม่วง","มะละกอ"]
vet = ("ชะอม","ผักกาด","คะน้า")
displayFruit(fruit)
displayFruitTup(vet)

