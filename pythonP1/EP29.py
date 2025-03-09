start,stop = 1,5
sum,avg = 0,0

while(start <= stop):
    number = int(input("ป้อนตัวเลขของคุณ :"))
    sum += number #บวกตัวเลขที่ป้อนในแต่ละรอบ
    start += 1

avg = sum/stop
print("ผลรวม = ",sum,"ค่าเฉลี่ย = ",avg)