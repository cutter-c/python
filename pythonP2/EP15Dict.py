# list , tuple
lis = ["สีแดง","สีเหลือง","สีเขียว"]
tup = ("สีแดง","สีเหลือง","สีเขียว")

# dictionary => key(การเข้าถึงข้อมูล) , value(ค่าของข้อมูล)
# list , tuple => index , value
# การสร้าง dict
# ชื่อตัวแปร = {key:value,key:value,key:value}
colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า"}
city = {"bangkok":"กรุงเทพ"}
animal = {"ไก่":"chicken","แมว":"cat","หมา":"dog"}
# ระบุ dict
animals = dict(cat="น้องแมว",dog="น้องหมา",duck="น้องเป็ด")
student = {"ก้อง":40,"โจ้":50,"โค้ช":100}
room = {300:"นาย A",301:"นาย B",302:"นาย C"}
#print(lis[0])
#print(tup[0])
print(colors[98])
print(city["bangkok"])
print(animal["หมา"])
print(student["โจ้"])
print(room[301])
print(animals["duck"])
# ระบุอีกแบบได้ ???.get(...)
print(animals.get("dog"))
# เปลี่ยนข้อมูล
colors[100] = "บ้านสวน"
print(colors[100])
# เพิ่มข้อมูล
# ถ้า เป็น key ซ้ำให้แก้ไขข้อมูลอันเก่า
colors.update({"blue":"สีน้ำเงิน","orange":"สีส้ม"})
print(colors)

# อยากได้เฉพาะส่วนของ key/values = ???.keys() &???.valued()
# เอาทั้งสอง ???.items()
for k,v in colors.items():
    print("key = ",k,"value = ",v)

# การลบข้อมูล(ระบุ)
colors.pop("red")
# ลบข้อมูลล่าสุด(ตัวสุดท้าย)
colors.popitem()
# เคลียร์ข้อมูล
'''colors.clear()'''
# ลบตัวแปร
'''del colors'''
print(colors)
# copy ข้อมูล
x = colors.copy()
print(x)

#dict ซ้อน dict
market = {
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กระเพราไก่","ก๋วยเตี้ยว"],
        "zone":"ตะวันออก"
    },
    "ร้านลุงป้อม":{
        "name":"น้าจ๊อบ",
        "menu":["มะม่วง","ทุเรียน"],
        "zone":'ทางเข้าตลาด'
    },
    "ร้านน้าใจ":{
        "name":"น้าใจ",
        "menu":["นมปั่น","นมเย็น"],
        "zone":'ข้าง 7-11'
    }
}

print(market["ร้านป้าพร"]["menu"])
# check ว่ามีหรือไม่
print("ก๋วยเตี้ยว" in market ["ร้านป้าพร"]["menu"])

if "ก๋วยเตี้ยว" in market["ร้านป้าพร"]["menu"]:
    print("เป็น")
else:
    print("ไม่เป็น")