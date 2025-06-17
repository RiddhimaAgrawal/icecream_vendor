flavors = {
    'Vanilla': 30,
    'Chocolate': 40,
    'Strawberry': 35,
    'Mango': 45
}

cones = {
    'Waffle': 20,
    'Cup': 10,
    'Sugar Cone': 15
}
import csv
with open('menu.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item', 'Type', 'Price'])
    for flavor, price in flavors.items():
        writer.writerow([flavor, 'Flavor', price])
    for cone, price in cones.items():
        writer.writerow([cone, 'Cone', price])
