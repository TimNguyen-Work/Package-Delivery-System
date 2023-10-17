from datetime import datetime


#Build a class that manages packages for trucks.
class WGUPS_Truck_Package:
    def __init__(self, uid_package, location_package, city_package, us_state_package, us_zipcode_package, deadline_time_package, mass_package, requirement_package, delivery_status_package):
        self.uid_package = uid_package
        self.location_package = location_package
        self.city_package = city_package
        self.us_state_package = us_state_package
        self.us_zipcode_package = us_zipcode_package
        self.deadline_time_package = deadline_time_package
        self.mass_package = mass_package
        self.requirement_package = requirement_package
        self.departure_time_package = None
        self.delivery_time_package = None
        self.delivery_status_package = delivery_status_package

    def __str__(self):
        return "Package: %s, Address: %s, City: %s, State: %s, Zip code: %s, Deadline: %s,Mass: %s, \033[92mDeparture: %s\033[0m, \033[93mDelivery: %s\033[0m, \033[91mStatus: %s\033[0m" % (self.uid_package, self.location_package, self.city_package, self.us_state_package, self.us_zipcode_package, self.deadline_time_package, self.mass_package, self.departure_time_package, self.delivery_time_package, self.delivery_status_package)


    # Create a function to update the 'delivery_status_package' based on user input
    def update_status_with_time(self, input_time):
        if self.delivery_time_package <= input_time:
            self.delivery_status_package = "Delivered"
        elif self.departure_time_package < input_time and self.delivery_time_package > input_time:
            self.delivery_status_package = "En route"
        else:
            self.delivery_status_package = "At the hub"


