# Factorial 

'''
5! = 5 x 4 x 3 x 2 x 1 = 120
2! = 2 x 1 = 2
'''

def factorial(number):
    if number == 1 :
        return number
    else :
        return number * factorial(number-1)

x = factorial(8)
print(x)

# Fibonacci number
# 0, 1,(0+1)= 1,(1+1)= 2,(1+2)= 3, 5, 8 , 13, 21
# f0 = ? , f1 = ?

def fibonacci(number):
    if number <= 1:
        # สอง ลำดับแรก
        return number
    else :    
        #เลขลำดับถัดไป
        return fibonacci(number-1) + fibonacci(number-2)
                # ตำแหน่งก่อนหน้า 1     #ตำแหน่งก่อนหน้า 2
for i in range(10):
    print(fibonacci(i))

'''
i = 0
i = 1 
i = 2
i = 3

ตำแหน่งที่ 0= 0,ตำแหน่งที่ 1= 1,
fibonacci(2-1)= ตำแหน่งที่ 1 = **1 + fibonacci(2-2)= ตำแหน่งที่ 0 = **0 ตำแหน่งที่ 2 = 1
fibonacci(3-1)= ตำแหน่งที่ 2 = **1 + fibonacci(3-2)= ตำแหน่งที่ 1 = **1 ตำแหน่งที่ 3 = 2
fibonacci(4-1)= ตำแหน่งที่ 3 = **2 + fibonacci(4-2)= ตำแหน่งที่ 2 = **1 ตำแหน่งที่ 4 = 3
fibonacci(5-1)= ตำแหน่งที่ 4 = **3 + fibonacci(5-2)= ตำแหน่งที่ 3 = **2 ตำแหน่งที่ 5 = 5

'''
