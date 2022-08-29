class Vehicles:
    driver = 1
    # capacity attribute does not include the driver
    
    def __init__(self, name, mileage, capacity_attributes):
        self.name = name
        self.mileage = mileage
        self.capacity_attributes = capacity_attributes

    def __str__(self):
        pass

class LandVehicles(Vehicles):
    def means_of_movement(self):
        print("Vehicle moves on land")

class WaterVehicles(Vehicles):
    def means_of_movement(self):
        print("Vehicle moves on water")

class AirVehicles(Vehicles):
    def means_of_movement(self):
        print("Vehicle moves on Air")

class FourWheels(LandVehicles):
    def number_of_wheels(self):
        print("Vehicle has four wheels")

class ThreeWheels(LandVehicles):
    def number_of_wheels(self):
        print("Vehicle has Three wheels")

class TwoWheels(LandVehicles):
    def number_of_wheels(self):
        print("Vehicle has two wheels")

class Cars(FourWheels):
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 4 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement=1):
        if self.currentpassenger <= 0:
            return("passenger cannot be less than zero")
        elif self.currentpassenger <= 4:
            self.decrement = decrement
            self.currentpassenger -= self.decrement
        return(decrement, "passenger left")

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)

class Bus(FourWheels):
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
        elif 0 <= self.currentpassenger < 16 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement=1):
        if self.currentpassenger <= 0:
            return("passenger cannot be less than zero")
        elif self.currentpassenger <= 16:
            self.decrement = decrement
            self.currentpassenger -= self.decrement
        return(decrement, "passenger left")

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)

class Trucks(FourWheels):
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 2 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement=1):
        if self.currentpassenger <= 0:
            return("passenger cannot be less than zero")
        elif self.currentpassenger <= 2:
            self.decrement = decrement
            self.currentpassenger -= self.decrement
        return(decrement, "passenger left")

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)

    def load(self):
        pass

class Tricycle(ThreeWheels):
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 4 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement=1):
        if self.currentpassenger <= 0:
            return("passenger cannot be less than zero")
        elif self.currentpassenger <= 3:
            self.decrement = decrement
            self.currentpassenger -= self.decrement
        return(decrement, "passenger left")

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)

class Bicycle(TwoWheels):
    def __init__(self, name, mileage, capacity_attributes):
        super().__init__(name, mileage, capacity_attributes)
        
    def add_passenger(self):
        return self.driver

    def remove_passenger(self):
        return self.driver

    def total_number_passenger(self):
        return self.driver

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.driver * fare)

class MotorCycle(TwoWheels):
    
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 1 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement=1):
        if self.currentpassenger <= 0:
            return("passenger cannot be less than zero")
        elif self.currentpassenger <= 1:
            self.decrement = decrement
            self.currentpassenger -= self.decrement
        return(decrement, "passenger left")

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)

class Ships(WaterVehicles):
    
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 5000 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement):
        if self.currentpassenger <= 0:
            return("passenger cannot be less than zero")
        elif self.currentpassenger <= 5000:
            self.decrement = decrement
            self.currentpassenger -= self.decrement
        return(decrement, "passenger left")

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)
   
    def load(self):
        pass

class Boats(WaterVehicles):
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 8 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement):
        self.decrement = decrement
        if self.decrement > self.currentpassenger:
            print("number to be removed should not be greater than currentpassenger")
            return False
        if self.currentpassenger <= 0:
            return("passenger cannot be zero or less than zero")
        elif self.currentpassenger <= 8:
            self.currentpassenger -= self.decrement
            return(decrement, "passenger left")
        
    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)
   
    def load(self):
        pass

class Canoes(WaterVehicles):
    
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger < 2 and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement):
        self.decrement = decrement
        if self.decrement > self.currentpassenger:
            print("number to be removed should not be greater than currentpassenger")
            return False
        if self.currentpassenger <= 0:
            return("passenger cannot be zero or less than zero")
        if self.currentpassenger <= 2:
            self.currentpassenger -= self.decrement
            return(decrement, "passenger left")
        

    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)
   
    def load(self):
        pass

class Aeroplane(AirVehicles):
    
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger <100  and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement):
        self.decrement = decrement
        if self.decrement > self.currentpassenger:
            print("number to be removed should not be greater than currentpassenger")
            return False
        if self.currentpassenger <= 0:
            return("passenger cannot be zero or less than zero")
        if self.currentpassenger <= 100:
            self.currentpassenger -= self.decrement
            return(decrement, "passenger left")
    
    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)
   
    def load(self):
        pass

class Helicopter(AirVehicles):
    
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than {self.capacity_attributes}")
            return False
        elif 0 <= self.currentpassenger <14  and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement):
        self.decrement = decrement
        if self.decrement > self.currentpassenger:
            print("number to be removed should not be greater than currentpassenger")
            return False
        if self.currentpassenger <= 0:
            return("passenger cannot be zero or less than zero")
        if self.currentpassenger <= 14:
            self.currentpassenger -= self.decrement
            return(decrement, "passenger left")
    
    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)
   
class Jet(AirVehicles):
    def __init__(self, name, mileage, capacity_attributes, currentpassenger, newpassenger):
        super().__init__(name, mileage, capacity_attributes)
        self.newpassenger = newpassenger
        self.currentpassenger = currentpassenger

    def add_passenger(self):
        if (self.currentpassenger + self.newpassenger) > self.capacity_attributes:
            print(f"capacity attribute should not be more than fourteen")
            return False
        elif 0 <= self.currentpassenger < 14  and self.newpassenger > 0:
            self.currentpassenger += self.newpassenger
            return("There are", self.currentpassenger, "passengers in this vehicle")
        if self.newpassenger < 0:
            return False
        if self.currentpassenger == self.capacity_attributes:
            print("capacity attribute has reached it's limit, no passengers can be added")

    def remove_passenger(self, decrement):
        self.decrement = decrement
        if self.decrement > self.currentpassenger:
            print("number to be removed should not be greater than currentpassenger")
            return False
        if self.currentpassenger <= 0:
            return("passenger cannot be zero or less than zero")
        if self.currentpassenger <= 14:
            self.currentpassenger -= self.decrement
            return(decrement, "passenger left")
    
    def total_number_passenger(self):
        return(self.currentpassenger, "remain")

    def totalfare(self, fare):
        self.fare = fare
        return("The total fare left to be collected", self.currentpassenger * fare)
    

vehicle1 = Vehicles("car", "35miles/hour", 4)
car = Cars("Benz", 35, 4, 3, 1)
print(car.add_passenger())
print(car.remove_passenger())
print(car.total_number_passenger())
print(car.totalfare(200))
bus = Bus("16seatersbus", 67, 16, 10, 4)
print(bus.add_passenger())
print(bus.remove_passenger())
print(bus.total_number_passenger())
print(bus.totalfare(500))
trucks = Trucks("big trucks", 560, 2, 1, 1)
print(trucks.add_passenger())
print(trucks.remove_passenger())
print(trucks.total_number_passenger())
print(trucks.totalfare(1000))
bicycle = Bicycle("bicycle", 34, 0)
print(bicycle.add_passenger())
print(bicycle.remove_passenger())
print(bicycle.total_number_passenger())
print(bicycle.totalfare(0))
tricycle = Tricycle("Jincheng", 50, 4, 3, 4)
print(tricycle.add_passenger())
print(tricycle.remove_passenger())
print(tricycle.total_number_passenger())
print(tricycle.totalfare(150))
motorbike = MotorCycle("okada", 440, 1, 0, 1)
print(motorbike.add_passenger())
print(motorbike.remove_passenger())
print(motorbike.total_number_passenger())
print(motorbike.totalfare(150))
ship = Ships("Titanic", 5900, 3000, 2000, 1)
print(ship.add_passenger())
print(ship.remove_passenger(5))
print(ship.total_number_passenger())
print(ship.totalfare(150))
boat = Boats("boaty", 456, 8, 2, 1)
print(boat.add_passenger())
print(boat.remove_passenger(8))
print(boat.total_number_passenger())
print(boat.totalfare(150))
canoe = Canoes("canon", 45, 2, 1, 7)
print(canoe.add_passenger())
print(canoe.remove_passenger(8))
print(canoe.total_number_passenger())
print(canoe.totalfare(250))
aeroplane = Aeroplane("Boeing 747", 456, 100, 90, 10)
print(aeroplane.add_passenger())
print(aeroplane.remove_passenger(4))
print(aeroplane.total_number_passenger())
print(aeroplane.totalfare(150000))
helicopter = Helicopter("Boeing 747", 456, 100, 90, 10)
print(helicopter.add_passenger())
print(helicopter.remove_passenger(4))
print(helicopter.total_number_passenger())
print(helicopter.totalfare(250000))
jet = Jet("Boeing 747", 456, 100, 90, 10)
print(jet.add_passenger())
print(jet.remove_passenger(4))
print(jet.total_number_passenger())
print(jet.totalfare(150000))










