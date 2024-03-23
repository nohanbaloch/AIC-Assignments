class Spaceship():

    def __init__(self, name, crew, fuel, mass, acceleration, engine):

        self.name = name
        self.crew = crew
        self.fuel = fuel
        self.mass = mass
        self.acceleration = acceleration
        self.engine = engine

    def launch(self):
        print(f"{self.name} is launching!")

    def accelerote(self):
        print(f"{self.name} is accelerating at {self.acceleration} km/s^2")

    def stop_engine(self):
        print(f"{self.name}'s engine is stoped")
    
 
dragon1 = Spaceship('dragon1', 3, 1000, 400, 29.4, 2)

print(f"Spaceship name: {dragon1.name}")
print(f"craw members: {dragon1.crew}")
print(f"Fuel : {dragon1.fuel}")
print(f"Mass: {dragon1.mass} kg")
print(f"acceleration: {dragon1.acceleration}")
print(f"no of engine in this spaceship: {dragon1.engine}")

#function of space ship
dragon1.launch()
dragon1.accelerote()
dragon1.stop_engine()