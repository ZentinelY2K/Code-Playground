robotics_inventory = {
    'microcontroller_A': 25,
    'servo_motor_20kg': 12,
    'ultrasonic_sensor_v3': 8,
}
robotics_inventory['battery_pack_3s'] = 30
print(f"New values: {robotics_inventory}")
robotics_inventory['servo_motor_20kg'] += 5
print(f"New servo quantity: {robotics_inventory['servo_motor_20kg']}")
if 'old_camera_module' in robotics_inventory:
    del robotics_inventory['old_camera_module']
else:
    print('Part Not Found in Inventory')
for part, quantity in robotics_inventory.items():
    print(f"{part} - Quantity: {quantity}")
#check for unique parts (lone parts)
number_of_unique= len(robotics_inventory)
print(number_of_unique)