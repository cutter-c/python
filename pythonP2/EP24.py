# **kwargs(keywordargs) ขอแค่ มี **???

# *args => ค่าใน parameter มีได้หลายค่า
def add(*number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    print(sum)

# ชื่อ parameter มีได้หลายชื่อ
def displayData(**kwargs):#เป็นข้อมูล dict
    print(kwargs)

displayData(fname ="ternaja",lname = "kubpom",age = 20,city = "bangkok")
