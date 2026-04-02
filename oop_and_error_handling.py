class Sentinel:
    def __init__(self,id,battery_level,status):
        """
        Paramteres:
        id = name of model
        battery_level = percentage 1-100
        status = on/off
        """
        self.id = id
        self.battery_level = battery_level
        self.status = status

    def respond_to_threat(self,threat_level):
        """
        Argument must be 1-3
        """
        self.threat_level = threat_level
        if self.threat_level < 1 or self.threat_level > 3:
            print("Invalidated Input, please make sure range is within 1-3")
        elif self.threat_level == 1:
            print(f"Model: {self.id} - Warning Rounds Mode Activated | Bring to Justice")

        elif self.threat_level == 2:
            print(f"Model: {self.id} - Hazardous Rounds Mode Activated | Dead or Alive")

        elif self.threat_level == 3:
            print(f"Model: {self.id} - Deadly Rounds Mode Activated | Kill Target At All Costs")
        
    def get_status(self):
        try:
          if self.threat_level < 1 or self.threat_level > 3:
            raise AttributeError('Please Input A Number Within Range as Seen Previously')
          print(f"Status: Mode > {self.threat_level} Battery_Level > {self.battery_level} Status > {self.status}")
        except AttributeError:
            raise AttributeError('Please Make sure to give Threat_level argument beforehand')


Sentinel = Sentinel('Turret','64%','On')
Sentinel.respond_to_threat(3)
Sentinel.get_status()