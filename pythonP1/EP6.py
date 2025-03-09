# Type Coversion
x = 10
y = 3.14
z = "20"

# บวกเลข
#result = x + z  # 10 + 3.14 = 13.14

# string => int
# "20" => 20
int(z)

# int => string
# 10 => "10"
str(x)
result = str(x) + z
print(result)

# float <= string
# "20" => 20.00
float(z) 

# int => float
# 10 => 10.00
float(x)

# float => int
# 3.14 => 3
int(y)

# ต้องใส่ค่าที่จะเปลี่ยนภายในบรรทัดที่จะเปลี่ยน
# print(int(y))
# การบวก str คือจะนำ str มาต่อกัน เช่น "23" + "10" จะได้ 2310

print(result)