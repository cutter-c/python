# Assingnment รับและเรียงลำดับข้อมูลตัวเลข

number = []
while True:
    x = int(input("ป้อนตัวเลขของคุณ :"))
    if x < 0:
        break
    number.append(x)

print("ก่อนเรียง =>",number)
number.sort() # น้อยไปมาก
print("เรียงน้อยไปมาก =>",number)
number.reverse() # มากไปน้อย
print("เรียงมากไปน้อย =>",number)
print("จบโปรแกรม")