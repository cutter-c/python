# แปลงอุณหภูมิ
# C = (F - 32) * (5 / 9)
# F = C * (9 / 5) + 32
print("กรุณาเติมองศาต่อท้าย(C or F)")
temp = (input("ป้อนอุณหภูมิ(องศา) :"))

# a = "19C"
# print(a[:-2]) # [:-2] ตัดตัวหลัง 2 ตัว

degree = int(temp[:-1])
unit = temp[-1].upper() # ตัวหลังสุด พิมพ์ใหญ่

if unit == "C":
    F = str((degree * 9 / 5) + 32) + "F"
    #F = str(F)+"F"
    print("อุณหภูมิ ",temp.upper()," = ",F)
if unit == "F":
    C = str((degree - 32) * (5 / 9)) + "C"
    #C = str(C)+"C"
    print("อุณหภูมิ ",temp.upper()," = ",C)

'''
if unit == 'C':
    result = (degree * 9 / 5) + 32
    unit_result = "ฟาเรนไฮน์"
if unit == 'F':
    result = (degree - 32) * (5 / 9)
    unit_result = "เชลเชียส"

print("แปลงตัวเลข = ",temp,"เป็น",unit_result," = ",result)
'''