from ParkingLotSystem import ParkingLot

def main():
    parking_lot = ParkingLot()
    while True:
        print("\n*** Parking Lot System ***")
        print("1. Park a Vehicle")
        print("2. Find Vehicle")
        print("3. Unpark Vehicle")
        print("4. Find Nearest Parking Spot")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_number = input("Enter Vehicle Number: ")
            print(parking_lot.assign_parking(vehicle_number))
        elif choice == '2':
            vehicle_number = input("Enter Vehicle Number: ")
            print(parking_lot.retrieve_parking_spot(vehicle_number))
        elif choice == '3':
            vehicle_number = input("Enter Vehicle Number: ")
            print(parking_lot.unpark_vehicle(vehicle_number))
        elif choice == '4':
            print(parking_lot.find_nearest_parking())
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
