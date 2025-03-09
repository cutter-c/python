# สร้างฟังก์ชั่นหา เลขคู่ / เลขคี่

def searchNumber(number):
    if number % 2 == 0:
        print("เลขคู่")
    else :
        print("เลขคี่")

a,b,c,d = 10,23,40,50
searchNumber(a)
searchNumber(b)
searchNumber(c)
searchNumber(d)