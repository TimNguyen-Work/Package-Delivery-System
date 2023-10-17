from datetime import timedelta
import function
import truck
from truck import *

class Main:
    # Show the interface for the user
    print("Please choose from the following options:")
    print("Choose 1 - Start the WGUPS Routing Program")
    print("Choose 2 - Find package")
    print("Choose 3 - Quit")
    user_input = input("Enter your choice ( 1 or 2 or 3 ):")

    # Run the simulated WPUPS Routing Program
    if user_input == "1":
        print("Starting the WGUPS Routing Program...")
        # Populate hash table
        function.populate_hash_table()
        # Run simulations for all trucks.
        function.nearest_neighbor_algorithm(WGUPS_truck_1)
        function.nearest_neighbor_algorithm(WGUPS_truck_2)
        function.nearest_neighbor_algorithm(WGUPS_truck_3)

        # Display the total mileage for the route using the nearest neighbor algorithm.
        print("Using the nearest neighbor algorithm, the total mileage for the route is:")
        print(truck.WGUPS_truck_1.truck_total_mileage + truck.WGUPS_truck_2.truck_total_mileage + truck.WGUPS_truck_3.truck_total_mileage)
        print("---------------------------------------------------------------------------------------------")

        # Display the user interface to check the status of all packages or a single package.
        print("Choose 1 - Check the status of all packages:")
        print("Choose 2 - Check the status of a single package:")
        user_input = input("Enter your choice ( 1 or 2 ):\n")

        # Display all packages
        if user_input == "1":

            # Ask the user to input the time to check the status of all packages.
            time_input = input("\nPlease enter the time in 'HH:MM:SS' format:\n")
            (hours, minutes, seconds) = time_input.split(":")
            time_input = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
            function.display_all_packages(time_input)

        # Display a single package
        elif user_input == "2":

            # Ask the user to input the time to check the status of a single package.
            time_input = input("\nPlease enter the time in 'HH:MM:SS' format\n")
            (hours, minutes, seconds) = time_input.split(":")
            time_input = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

            # Ask the user to input the package number to check the status of a single package.
            package_ID = input("\nPlease enter the package number:\n")
            function.display_package(int(package_ID), time_input)
        else:
            print("Invalid choice. Please select a valid option ( 1 or 2 ).")
    elif user_input == "2":
        # Populate hash table
        function.populate_hash_table()
        package_input = input("\n Please enter the package number ( from 1 to 40 ):")
        function.find_package_using_package_ID(int(package_input))
    elif user_input == "3":
        print("Quitting the program.")

    else:
        print("Invalid choice. Please select a valid option ( 1 or 2 ).")
