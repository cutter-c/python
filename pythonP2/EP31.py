# หาจำนวนตัวอักษรพิมพ์เล็ก/พิมพ์ใหญ่

def checkstring(message):
    result ={"UPPER":0,"LOWWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWWER"]+=1
        else:
            pass
    return result

message = input("input your message :")
x = checkstring("ABcDef")
print(x)