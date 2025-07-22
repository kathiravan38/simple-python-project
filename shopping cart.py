#simple shopping cart program
items=[]
prices=[]
total=0
i=0
while True:
    item=input("Enter the name of item you want to buy (q for quit): ").lower()
    if item == 'q':
        break
    else:
        price=float(input(f"Enter the price of '{item.upper()}':$ "))
        items.append(item)
        prices.append(price)
    i+=1  

print("-----YOUR CART-----")

for x in range(i):
    print(f"{items[x].upper()}\t{prices[x]}")
for cart_price in prices:
    total+=cart_price
    
   
print("-----YOUR TOTAL PRICES-----")
print(f"Total = ${total}")
