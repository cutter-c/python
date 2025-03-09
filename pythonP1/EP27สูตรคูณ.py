# แม่สูตรคูณ

start = int(input("ป้อนแม่สูตรคูณเริ่มต้น = "))
stop = int(input("ป้อนแม่สูตรคูณสุดท้าย = "))+1

for i in range(start,stop):
    print("แม่สูตรคูณ = ",i)
    for j in range(1,13):
        print(i,'x',j," = ",(i*j))