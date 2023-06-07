class  Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrakedVehicle(LandVehicle):
    pass
#print('issubclass(TrakedVehicle,(Vehicle))
for cls1 in [Vehicle, LandVehicle, TrakedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrakedVehicle]:
        print(issubclass(cls1,cls2), end='\t')
    print()