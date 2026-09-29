vehicles = []
#campus vehicle management system
#Developed using python
#This program allows users to manage vehicles, users, bookings, and trips in a campus environment.
def invalid_choice():
    print("Invalid choice. Please try again.")
    #--------------Vehicle Management----------------

def vehicle_management():
    while True:
        print("\n===== VEHICLE MANAGEMENT =====")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Search Vehicle")
        print("4. Delete Vehicle")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_id = input("Enter Vehicle ID: ")
            if vehicle_id == "":
                print("Vehicle ID cannot be empty.")
                continue
            vehicle_name = input("Enter Vehicle Name: ")
            vehicle_type = input("Enter Vehicle Type: ")
            driver = input("Enter Driver Name: ")

            vehicle = {
                "id": vehicle_id,
                "name": vehicle_name,
                "type": vehicle_type,
                "driver": driver
            }

            vehicles.append(vehicle)
            print("Vehicle added successfully!")

        elif choice == "2":
            if len(vehicles) == 0:
                print("No vehicles available.")
            else:
                print("\n--- Vehicle List ---")
                for vehicle in vehicles:
                    print(
                        vehicle["id"],
                        vehicle["name"],
                        vehicle["type"],
                        vehicle["driver"]
                    )

        elif choice == "3":
            search_id = input("Enter Vehicle ID to search: ")
            found = False

            for vehicle in vehicles:
                if vehicle["id"] == search_id:
                    print("Vehicle Found!")
                    print("Name:", vehicle["name"])
                    print("Type:", vehicle["type"])
                    print("Driver:", vehicle["driver"])
                    found = True

            if not found:
                print("Vehicle not found.")

        elif choice == "4":
            delete_id = input("Enter Vehicle ID to delete: ")

            for vehicle in vehicles:
                if vehicle["id"] == delete_id:
                    vehicles.remove(vehicle)
                    print("Vehicle deleted successfully!")
                    break
            else:
                print("Vehicle not found.")

        elif choice == "5":
            break

        else:
            invalid_choice()
users = []
#--------------User Management----------------
def user_management():
    while True:
        print("\n===== USER MANAGEMENT =====")
        print("1. Add User")
        print("2. View Users")
        print("3. Search User")
        print("4. Delete User")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            user_name = input("Enter User Name: ")
            user_email = input("Enter User Email: ")

            user = {
                "id": user_id,
                "name": user_name,
                "email": user_email
            }

            users.append(user)
            print("User added successfully!")

        elif choice == "2":
            user_management()
            if len(users) == 0:
                print("No users available.")
            else:
                print("\n--- User List ---")
                for user in users:
                    print(
                        user["id"],
                        user["name"],
                        user["email"]
                    )

        elif choice == "3":
            search_id = input("Enter User ID to search: ")
            found = False

            for user in users:
                if user["id"] == search_id:
                    print("User Found!")
                    print("Name:", user["name"])
                    print("Email:", user["email"])
                    found = True

            if not found:
                print("User not found.")

        elif choice == "4":
            delete_id = input("Enter User ID to delete: ")

            for user in users:
                if user["id"] == delete_id:
                    users.remove(user)
                    print("User deleted successfully!")
                    break
            else:
                print("User not found.")

        elif choice == "5":
            break

        else:
            invalid_choice()
    while True:
        print("\n===== USER MANAGEMENT =====")
        print("1. Add User")
        print("2. View Users")
        print("3. Search User")
        print("4. Delete User")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            user_name = input("Enter User Name: ")
            user_email = input("Enter User Email: ")

            user = {
                "id": user_id,
                "name": user_name,
                "email": user_email
            }

            users.append(user)
            print("User added successfully!")

        elif choice == "2":
            if len(users) == 0:
                print("No users available.")
            else:
                print("\n--- User List ---")
                for user in users:
                    print(
                        user["id"],
                        user["name"],
                        user["email"]
                    )

        elif choice == "3":
            search_id = input("Enter User ID to search: ")
            found = False

            for user in users:
                if user["id"] == search_id:
                    print("User Found!")
                    print("Name:", user["name"])
                    print("Email:", user["email"])
                    found = True

            if not found:
                print("User not found.")

        elif choice == "4":
            delete_id = input("Enter User ID to delete: ")

            for user in users:
                if user["id"] == delete_id:
                    users.remove(user)
                    print("User deleted successfully!")
                    break
            else:
                print("User not found.")

        elif choice == "5":
            break

        else:
            invalid_choice()
bookings = []
#--------------Booking Management----------------
def booking_management(): 
    while True: 
        print("\n===== BOOKING MANAGEMENT =====")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Search Booking")
        print("4. Delete Booking")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            booking_id = input("Enter Booking ID: ")
            user_id = input("Enter User ID: ")
            vehicle_id = input("Enter Vehicle ID: ")
            booking_date = input("Enter Booking Date (YYYY-MM-DD): ")

            booking = {
                "id": booking_id,
                "user_id": user_id,
                "vehicle_id": vehicle_id,
                "date": booking_date
            }

            bookings.append(booking)
            print("Booking added successfully!")

        elif choice == "2":
            if len(bookings) == 0:
                print("No bookings available.")
            else:
                print("\n--- Booking List ---")
                for booking in bookings:
                    print(
                        booking["id"],
                        booking["user_id"],
                        booking["vehicle_id"],
                        booking["date"]
                    )

        elif choice == "3":
            search_id = input("Enter Booking ID to search: ")
            found = False

            for booking in bookings:
                if booking["id"] == search_id:
                    print("Booking Found!")
                    print("User ID:", booking["user_id"])
                    print("Vehicle ID:", booking["vehicle_id"])
                    print("Date:", booking["date"])
                    found = True

            if not found:
                print("Booking not found.")

        elif choice == "4":
            delete_id = input("Enter Booking ID to delete: ")

            for booking in bookings:
                if booking["id"] == delete_id:
                    bookings.remove(booking)
                    print("Booking deleted successfully!")
                    break
            else:
                print("Booking not found.")

        elif choice == "5":
            break

        else:
            invalid_choice()
trips = []
#--------------Trip Management----------------
def trip_management():
    while True:
        print("\n===== TRIP MANAGEMENT =====")
        print("1. Add Trip")
        print("2. View Trips")
        print("3. Search Trip")
        print("4. Delete Trip")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            trip_id = input("Enter Trip ID: ")
            user_id = input("Enter User ID: ")
            vehicle_id = input("Enter Vehicle ID: ")
            trip_date = input("Enter Trip Date (YYYY-MM-DD): ")

            trip = {
                "id": trip_id,
                "user_id": user_id,
                "vehicle_id": vehicle_id,
                "date": trip_date
            }

            trips.append(trip)
            print("Trip added successfully!")

        elif choice == "2":
            if len(trips) == 0:
                print("No trips available.")
            else:
                print("\n--- Trip List ---")
                for trip in trips:
                    print(
                        trip["id"],
                        trip["user_id"],
                        trip["vehicle_id"],
                        trip["date"]
                    )

        elif choice == "3":
            search_id = input("Enter Trip ID to search: ")
            found = False

            for trip in trips:
                if trip["id"] == search_id:
                    print("Trip Found!")
                    print("User ID:", trip["user_id"])
                    print("Vehicle ID:", trip["vehicle_id"])
                    print("Date:", trip["date"])
                    found = True

            if not found:
                print("Trip not found.")

        elif choice == "4":
            delete_id = input("Enter Trip ID to delete: ")

            for trip in trips:
                if trip["id"] == delete_id:
                    trips.remove(trip)
                    print("Trip deleted successfully!")
                    break
            else:
                print("Trip not found.")

        elif choice == "5":
            break

        else:
            invalid_choice()
#reports
def reports():
  while True:
    print("\n===== REPORTS =====")
    print("1. Vehicle Report")
    print("2. User Report")
    print("3. Booking Report")
    print("4. Trip Report")
    print("5. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(vehicles) == 0:
            print("No vehicles available.")
        else:
            print("\n--- Vehicle Report ---")
            for vehicle in vehicles:
                print(
                    vehicle["id"],
                    vehicle["name"],
                    vehicle["type"],
                    vehicle["driver"]
                )

    elif choice == "2":
        if len(users) == 0:
            print("No users available.")
        else:
            print("\n--- User Report ---")
            for user in users:
                print(
                    user["id"],
                    user["name"],
                    user["email"]
                )

    elif choice == "3":
        if len(bookings) == 0:
            print("No bookings available.")
        else:
            print("\n--- Booking Report ---")
            for booking in bookings:
                print(
                    booking["id"],
                    booking["user_id"],
                    booking["vehicle_id"],
                    booking["date"]
                )

    elif choice == "4":
        if len(trips) == 0:
            print("No trips available.")
        else:
            print("\n--- Trip Report ---")
            for trip in trips:
                print(
                    trip["id"],
                    trip["user_id"],
                    trip["vehicle_id"],
                    trip["date"]
                )

    elif choice == "5":
        return

    else:
        invalid_choice()
while True:
    print("\n=====CAMPUS VEHICLE MANAGEMENT SYSTEM =====" )
    print("1.Vehicle MANAGEMENT")
    print("2.USER Management")
    print("3.Booking Managemment")
    print("4.Trip Management")
    print("5.reports")
    print("6.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        vehicle_management()
    elif choice == "2":
        user_management()
    elif choice == "3":
        booking_management()
    elif choice == "4":
        trip_management()
    elif choice == "5":
        reports()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        invalid_choice()