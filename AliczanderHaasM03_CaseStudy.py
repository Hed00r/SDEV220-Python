class Vehicle:
    def __init__(self, vehicletype):
        self.vehicletype = vehicletype


class Automobile(Vehicle):
    def __init__(self, vehicletype, year, make, model, doors, roof):
        Vehicle.__init__(self, vehicletype)
        self.year = year
        self.make = make
        self. model = model
        self.doors = doors
        self.roof = roof


def main():
    vehicletype = input('Input the type of vehicle: ')
    year = input('Input the year of the ' + vehicletype + ' ')
    make = input("Input the make of " + vehicletype + " ")
    model = input("Input the model of " + vehicletype + " ")
    doors = int(input("How many doors does the "+vehicletype+" have?"))
    roof = input("What type of roof does the "+vehicletype+" have? ")

    print('Vehicle Type: ' + vehicletype + "\nVehicle Year: " + year + "\nVehicle Make: " + make +
          "\nVehicle model:" + model + "\nVehicle doors: " + str(doors) + "\nVehicle roof type: " + roof)

main()
