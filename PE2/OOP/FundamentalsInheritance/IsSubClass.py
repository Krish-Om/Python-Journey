class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class Jeep(LandVehicle):
    pass

print(issubclass(Jeep,(Vehicle,LandVehicle)))