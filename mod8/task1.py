class Transport():
    def __init__(self, coordinates:tuple, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number
    
    def __str__(self) -> str:
        return f"Coordinates: {self.coordinates}, Speed: {self.speed}, Brand: {self.brand}, Year: {self.year}, Number: {self.number}"
    
    def isInArea(self, pos_x, pos_y, length, width):
        return (self.coordinates[0] >= pos_x and self.coordinates[0] <= pos_x + width) and (self.coordinates[1] >= pos_y and self.coordinates[1] <= pos_y + length)
    
    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, coordinates):
        if (type(coordinates) != tuple or len(coordinates) != 2 or type(coordinates[0]) != int or type(coordinates[1]) != int):
            raise Exception()
        self._coordinates = coordinates
    
    @property
    def speed(self):
        return self.speed
    
    @speed.setter
    def speed(self, speed):
        if (type(speed) != int or speed < 0):
            raise Exception()
        self.speed = speed
        
    @property
    def brand(self):
        return self.brand
    
    @brand.setter
    def brand(self, brand):
        if (type(brand) != str or brand == ''):
            raise Exception
        self.brand = brand
        
    @property
    def year(self):
        return self.year
    
    @year.setter
    def year(self, year):
        if (type(year) != int or year < 0):
            raise Exception()
        self.year = year
        
    @property
    def number(self):
        return self.number
    
    @number.setter
    def number(self, number):
        if (type(number) != int or number < 0):
            return self.number
        
class Passenger:
    @property
    def passenger_capacity(self):
        return self.__passenger_capacity
        
    @passenger_capacity.setter
    def passenger_capacity(self, passenger_capacity):
        if (passenger_capacity < 0 or type(passenger_capacity) != int):
            raise Exception()
        self.__passenger_capacity = passenger_capacity
    
    @property
    def number_of_passenger(self):
        return self.__number_of_passenger
    
    @number_of_passenger.setter
    def number_of_passenger(self, number_of_passenger):
        if (number_of_passenger < 0 or type(number_of_passenger) != int):
            raise Exception()
        self.__number_of_passenger = number_of_passenger
        
class Cargo():
    @property
    def carrying(self):
        return self.__carrying
    
    @carrying.setter
    def carrying(self, carrying):
        if (carrying < 0 or type(carrying) != int):
            raise Exception()
        self.__carrying = carrying
            
class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if (height < 0 or type(height) != int):
            raise Exception()
        self.__height = height

class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port
    
    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, port):
        if (type(port) != str):
            raise Exception()
        self.__port = port
        
class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        
class Buss(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        
class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        
class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)
        
class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(coordinates, speed, brand, year, number, height)
        Ship.__init__(coordinates, speed, brand, year, number, port)
        
b = Transport((1, 2), 432, "asfds", 1203, 23)