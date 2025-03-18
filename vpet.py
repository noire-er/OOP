class VirtualPet:
    def__init__(self, name, energy, hunger):
        self.name = name
        self.energy = 10
        self.hunger = 0 


    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.hunger += 2
            print(f"{self.name} has been fed and has {self.hunger} hunger levels")
        else:
            print("Too tired to play")





# this class has the following methods:
# (1) play() - simulate playing by reducing the energy by 2 and increase the hunger by 2
#     each time this method is called. If insufficient energy, prints "Too tired to play"



    def feed(self):
        self.hunger = max(0, hunger - 3)
        print(f"{self.name} was fed and now has {self.hunger} hunger levels")
# (2) feed() - to simulate feeding the pet and reducing hunger by reducing hunger by the formula
#     hunger = max(0, hunger - 3). If hunger is less than 0, the pet is overfeed (which is possible)


    def sleep(self):
        self.energy += 10
        print(f"{self.name} has slept and gained {self.energy} energy levels")
# (3) sleep() - let the pet sleep to restore energy by increasing the energy by 10.

    def __str__(self):
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger levels"
# (4) __str__ - returns the details of the pet in the format "pet_name with x energy points and y hunger level", 
#     e.g., Timmy with 100 energy points and 0 hunger level
