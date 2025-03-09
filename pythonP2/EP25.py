# ฟังก์ชั่น เรียก ฟังก์ชั่น

def equal(x,y,z):
    #a = compare(x,y)
    #b = compare(a,z)
    #return b
    return compare(compare(x,y),z) #แบบลดรูป

def compare(x,y):
    if x > y :
        return x
    else :
        return y


max = equal(10,5,50)
print("ค่ามากที่สุด = ",max)