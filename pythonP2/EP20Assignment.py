# Keyword Arguments

def displayData(fname,lname,city="Bangkok"):#ระบุข้อมูลจังหวัดไว้
    print("ชื่อ =",fname)
    print("นามสกุล =",lname)
    print("จังหวัด =",city)
    print(" ")

displayData("Piyapon","Thabua","Bangkok")
displayData("Thailand","Thabua","Piyapon")
# สลับตำแหน่งได้แต่ต้องระบุ Parameter
displayData(city="Sukhothai",lname="Thabua",fname="Piyapon")

displayData(fname="Bob",lname="JaiD")