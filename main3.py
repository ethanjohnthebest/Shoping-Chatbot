"""
Hello and Welcome to our Store
Kindly enter your name :
Ram
Hello Ram
Choose the department, you wish to shop in
1. Grocery
2. Frozen
3. Utensils
4. Clothes
3
Thankyou
You will be redirected to your desired department
"""

print("Hello and Welcome to our Store")
name = input("What is your Name ")
print(f"Hello {name}")
print("Choose the department, you wish to shop in")
print(f"1. Grocery")
print(f"2. Frozen")
print(f"3. Utensils")
print(f"4. Clothes")
print(f"5. Snacks")
print(" "*20)
store = int(input())
print(f"You have Choosen {store}")
if store == 1:
    print("I Will Do The Code For Grocery")
elif store == 2:
    print("I Will Do The Code For Frozen")
if store == 3:
    print("I Will Do The Code For Utensils")
elif store == 4:
    print("I Will Do The Code For Clothes")
elif store == 5:
    print("I Will Do The Code For Snacks")
else :
    print("Choose 1,2,3,4 or 5")

print(" "*20)
print("Can you please tell us your Budget for shopping?")
