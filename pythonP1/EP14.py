'''
โครงสร้างควบคุม (Control Structure)
1. แบบลำดับ
2. แบบเลือก
3. แบบทำซ้ำ
'''

'''
if boolean expression:
    statement
'''

age = int(input("ป้อนอายุของคุณ :"))

'''
if age >= 15: #เมื่อเงื่อนไขเป็นจริง
    print("คำนำหน้าเป็น นาย,นางสาว")
else : #เมื่อนอกเหนือจากเงื่อนไขข้างต้น
    print("คำนำหน้าเป็น เด็กหญิง,เด็กชาย") 
    
print("\tจบโปรแกรม") 
'''


'''
 if จริง :
     ทำอะไร
else :
    ทำอะไร
'''
# if elif (เมื่อเจอค่าที่เป็นจริงแล้วจะเอาค่านั้นเลย(ค่าอื่นไม่เอา))
# เช็คทุกค่าจากบนลงล่างถ้าจริงเอาตัวนั้นตัวเดียวเลย
# ตัวอย่าง
# เช็ควัยตามอายุ

'''
if age >= 15:
    print("วัยรู่น")
elif age >= 20:
    print("วัยผู้ไหญ่")
elif age >= 30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")

print("\tจบโปรแกรม") 
'''

# and or not
# การกำหนดข้อมูลที่ป้อน
'''
if age >= 15 and age < 20:
    print("วัยรู่น")
elif age >= 20 and age < 30:
    print("วัยหนุ่มสาว")
elif age >= 30 and  age < 60:
    print("วัยทำงาน")
elif age >= 60 and age < 80:
    print("วัยเกษียตรญ์")   
elif age >= 80:
    print("วัยชรา")
elif age <= 0:
    print("ไม่สามารถบอกวัยได้")
else :
    print("วัยเด็ก")

print("จบโปรแกรม") 
'''

# Ternary Operator
'''
print("วัยรู่น") if age >= 15 else print("วัยเด็ก")
print("จบโปรแกรม")
'''   
