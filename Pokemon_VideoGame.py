# TODO: Complete Project Code Here

class Select():
    def __init__(self):
        self.__pokemons = ['Charmander','Pikachu','Swoobat','Oshawott','Victini']
        self.__raise_error_yN = False 
        self.__pokemon_stats = {
            'Charmander': {
                'Health': 3,'Attack': 4,'Speed': 3
            },
            'Pikachu': {
                'Health': 1, 'Attack': 5,'Speed': 5
            },
            'Swoobat': {
                'Health' : 2, 'Attack' : 3, 'Speed': 5
            },
            'Oshawott':{
                'Health': 5, 'Attack': 1, 'Speed': 2
            },
            'Victini': {
                'Health':3, 'Attack' : 5, 'Speed': 2
            }
        }
        
    def show_pokemon(self):
        print(f"Available: {self.__pokemons}")



    def choose_pokemon(self,user_choice_of_pokemon):
        self.user_choice_of_pokemon = user_choice_of_pokemon
        if user_choice_of_pokemon in self.__pokemons:
            self.__pokemons.remove(self.user_choice_of_pokemon)
        else:
            print("Error | Not processed! Argument must be in the pokemon list")
            self.__raise_error_yN = True
            

    def show_pokemon_stats(self):
        if self.__raise_error_yN == True:
            raise ValueError('Please give a valid Pokemon name beforehand')
        else:
            print(f"{self.user_choice_of_pokemon} : {self.__pokemon_stats[self.user_choice_of_pokemon]}")

            
class attacks(Select):
    def __init__(self):
            Select.__init__() #this inherits the attirbutes from Select
            
            self.__pokemon_attacks = [['Fire Storm','Inferno','Furnace'],['ZAP!','Short Circuit','A TRILLION volts!'],
                              ['Sonic BOOM','Ear Blooshed','Speed of sound'],['Tsunami','Acid Rain','Fatal Wave'],
                               ['Lucky','V','Black Energy']]
            
            self.__charmander_attacks = self.__pokemon_attacks[0]
            self.__pikachu_attacks = self.__pokemon_attacks[1]
            self.__swoobat_attacks = self.__pokemon_attacks[2]
            self.__oshawott_attacks = self.__pokemon_attacks[3]
            self.__victini_attacks = self.__pokemon_attacks[4]
        
    def Charmander(self):
        if Select.user_choice_of_pokemon == 'Charmander': #Notice how 'Select' acts as self, thats because 'self' is literally the name of the Class
            print(self.__charmander_attacks)
        else:
            raise ValueError('Please select your corresponding Pokemon')
        
    def Pikachu(self):
        if Select.user_choice_of_pokemon == 'Pikachu': #Notice how 'Select' acts as self, thats because 'self' is literally the name of the Class
            print(self.__pikachu_attacks)
        else:
            raise ValueError('Please select your corresponding Pokemon')
    
    def Swoobat(self):
        if Select.user_choice_of_pokemon == 'Swoobat': #Notice how 'Select' acts as self, thats because 'self' is literally the name of the Class
            print(self.__swoobat_attacks)
        else:
            raise ValueError('Please select your corresponding Pokemon')
    
    def Oshawott(self):
        if Select.user_choice_of_pokemon == 'Oshawott': #Notice how 'Select' acts as self, thats because 'self' is literally the name of the Class
            print(self.__oshawott_attacks)
        else:
            raise ValueError('Please select your corresponding Pokemon')
        
    def Victini(self):
        if Select.user_choice_of_pokemon == 'Victini': #Notice how 'Select' acts as self, thats because 'self' is literally the name of the Class
            print(self.__victini_attacks)
        else:
            raise ValueError('Please select your corresponding Pokemon')
        
        
        
        
            
    
        

Select = Select()
attacks = attacks()
Select.show_pokemon()
Select.choose_pokemon('Pikachu')
Select.show_pokemon_stats()
attacks.Pikachu()