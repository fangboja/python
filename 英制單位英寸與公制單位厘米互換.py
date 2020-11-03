value=float(input("請輸入長度"))
unit=input("輸入單位")

if unit=="in" or unit =="英寸":
    print("%f英寸=%f厘米"%(value,value*2.54))
elif unit == "cm" or unit=="厘米":
    print("%f厘米=%f英吋" % (value, value/2.54))
else:
    print("輸入錯誤")