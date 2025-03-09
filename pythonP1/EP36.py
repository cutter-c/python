# เกมทายเลขลูกเต๋า

import random
#สุ่มตัวเลขลูกเต๋า
myrandom = random.randrange(1,6+1)
k = 0

#print(myrandom)
#correct = False
while True:
    if k == 3:
        break
    number = int(input("ป้อนคำตอบของคุณ = "))
    #correct = (number == myrandom)
    if number < 0:
        break
    
    correct = (number == myrandom)
    
    if not correct :
        if(number > myrandom):
            print("น้อยกว่า")
        if(number < myrandom):
            print("มากกว่า")
    
    if correct :
        print("ดีใจด้วยคุณตอบถูกต้อง")
        break
    else :
        print("เสียใจด้วยคุณตอบผิด")
    k += 1

if not correct :
    print("เสียใจด้วย")
    print("เฉลย = ",myrandom)