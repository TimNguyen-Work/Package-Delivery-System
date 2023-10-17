from HashTable import Hash_Table
import csv
from package import *
import datetime

from truck import *

# Create a list called 'WGUPS_list_address' to store data from the 'Address_Data.csv' file.
with open("DataCSV/Address_Data.csv") as csv1:
    WGUPS_list_address = list(csv.reader(csv1))
# Create a list called 'WGUPS_list_package' to store data from the 'Package_Data.csv' file.
with open("DataCSV/Package_Data.csv") as csv2:
    WGUPS_list_package = list(csv.reader(csv2))

# Update the location and zipcode for package with ID 9, as this package needs to align with the schedule of truck 3, which starts at 10:30.
correct_address = "410 S State St"
correct_zipcode = "84111"
WGUPS_list_package[8][1] = correct_address
WGUPS_list_package[8][4] = correct_zipcode

# Create a list called 'WGUPS_list_distance' to store data from the 'Distance_Data' file.
with open("DataCSV/Distance_Data.csv") as csv3:
    WGUPS_list_distance = list(csv.reader(csv3))

# Create hash table using class Hash_Table
WGUPS_package_Hash_Table = Hash_Table()


# Populate the hash table 'WGUPS_package_Hash_Table' with package objects
def populate_hash_table():
    with open("DataCSV/Package_Data.csv") as WGUPS_package_csv:
        WGUPS_package_data = csv.reader(WGUPS_package_csv)
        for package in WGUPS_package_data:
            WGUPS_package_ID = int(package[0])
            WGUPS_package_location = package[1]
            WGUPS_package_city = package[2]
            WGUPS_package_state = package[3]
            WGUPS_package_zipcode = package[4]
            WGUPS_package_time = package[5]
            WGUPS_package_mass = package[6]
            WGUPS_package_requirement = package[7]
            WGUPS_package_status = "At the hub"

            # Update the location and zipcode for package with ID 9, as this package needs to align with the schedule
            # of truck 3, which starts at 10:30.
            if WGUPS_package_ID == 9:
                WGUPS_package_location = "410 S State St"
                WGUPS_package_zipcode = "84111"
            # Package object
            truck_load_package = WGUPS_Truck_Package(WGUPS_package_ID, WGUPS_package_location, WGUPS_package_city,
                                                     WGUPS_package_state, WGUPS_package_zipcode,
                                                     WGUPS_package_time, WGUPS_package_mass, WGUPS_package_requirement,
                                                     WGUPS_package_status)
            # Add data into WGU_package_Hash_Table using key ID from WGUPS_package_ID
            WGUPS_package_Hash_Table.add_uid_key(WGUPS_package_ID, truck_load_package)


# Create a function called 'find_package_using_package_ID' to find a package using the user's input.
def find_package_using_package_ID(package_ID):
    find_package = WGUPS_package_Hash_Table.find_uid_key(package_ID)
    print(str(find_package))


# Create a function called 'matching_street_name' to match the 'street_address' from 'Package_data.csv' with the data from 'Address_data.csv'.
def matching_street_name(street_address):
    for i in range(len(WGUPS_list_address)):
        if street_address == WGUPS_list_address[i][2]:
            return WGUPS_list_address[i][0]


# Create a function named 'distance_from_truck_to_next_location' to calculate the distance between the truck's current location and the next destination.
def distance_from_truck_to_next_destination(truck_location, next_destination):
    truck = int(truck_location)
    destination = int(next_destination)
    distance = WGUPS_list_distance[truck][destination]
    if distance == "":
        distance = WGUPS_list_distance[destination][truck]
    return float(distance)


# Create a function named 'nearest_neighbor_algorithm' to calculate the distance traveled by the truck using the nearest neighbor algorithm
def nearest_neighbor_algorithm(WGUPS_truck):
    # Because the truck starts at the hub (Western Governors University - 4001 South 700 East), the truck_location_ID is 0.
    truck_location_ID = 0
    # Create a list of packages to be delivered from the truck class
    package_list = WGUPS_truck.truck_package
    # Create a 'min_distance' variable to find the minimum distance from the truck to the delivery location.
    min_distance = 100
    # Create a 'min_address' variable to store the shortest location
    min_address = None
    # Create a 'min_address_ID' variable to store the shortest location ID
    min_address_ID = None
    # Create a 'min_address_index' variable to store the shortest location index
    min_address_index = None
    # Create a 'total_distance' variable to store the total distance traveled by the truck.
    total_distance = float(0)
    # Create a variable named 'truck_depart_time' to store the time of the truck's departure.
    truck_depart_time = WGUPS_truck.truck_start_time
    # Create an empty list to store a list of package IDs.
    package_list_ID = []
    # Use the 'matching_street_name' function to match package IDs between 'Package_Data.csv' and 'Address_Data.csv',
    # which will be used to find corresponding distances in the 'Distance_data.csv'.
    for package in package_list:
        package = WGUPS_list_package[package - 1][1]
        package = matching_street_name(package)
        package_list_ID.append(
            package)  # Create a 'package_list_ID' variable to reduce the time complexity when calculating distances.

    # Create a loop to iterate 'n' times for each package in the list.
    for i in range(len(package_list_ID)):

        # Create a loop to iterate 'n' times for each package in the list.
        for package_ID in package_list_ID:
            package_location = package_ID
            truck_location = truck_location_ID
            # Use the function 'distance_from_truck_to_next_location' 'to find the distance between package location and truck location
            distance = distance_from_truck_to_next_destination(package_location, truck_location)
            # Implement a logic to determine the shortest distance from the truck's current location to the next package.
            if distance < min_distance:
                min_distance = distance
                min_address_ID = package_ID
                min_address = WGUPS_list_address[int(package_ID)][2]
                min_address_index = package_list_ID.index(package_ID)

        # Update the truck's location.
        truck_location_ID = min_address_ID
        WGUPS_truck.truck_location = min_address
        # Remove the locations that the truck has passed by.
        package_list_ID.remove(min_address_ID)
        # Update total distance that the truck has passed by.
        total_distance = total_distance + min_distance
        # Create a 'passing_time' variable to calculate the duration it takes for the truck to pass by using the nearest neighbor algorithm.
        passing_time = datetime.timedelta(hours=(min_distance / WGUPS_truck.truck_max_speed))
        # Create a 'delivery_time' variable to calculate the time when package was delivered.
        delivery_time = truck_depart_time + passing_time
        # Reset the 'min_distance' for comparison.
        min_distance = 100
        # Use the 'min_address_index' to find the corresponding index in 'package_list' and store it in 'package_index'.
        package_index = package_list[min_address_index]
        # Remove the package that has been delivered.
        package_list.pop(min_address_index)
        # Use 'package_index' as the key to retrieve the corresponding value from the hash table and store it in the 'hash_package' variable.
        hash_package = WGUPS_package_Hash_Table.find_uid_key(package_index)
        # Update the departure information for the package in the hash table.
        hash_package.departure_time_package = truck_depart_time
        # Update the delivery information for the package in the hash table.
        hash_package.delivery_time_package = delivery_time
        # Update the truck current time
        WGUPS_truck.truck_current_time = delivery_time
        # Update the truck delivery time
        truck_depart_time = delivery_time

    # Calculate the distance between the last location of truck and the hub
    back_to_hub = distance_from_truck_to_next_destination(0, min_address_ID)
    # Add the distance between the last location of truck and the hub to the total_distance
    total_distance += back_to_hub
    # Update the total mileage of the truck
    WGUPS_truck.truck_total_mileage = total_distance


# Create a function called 'display_all_packages' that takes an input 'input_time' to display the status of all packages.
def display_all_packages(input_time):
    for WGUPS_package_ID in range(1, 41):
        WGUPS_package = WGUPS_package_Hash_Table.find_uid_key(WGUPS_package_ID)
        WGUPS_package.update_status_with_time(input_time)
        print(str(WGUPS_package))


# Create a function named 'display_package' that takes 'input_time' and 'package_ID' to display the status of a single package.
def display_package(package_ID, input_time):
    WGUPS_package = WGUPS_package_Hash_Table.find_uid_key(package_ID)
    WGUPS_package.update_status_with_time(input_time)
    print(str(WGUPS_package))


