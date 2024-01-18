class Dessert:
    def show_menu(self):
        while True:
            try:
                choice = int(input("\n1. Vanilla Ice Cream (INR 80/pc)\n2. Choco lava cake (INR 120/pc)\n3. Ice cream Shake (INR 60/pc)\n"))
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Wrong input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def cart(self, choice):
        if choice == 1:
            self.name = "Vanilla Ice Cream"
            self.price = 80
            self.description = "Made with Milk and essence of vanilla"
        elif choice == 2:
            self.name = "Choco Lava Cake"
            self.price = 120
            self.description = "A Chocolate based cake with melted chocolate filling"
        elif choice == 3:
            self.name = "Ice Cream Shake"
            self.price = 60
            self.description = "Milk Shake with ice cream topped on it, a mouthwatering edible shake"


class Appetizer:
    def show_menu(self):
        while True:
            try:
                choice = int(input("\n1. Potato Wedges (INR 120/plate)\n2. French Fries (INR 100/plate)\n3. Paneer Chilly (INR 180/plate)\n"))
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Wrong input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def cart(self, choice):
        if choice == 1:
            self.name = "Potato Wedges"
            self.price = 120
            self.description = "Fried Potato with wrinkled shape and seasoned with salt and pepper"
        elif choice == 2:
            self.name = "French Fries"
            self.price = 100
            self.description = "Deep Fried Potato sticks with Peri Peri seasonings"
        elif choice == 3:
            self.name = "Paneer Chilly"
            self.price = 180
            self.description = "Paneer Seasoned with veggies and sauce and Saute with golden crisp"


class MainCourse:
    def show_menu(self):
        while True:
            try:
                choice = int(input("\n1. Veg Plate Thali (INR 230/Thali)\n2. Non Veg Plate Thali (INR 260/Thali)\n3. Special Veg Thali (INR 280/Thali)\n4. Special Non Veg Thali (INR 300/Thali)\n"))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Wrong input. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def cart(self, choice):
        if choice == 1:
            self.name = "Veg Plate Thali"
            self.price = 230
            self.description = "A Full meal Thali Served with 4 Rotis and Jeera Rice alongside With salad, paneer, Dal, papad"
        elif choice == 2:
            self.name = "Non Veg Plate Thali"
            self.price = 260
            self.description = "A Full meal Thali Served with 4 Rotis and Jeera Rice alongside With salad, Chicken, Dal, papad"
        elif choice == 3:
            self.name = "Special Veg Thali"
            self.price = 280
            self.description = "A Full meal Thali Served with 4 Rotis and Jeera Rice alongside With salad, 2 paneer sabzi, veg mix, Dal, papad"
        elif choice == 4:
            self.name = "Special Non Veg Thali"
            self.price = 300
            self.description = "A Full meal Thali Served with 4 Rotis and Jeera Rice alongside With salad, 2 Chicken sabzis, Mutton, Dal, papad"
