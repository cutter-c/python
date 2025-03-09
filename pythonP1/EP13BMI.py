# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

weight = int(input("ป้อนน้ำหนักของคุณ (kg): "))
hight = int(input("ป้อนส่วนสูงของคุณ (cm): "))

#process
#cm => m
hight /= 100 
#calculate bmi
bmi = weight / (hight * hight)#hight**2

#output
#print("BMI = ",bmi)
print("BMI = ",bmi)


#แบบที่ 2
weight = int(input("ป้อนน้ำหนักของคุณ (kg): "))
hight = int(input("ป้อนส่วนสูงของคุณ (cm): "))/100
print("BMI = ",weight / (hight * hight))