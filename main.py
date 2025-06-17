from display import load_menu_from_csv, display_menu
def take_order(flavors, cones):
    flavor_names = list(flavors.keys())
    cone_names = list(cones.keys())
    try:
        flavor_choice = int(input("\nChoose a flavor (1-4): "))
        scoops = int(input("Number of scoops: "))
        cone_choice = int(input("Choose a cone type (1-3): "))
    except ValueError:
        print("X Invalid input! Please enter numbers only.")
        return take_order(flavors, cones)
    if not (1 <= flavor_choice <= len(flavor_names)) or not (1 <= cone_choice <= len(cone_names)):
        print("❌ Invalid choice! Try again.")
        return take_order(flavors, cones)

    flavor = flavor_names[flavor_choice - 1]
    cone = cone_names[cone_choice - 1]

    return flavor, scoops, cone


def calculate_price(flavor, scoops, cone, flavors, cones):
    flavor_price = flavors[flavor] * scoops
    cone_price = cones[cone]
    total = flavor_price + cone_price
    return flavor_price, cone_price, total


from tabulate import tabulate

def show_bill(order_list):
    headers = ["Flavor", "Scoops", "Cone", "Flavor Price", "Cone Price", "Total"]
    print("\nBILLING DETAILS:")
    print(tabulate(order_list, headers=headers, tablefmt="grid"))
def main():
    flavors, cones = load_menu_from_csv('menu.csv')
    display_menu(flavors, cones)
    orders = []
    while True:
        
        flavor, scoops, cone = take_order(flavors, cones)
        f_price, c_price, total = calculate_price(flavor, scoops, cone, flavors, cones)
        orders.append([flavor, scoops, cone, f_price, c_price, total])

        cont = input("Do you want to order more? (yes/no): ").lower()
        if cont != 'yes':
            break

    show_bill(orders)
if __name__ == "__main__":
    main()