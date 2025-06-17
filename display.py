import csv
def load_menu_from_csv(file_path):
    flavors = {}
    cones = {}
    
    with open('menu.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = row['Item']
            item_type = row['Type']
            price = int(row['Price'])
            
            if item_type.lower() == 'flavor':
                flavors[item] = price
            elif item_type.lower() == 'cone':
                cones[item] = price
    
    return flavors, cones
def display_menu(flavors, cones):
    print("\nFlavors:")
    for i, (flavor, price) in enumerate(flavors.items(), 1):
        print(f"{i}. {flavor} - Rs.{price}/scoop")
    
    print("\nCone Types:")
    for i, (cone, price) in enumerate(cones.items(), 1):
        print(f"{i}. {cone} - Rs.{price}")

