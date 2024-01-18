from Food_Ordering_Class import *
from colorama import Fore

def food_menu():
    price = 0
    pay = ""
    id = ""
    y = ""
    des = Dessert()
    app = Appetizer()
    mncr = MainCourse()
    i = 1
    l = []
    while True:
        print(Fore.CYAN,"\nWELCOME TO FOOD ORDERING SECTION\n\nWHAT IS IT THAT YOU'D LIKE TO ORDER?")
        print("\n1. Dessert\n2. Appetizer\n3. Main Course\n")
        choice = int(input())
        
        
        if choice > 3 or choice < 1:
            continue
        if choice == 1:
            
            print(Fore.WHITE,"\n               DESSERT                  \n")
            dc = des.show_menu()
            des.cart(dc)
            
        elif choice == 2:
            print(Fore.WHITE , "\n               APPETIZER                  \n")
            ac = app.show_menu()
            app.cart(ac)
        elif choice == 3:
            print(Fore.WHITE,"\n              MAIN MENU                  \n")
            mc = mncr.show_menu()
            mncr.cart(mc)

        if choice == 1:
            print("\n\nYour Item : ")
            print(f"\n           {des.name}  for INR {des.price}\n          {des.description}")
            l.append(f"{des.name}  for INR {des.price}          {des.description}")
            price += des.price
        elif choice == 2:
            print("Your Item : ")
            print(f"\n           {app.name}  for INR {app.price}\n           {app.description}")
            l.append(f"{app.name}  for INR {app.price}           {app.description}")
            price += app.price
        elif choice == 3:
            print(f"Your Item : \n\n           {mncr.name}  for INR {mncr.price}\n           {mncr.description}")
            l.append(f"{mncr.name}  for INR {mncr.price}           {mncr.description}")
            price += mncr.price
        
        y = input("\n\nWant to order any other food? (y/n)")

        if y.upper() != 'Y':
            print("\n\nEAT WELL :)\nYOUR BILL : \n\n\n")
            a = 1
            d = []
            for i in l:
                print(f"{a} : {i}")
                d.append(i)

                a += 1
            
            print(Fore.RED,f"\n\n\n\nTotal Bill = INR {price} + (TAX) {price * 0.18}")
            print(f"\n\nGRAND TOTAL  = INR {price + (price * 0.18)}")
            print("\n\n\nHow would you like to pay? (Online/Cash)")
            pay = input()
            if pay.upper() == "ONLINE" or pay.upper() == "CASH":
                if pay.upper() == "ONLINE":
                    print("\nEnter Upi id : ")
                    id = ["1"]
                    while True:
                            id = input().split("@") 
                            if(len(id) == 2 ):
                                break
                            else:
                                print("Please input valid upi id")
                        
                        
                    print(f"\nSent the request to pay {price + (price * 0.18)} to your upi id {id}")
                else:
                    print(f"\nPlease pay {price + (price * 0.18)} with the cash With Change......Thank you :)")
            print("\nTHANK YOU FOR CHOOSING OUR TREAT. HAVE A GREAT DINE :)")
            return 101
            break

