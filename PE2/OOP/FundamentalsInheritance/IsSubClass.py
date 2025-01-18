class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class Jeep(LandVehicle):
    pass
j = Jeep()
print(issubclass(Jeep,(Vehicle,LandVehicle)))
print(isinstance(j,Jeep))