#simple concession stand program
menu={"popcorn":100,"chips":50,"soda":20,"juice":30,"water":40,"cake":65,"ice cream":50}
cart=[]
total=0
print("*****CONCESSION STAND*****")

#print menu
print("----------MENU----------")
for key,value in menu.items():
    print(f"{key:10} : ₹{value:.2f}")
print("------------------------")

#take order from  user
while True:
    food= input("select an item(q for quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"''{food}' is not in menu'\n'Select item from menu'")

#print order and total
print("----------🛒YOUR ORDER🛒----------")
for food in cart:
    total+=menu.get(food)
    print(f"✅{food:10}:₹{menu.get(food)}")
print("\n------------------------")
print(f"💵Total is : ₹{total}")
print("------------------------")    
