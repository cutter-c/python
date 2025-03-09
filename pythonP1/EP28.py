# break / continue

"""
i = 1
while i <= 10:
    print("รอบที่ = ",i) 
    if(i == 5):
        break
    i += 2
else:
    print("จบโปรแกรม")
"""
print(3%2)

i = 0
while i <= 10:
    i+=1
    if(i%2 == 1):
        print("T : ",i)
        continue
    print("รอบที่ = ",i)

print("จบโปรแกรม")