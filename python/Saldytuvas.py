fridge = {}
recipe = {}

def add_product():
    product_name = input("Enter product name: ")
    product_quantity = float(input("Enter product quantity: "))
    fridge[product_name] = product_quantity

def remove_product():
    product_name = input("Enter product name: ")
    if product_name in fridge:
        fridge.pop(product_name)
        print(f"{product_name} removed from fridge.")
    else:
        print(f"{product_name} not found in fridge.")

def view_products():
    print("Products in fridge:")
    for product_name, product_quantity in fridge.items():
        print(f"{product_name}: {product_quantity}")

def get_fridge_weight():
    weight = 0
    for product_name, product_quantity in fridge.items():
        if product_name.endswith("kg"):
            weight += product_quantity
        elif product_name.endswith("l"):
            weight += product_quantity * 1
        else:
            weight += product_quantity * 1
    return weight

def remove_zero_product():
    empty_keys = []
    for product_name, product_quantity in fridge.items():
        if product_quantity == 0:
            empty_keys.append(product_name)
    for key in empty_keys:
        fridge.pop(key)
    if empty_keys:
        print("The following products have been removed from the fridge because their quantity reached zero:")
        print(empty_keys)

def can_make_dish():
    print("Enter the recipe for one serving:")
while True:
        recipe_input = input()
        if not recipe_input:
            break
        try:
            ingredient, quantity = recipe_input.split(":")
            recipe[ingredient.strip()] = float(quantity.strip())
        except:
            print("Invalid input. Please try again.")
        servings = int(input("Enter the number of servings: "))
        needed = {}
        for ingredient, quantity in recipe.items():
            if ingredient in fridge:
                if ingredient.endswith("kg"):
                    needed[ingredient] = quantity * servings - fridge[ingredient]
            elif ingredient.endswith("l"):
                needed[ingredient] = quantity * servings - fridge[ingredient] * 1
            else:
                needed[ingredient] = quantity * servings - fridge[ingredient] * 1
        else:
            needed[ingredient] = quantity * servings
        enough = True
        shopping_list = {}
        for ingredient, quantity in needed.items():
            if quantity > 0:
                enough = False
            shopping_list[ingredient] = quantity
        if enough:
            print("You have enough ingredients to make the dish!")
        else:
            print("You don't have enough ingredients to make the dish. Here's what you need to buy:")
        for ingredient, quantity in shopping_list.items():
            print(f"{ingredient}: {quantity}")

        surplus = {}
        for ingredient, quantity in fridge.items():
            if ingredient in recipe:
                if ingredient.endswith("kg"):
                    surplus[ingredient] = fridge[ingredient] - recipe[ingredient] * servings
            elif ingredient.endswith("l"):
                surplus[ingredient] = fridge[ingredient] - recipe[ingredient] * servings / 1
            else:
                surplus[ingredient] = fridge[ingredient] - recipe[ingredient] * servings / 1
        else:
            surplus[ingredient] = fridge[ingredient]
        for ingredient, quantity in surplus.items():
            if quantity > 0:
                if ingredient.endswith("kg"):
                    print(f"You can make {quantity / recipe[ingredient]:.1f} more servings with {ingredient}.")
            elif ingredient.endswith("l"):
                print(f"You can make {quantity * 1 / recipe[ingredient]:.1f} more servings with {ingredient}.")
            else:
                print(f"You can make {quantity * 1 / recipe[ingredient]:.1f} more servings with {ingredient}.")

def menu():
    print("Welcome to the fridge program!")
    while True:
        print("Menu:")
        print("1. Add products")
        print("2. Remove products")
        print("3. View fridge contents")
        print("4. Calculate fridge weight")
        print("5. Can make dish?")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            view_products()
        elif choice == "4":
            get_fridge_weight()
        elif choice == "5":
            can_make_dish()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    