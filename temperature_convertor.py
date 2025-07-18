#celsius to fahrenheit and kelvin
def celsius(temp,targetunit):
    if targetunit == "f":
        convert_temp= round((temp*9/5)+32, 2)
        print(f"the temperature in fahrenheit is {convert_temp} °F")
    elif targetunit == "k":
        convert_temp= round(temp+273.15, 2)
        print(f"the temperature in kelvin is {convert_temp} K")
    elif targetunit == "c":
        print("both the unit are same, no conversion is needed")
    else:
        print(f"'{targetunit}' is invalid target unit")

#fahrenheit to celsius and kelvin       
def fahrenheit(temp,targetunit):
    if targetunit == "c":
        convert_temp= round((temp-32)*5/9, 2)
        print(f"the temperature in celsius is {convert_temp} °C")
    elif targetunit == "k":
        convert_temp= round(((temp-32)*5/9)+273.15, 2)
        print(f"the temperature in kelvin is {convert_temp} K")
    elif targetunit == "f":
        print("both the unit are same, no conversion is needed")
    else:
        print(f"'{targetunit}' is invalid target unit")

#kelvin to celsius and fahrenheit       
def kelvin(temp,targetunit):
    if targetunit == "c":
        convert_temp= round(temp-273.15, 2)
        print(f"the temperature in celsius is {convert_temp} °C")
    elif targetunit == "f":
        convert_temp= round(((temp-273.15)*9/5), 2)
        print(f"the temperature in fahrenheit is {convert_temp} °F")
    elif targetunit == "k":
        print("both the unit are same, no conversion is needed")
    else:
        print(f"'{targetunit}' is invalid target unit")

temp=float(input("enter the temperature: "))
unit=input("enter temperature unit celsius,fahrenheit or kelvin(C,F or K): ").lower()
if unit in ['c','f','k']:
    tarunit=input("enter the target unit (C,F or K): ").lower()
    if unit == "c":
        celsius(temp,tarunit)
    elif unit == "f":
        fahrenheit(temp,tarunit)
    elif unit == "k":
        kelvin(temp,tarunit)
else:
    print(f"'{unit}' invalid temperature unit")
