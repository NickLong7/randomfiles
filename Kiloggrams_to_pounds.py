weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L" :
    convertedkg = (.453 * int(weight))
    print(f"You are {convertedkg} Kilograms")
elif unit.upper() == "K":
    convertedlbs = (2.2 * int(weight))
    print(f"You are {convertedlbs} Pounds")
