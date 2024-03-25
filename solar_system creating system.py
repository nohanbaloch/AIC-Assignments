class Planet:
    def __init__(self, name, color, mass, Atmosphere, diameter, orbital_period, distance_from_sun):
        self.name = name
        self.color = color
        self.mass = mass
        self.Atmosphere = Atmosphere
        self.diameter = diameter
        self.orbital_period = orbital_period
        self.distance_from_sun = distance_from_sun

    def __str__(self):
        return f"Planet: {self.name} (color: {self.color},mass:{self.mass}, Atmosphere: {self.Atmosphere},  diameter: {self.diameter}, distance_from_sun: {self.distance_from_sun})"



class SolarSystem:
    def __init__(self):
        # Create planets here
        self.planets = [] # astronomical units (AU):
        self.add_planet("Mercury", "gray", 0.0553, 'Trace', 4879, 0.24,'0.39_AU')
        self.add_planet("Venus", "yellow", 0.815, 'Thick_CO2', 12104, 0.62, '0.72_AU')
        self.add_planet("Earth", "blue", 1.000, 'Nitrogen-Oxygenv', 12742, 1.00, '1_AU')
        self.add_planet("Mars", "red", 0.107, "Thin_CO2", 6779, 1.67, '1.52_AU')
        self.add_planet("Jupiter", "yellow_brown_red", 317.8, 'Hydrogen-Helium', 139822, 11.86, '5.20_AU' )
        self.add_planet("Saturn", "yellow_brown_grey", 95.2, 'Hydrogen-Helium', 116464, 29.46, '9.54_AU')
        self.add_planet("Uranus", "cyan", 14.5, 'Hydrogen-Helium', 50724, 84.01, '19.22 AU')
        self.add_planet("Neptune", "blue", 17.1, 'Hydrogen-Helium', 49244, 164.8, '30.06_AU')

    def rotate(self, name, color, mass, Atmosphere, diameter, orbital_period, distance_from_sun):
        print(f"The name of the is {name}, the color of this planet is {color}, the mass of the planet is {mass} ")

    def add_planet(self, name, color, mass, Atmosphere, diameter, orbital_period, distance_from_sun):
        self.planets.append(Planet(name, color, mass, Atmosphere, diameter, orbital_period, distance_from_sun))

    def display_planets(self):
        for planet in self.planets:
            print(planet)

    
# Create a Solar System object
solar_system = SolarSystem()

# Display the planets in the solar system
solar_system.display_planets()

#    def user():
#        if name is 0:
#            print("Enter a name for your planet ")
#            add_planet(name)
#        elif  ():


class dwarf_planet:
    def __init__(self):
        self.planets = []
        self.add_planet("Pluto")

# next adding the ability for the user to make planet and solor systems using gui
# uncomplete