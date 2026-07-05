
with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
   parsed = line.split("\t")
   currencyDict[parsed[0]] = parsed[1]
   
amount = int(input("Enter The Amount: \n"))

print("Enter The Name of The Currency You Want to Convert This Amount? Available Options: \n")

[print(item) for item in currencyDict.keys()]
currency = input("Enter One of These Values: ")
print(f"{amount} PKR is Equal To {amount *float(currencyDict[currency])} {currency}")