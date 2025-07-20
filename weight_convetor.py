#weight conversion
print("weight convertor")
weight = float(input("enter a weight: "))
unit = input("enter a unit of weight(g,kg or lbs): ").lower()
targetunit= input("enter target unit(g,kg or lbs): ").lower()

#g to kg,lbs
if unit == "g":
    if targetunit == "kg":
        w = weight/1000
        print(f"result={round(w,2)} kg")
    elif targetunit == "lbs":
        w = weight/453.6
        print(f"result={round(w,2)} lbs")
    elif targetunit == "g":
        print("conversion is not needed")
    else:
        print(f"'{targetunit}' invalid target unit \navailable units are (g,kg,lbs)")

#kg to g,lbs
elif unit == "kg":
    if targetunit == "lbs":
        w = weight*2.2046
        print(f"result={round(w,2)} lbs")
    elif targetunit == "g":
        w = weight*1000
        print(f"result={round(w,2)} g")
    elif targetunit == "kg":
        print("conversion is not needed")
    else:
        print(f"'{targetunit}' invalid target unit \navailable units are (g,kg,lbs)")

#lbs to kg,g
elif unit == "lbs":
    if targetunit == "kg":
        w = weight/2.2046
        print(f"result={round(w,2)} kg")
    elif targetunit == "g":
        w = weight*453.6
        print(f"result={round(w,2)} g")
    elif targetunit == "lbs":
        print("conversion is not needed")
    else:
        print(f"'{targetunit}' invalid target unit \navailable units are (g,kg,lbs)")

else:
    print(f"'{unit}' invalid unit \navailable units are (g,kg,lbs)")

