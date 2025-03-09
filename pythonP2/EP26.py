# Recursive Function

'''
หาจุดวนซ้ำ
หาจุดออกจาก function
'''
def a():
    print("A")
    a() 

# 1-5 โดยไม่ใช้ คำสั่ง loop
def num(number=0):
    if number == 5:
        return
    print(number+1)
    number += 1
    num(number)
    
def summation(number):
    if number == 1:
        return number
    else:
        return number+summation(number-1)
        
x = summation(3)
print(x)

