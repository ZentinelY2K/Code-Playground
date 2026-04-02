#Gemini OOP challenge
class servo_motor:
    def __init__(self,model,torque_capacity,power_supply_voltage):
        self.model = model
        self.torque_capacity = torque_capacity
        self.power_supply_voltage = power_supply_voltage
        self.pos = None
    def write(self,pos):
        self.pos = pos
    def get_pos(self):
        print(f'Current Position: {self.pos}')
    
class arm(servo_motor):
    def __init__(self,model,torque_capacity,power_supply_voltage,layer_num):
        servo_motor.__init__(self,model,torque_capacity,power_supply_voltage)
        self.layer_num = layer_num
        self.servo_layers = []
        self.servo_counter = 0
    def servo_layer(self,add=False,remove=False):
        if add:
            self.servo_counter += 1
            while True:
              new_servo = input("Model of the servo?")
              if new_servo.isalnum(): #if it has letters and/or digits
                 self.servo_layers.append(new_servo)
                 break
              else:
                  print("Try Again")

        elif remove:
            remove_servo = input("What servo model do we remove?")
            if remove_servo in self.servo_layers:
               self.servo_layers.remove(remove_servo)
               self.servo_counter -= 1
            else:
                print("Doesn't exist in list.")
    def see_servos(self):
        print(f"Total number of servos ({self.servo_counter})  > {self.servo_layers}")
    

servo_arm = arm('MG90 Servos','2.2kg','5v',0)
servo_arm.servo_layer(True,False)
servo_arm.see_servos()
servo_arm.write(90) 
servo_arm.get_pos()

class Dog:
    def __init__(self):
       self.__val = 0
Dog = Dog()
Dog.__val = 2
print(Dog.__val)
#new