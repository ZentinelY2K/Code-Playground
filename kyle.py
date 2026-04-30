class Kylee:
    def __init__(self,food,instrument,sport,rock):
        self.food = food
        self.instrument = instrument
        self.sport = sport
        self.rock = rock
    def eat(self):
        return f"Kylee is eating {self.food}!"
    
    def drawing(self):
        return f"Kylee is drawing!"
    
    def play_instrument(self):
        return f"Kylee is playing {self.instrument}!"
    
    def play_sport(self):
        return f"Kylee is playing the following sport {self.sport}!"
    
    def collect_rock(self):
        return f"Kylee collected the following rock: {self.rock}!"


Kylee = Kylee("Ribs","Piano","Boxing","Unakite")

print(Kylee.play_sport())