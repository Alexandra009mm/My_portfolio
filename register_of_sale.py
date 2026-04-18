keed_register = "yes" 
total_general = 0 
sales ={} 
iden = 0 

validation_rep = 1 
while validation_rep == 1: 
    try: 
        repetitions = int(input(" \n how many repetitions do you want to do?: ")) 
        if repetitions >= 1: 
            validation_rep = 2 
        else: 
            print("the repetitions must be a number\n") 
            validation_rep = 1 
    except ValueError: 
        print("error: Enter the number of repetitions: \n") 
        validation_rep = 1 

print("*" * 42)
print("| welcome! let's go to register your sale |".center(42))
print("*" * 42 + "\n")

for i in range(repetitions): 
    a = 1 
    while a == 1: 
        name = input("enter yor name: ").lower().strip( ) 
        if not name: 
            print("error, enter a name.\n") 
            a = 1 
        else: 
            a = 0 
    b = 2 
    while b ==2: 
        try: 
            price = float(input("enter the price of the product: ")) 
            if price <= 0: 
                print("Error. enter a valid price: \n") 
                b = 2 
            else: 
                b = 0 
        except ValueError: 
            print("Enter a correct price: \n") 
            b = 2 
    c = 3 
    while c == 3: 
        try: 
            quantity = int(input("enter quantity: ")) 
            if quantity <= 0: 
                print("Error, enter a valid quantity\n") 
                c = 3 
            else: 
                c = 0 
        except ValueError: 
            print("enter a quantity \n") 
            c = 3 
            
    total_cost = price * quantity 
    sale = { "costumer_name": name, "price": price, "quantity": quantity, "total": total_cost } 
    sales[iden] = sale 
    iden += 1 
    total_general += total_cost 
    print("Check, sale successfully registered!\n") 
    print(f"name: {name.capitalize()} | price: {price} | quantity: {quantity} | total cost: {total_cost} \n \n")


suma_quantity = 0 
for v in sales.values(): 
    suma_quantity += v['quantity'] 

print("*" * 42)
print("| RESUMMARY |".center(42)) 
print("*" * 42)
print(f"total costumers: {len(sales)}".center(42))
print(f"total quantity sold: {suma_quantity}".center(42))
print(f"total general: ${total_general:.2f}".center(42))
print("-" * 42)