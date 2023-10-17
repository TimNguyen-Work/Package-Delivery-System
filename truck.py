
import datetime
# Build a class for truck
class WGUPS_Truck:
    def __init__(self, truck_package, truck_start_time):
        self.truck_package = truck_package
        self.truck_location = "4001 South 700 East" # Start at the hub
        self.truck_total_mileage = 0.0
        self.truck_start_time = truck_start_time
        self.truck_current_time = truck_start_time
        self.truck_max_package = 16
        self.truck_max_speed = 18
        self.truck_status = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.truck_package, self.truck_location, self.truck_total_mileage, self.truck_start_time, self.truck_current_time, self.truck_max_package,
                                               self.truck_max_speed, self.truck_status)

# Load packages into the truck 1
WGUPS_truck_1 = WGUPS_Truck([1, 13, 14, 15, 16, 19, 20, 26, 29, 30, 31, 34, 37, 40], datetime.timedelta(hours= 8 ))

# Load packages into the truck 2
WGUPS_truck_2 = WGUPS_Truck([2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 17, 18, 25, 28, 32, 36, 38], datetime.timedelta(hours= 9, minutes= 5))

# Load packages into the truck 3
WGUPS_truck_3 = WGUPS_Truck([9, 21, 22, 23, 24, 27, 33, 35, 39], datetime.timedelta(hours= 10, minutes= 20))
