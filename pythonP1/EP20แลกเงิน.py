# แลกเงินและหาจำนวนแบงค์

# 2000 => 1000 => 2 ใบ
# 1500 => 1000,1ใบ => 500,1 ใบ
# 1800 => 1000,1ใบ => 500,1 ใบ =>100,3 ใบ
# 100 => 50,2 ใบ

number = int(input("ป้อนจำนวนเงินของคุณ : "))

#แบบเคสปกติแบงค์ใดแบงหนึ่ง
"""
if number >= 1000:
    print("1000 บาท = ",number//1000,"ใบ")

if number >= 500:
    print(" 500 บาท = ",number//500,"ใบ")

if number >= 100:
    print(" 100 บาท = ",number//100,"ใบ")
"""

if number >= 1000:
    print("1000 บาท = ",number//1000,"ใบ")
    number = number % 1000 # 1500 % 1000 = 500
#number=500
if number >= 500:
    print(" 500 บาท = ",number//500,"ใบ")
    number = number % 500 # number %= 500 
#number=100
if number >= 100:
    print(" 100 บาท = ",number//100,"ใบ")
    number = number % 100
#number=50
if number >= 50:
    print("  50 บาท = ",number//50,"ใบ")
    number = number % 50
#number=20
if number >= 20:
    print("  20 บาท = ",number//20,"ใบ")
    number = number % 20
#number=10
if number >= 10:
    print("  10 บาท = ",number//10,"เหรียญ")
    number = number % 10
#number=5
if number >= 5:
    print("   5 บาท = ",number//5,"เหรียญ")
    number = number % 5
#number=2
if number >= 2:
    print("   2 บาท = ",number//2,"เหรียญ")
    number = number % 2
#number=1
if number >= 1:
    print("   1 บาท = ",number//1,"เหรียญ")
    number = number % 1
