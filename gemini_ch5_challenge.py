#Gemini chapter five challenge
inventory = ["Laptops","Smartphones","Iot Devices","Accesories"]
print(inventory)
for loop_one in inventory:
    print(f"We stock: {loop_one}")
high_demand_accesories = inventory[:3]
for loop_two in high_demand_accesories:
    print(f"{loop_two} Is currently in high demand")
new_arrivals = inventory[:]
new_arrivals.append("Gaming Consoles")
new_arrivals.remove("Accesories")
print(inventory)
print(new_arrivals)
store_hours =(7,20)
"""store_hours[1] = 21"""
print("It failed because tuples are immutable, meaning they can't be changed unless rewritten")
store_hours = (7,21)
print(store_hours)
