from abc import ABC, abstractmethod
import datetime

# Decorator for logging rentals
def rental_log(func):
    def wrapper(*args, **kwargs):
        print(f"Logging rental action: {func.__name__} called.")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Base class Vehicle
class Vehicle(ABC):
    def __init__(self, vehicle_id, rental_price, availability_status=True):
        self._vehicle_id = vehicle_id  # Protected attribute
        self._rental_price = rental_price  # Protected attribute
        self._availability_status = availability_status  # Protected attribute

    # Getter and Setter methods for vehicle_id
    def get_vehicle_id(self):
        return self._vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self._vehicle_id = vehicle_id

    # Getter and Setter methods for rental_price
    def get_rental_price(self):
        return self._rental_price

    def set_rental_price(self, rental_price):
        self._rental_price = rental_price

    # Getter and Setter methods for availability_status
    def is_available(self):
        return self._availability_status

    def set_availability(self, availability_status):
        self._availability_status = availability_status

    # Abstract method to calculate rental price (to be overridden)
    @abstractmethod
    def calculate_rental_price(self, duration):
        pass

    # Method to check availability (to be overridden)
    @abstractmethod
    def check_availability(self):
        pass

# Subclass Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, vehicle_id, rental_price_per_hour, availability_status=True):
        super().__init__(vehicle_id, rental_price_per_hour, availability_status)

    # Overriding the calculate_rental_price method for cars (charged per hour)
    def calculate_rental_price(self, hours):
        return self.get_rental_price() * hours

    # Overriding the check_availability method for cars
    def check_availability(self):
        return "Car is available" if self.is_available() else "Car is not available"

# Subclass Bike inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, vehicle_id, rental_price_per_km, availability_status=True):
        super().__init__(vehicle_id, rental_price_per_km, availability_status)

    # Overriding the calculate_rental_price method for bikes (charged per kilometer)
    def calculate_rental_price(self, kilometers):
        return self.get_rental_price() * kilometers

    # Overriding the check_availability method for bikes
    def check_availability(self):
        return "Bike is available" if self.is_available() else "Bike is not available"

# Subclass Truck inheriting from Vehicle
class Truck(Vehicle):
    def __init__(self, vehicle_id, rental_price_per_day, availability_status=True):
        super().__init__(vehicle_id, rental_price_per_day, availability_status)

    # Overriding the calculate_rental_price method for trucks (charged per day)
    def calculate_rental_price(self, days):
        return self.get_rental_price() * days

    # Overriding the check_availability method for trucks
    def check_availability(self):
        return "Truck is available" if self.is_available() else "Truck is not available"

# Rental system to log actions for each vehicle rented
class RentalSystem:
    
    @rental_log
    def rent_vehicle(self, vehicle, duration):
        if vehicle.is_available():
            price = vehicle.calculate_rental_price(duration)
            vehicle.set_availability(False)
            print(f"{vehicle.__class__.__name__} rented successfully!")
            print(f"Rental Price: ${price}")
        else:
            print(f"Sorry, {vehicle.__class__.__name__} is not available for rent.")
    
    @rental_log
    def return_vehicle(self, vehicle):
        vehicle.set_availability(True)
        print(f"{vehicle.__class__.__name__} returned successfully!")

# Example usage
if __name__ == "__main__":
    # Creating instances of each vehicle
    car = Car("CAR123", 10)  # $10 per hour
    bike = Bike("BIKE456", 0.5)  # $0.5 per km
    truck = Truck("TRUCK789", 100)  # $100 per day

    # Creating an instance of the rental system
    rental_system = RentalSystem()

    # Renting a car for 5 hours
    rental_system.rent_vehicle(car, 5)

    # Returning the car
    rental_system.return_vehicle(car)

    # Renting a bike for 20 km
    rental_system.rent_vehicle(bike, 20)

    # Returning the bike
    rental_system.return_vehicle(bike)

    # Renting a truck for 3 days
    rental_system.rent_vehicle(truck, 3)

    # Returning the truck
    rental_system.return_vehicle(truck)
