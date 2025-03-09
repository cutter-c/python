# lambda function

'''
lambda arguments : expression
'''
# ไม่สามารค ระบุ return ได้
x = lambda name:name
sum = lambda x,y : x + y

print(x("ternaja"))
print(sum(1,3))

def myPower(x):
    # x = ตัวเลข
    # a = เลขชี้กำลัง
    return lambda a : x**a

y = myPower(int(input("ใส่เลขที่ต้องการยกกำลัง =")))
result = y(int(input("ใส่เลขชี้กำลังที่ต้องการ = ")))

print(result)