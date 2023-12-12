# class ParkingLot:
#     def __init__(self):
#         self.parking_lot = {'A': [None] * 20, 'B': [None] * 20}
#         self.vehicle_spot_map = {}
#         self.available_spots = {level: list(range(20)) for level in ['A', 'B']}

#     def _get_spot_index(self, level, spot_number):
#         return self.available_spots[level].index(spot_number)

#     def assign_parking(self, vehicle_number):
#         for level, spots in self.available_spots.items():
#             if spots:
#                 spot = spots.pop(0)
#                 self.parking_lot[level][spot] = vehicle_number
#                 self.vehicle_spot_map[vehicle_number] = (level, spot)
#                 return {'level': level, 'spot': spot + 1}
#         return "Parking is full"

#     def retrieve_parking_spot(self, vehicle_number):
#         return self.vehicle_spot_map.get(vehicle_number, "Vehicle not found")

#     def unpark_vehicle(self, vehicle_number):
#         if vehicle_number in self.vehicle_spot_map:
#             level, spot = self.vehicle_spot_map.pop(vehicle_number)
#             self.parking_lot[level][spot] = None
#             self.available_spots[level].insert(self._get_spot_index(level, spot), spot)
#             return f"Vehicle {vehicle_number} has been unparked"
#         return "Vehicle not found"

#     def find_nearest_parking(self):
#         for level, spots in self.available_spots.items():
#             if spots:
#                 return {'level': level, 'spot': spots[0] + 1}
#         return "Parking is full"
class ParkingLot:
    def __init__(self):
        self.parking_lot = {'A': [None] * 20, 'B': [None] * 20}
        self.vehicle_spot_map = {}
        # Adjusting spot numbers to start from 1 for user-friendliness
        self.available_spots = {level: list(range(1, 21)) for level in ['A', 'B']}

    def assign_parking(self, vehicle_number):
        for level, spots in self.available_spots.items():
            if spots:
                spot = spots.pop(0)
                self.parking_lot[level][spot - 1] = vehicle_number
                self.vehicle_spot_map[vehicle_number] = (level, spot)
                return {'level': level, 'spot': spot}
        return "Parking is full"

    def unpark_vehicle(self, vehicle_number):
        if vehicle_number in self.vehicle_spot_map:
            level, spot = self.vehicle_spot_map.pop(vehicle_number)
            self.parking_lot[level][spot - 1] = None
            # Inserting the spot back at the right position
            self.available_spots[level].insert(spot - 1, spot)
            return f"Vehicle {vehicle_number} has been unparked"
        return "Vehicle not found"

    def find_nearest_parking(self):
        for level, spots in self.available_spots.items():
            if spots:
                return {'level': level, 'spot': spots[0] + 1}
        return "Parking is full"
    
    def retrieve_parking_spot(self, vehicle_number):
        return self.vehicle_spot_map.get(vehicle_number, "Vehicle not found")


