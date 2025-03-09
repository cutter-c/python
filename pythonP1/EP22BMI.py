# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = WEIGHT(kg) / high * high (m)
# input / cunvert to integer
weight = int(input("ป้อนน้ำหนักของคุณ (kg): "))
high = int(input("ป้อนส่วนสูงของคุณ (cm): "))/100
bmi = weight/(high**2)
#print("BMI = ",bmi)
#print("BMI = ",weight/(high**2))

'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1 
>30 = โรคอ้วยระดับอันตราย
'''

if bmi < 18.0 and bmi >= 0:
    result="ผอม"
elif bmi >= 18.5 and bmi <= 22.9:
    result="สมส่วน"
elif bmi >= 23.0 and bmi <= 24.9:
    result="น้ำหนักเกิน"
elif bmi >= 25.0 and bmi <= 29.9:
    result="โรคอ้วน ระดับที่ 1 "
elif bmi >= 30:
    result="โรคอ้วนระดับอันตราย"
else:
    result="ไม่ทราบค่าที่ชัดเจน"

print("ค่า BMI =",bmi,"ทำนายว่า = ",result)

