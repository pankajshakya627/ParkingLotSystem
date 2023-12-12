# Parking Lot System

## Overview
This repository contains a Python-based terminal application for a Parking Lot System. The application simulates a parking lot with two levels, each capable of accommodating 20 vehicles. The system is designed with in-memory data structures and follows modular programming principles.

## Structure
The project comprises two main files:
- `ParkingLotSystem.py`: Contains the core logic of the Parking Lot System, including the classes and methods for parking management.
- `ExecuteParkingLotSystem.py`: Serves as the entry point of the application with the `main()` function, facilitating user interaction through a command-line interface.

## Features
- **Automatic Parking Assignment**: Assigns a parking spot to new vehicles.
- **Parking Spot Retrieval**: Retrieves the parking spot for a particular vehicle using its vehicle number.
- **Vehicle Unparking**: Allows for vehicles to be removed from their parking spot.
- **Nearest Parking Spot Retrieval**: Finds the nearest available parking spot, prioritizing recently vacated spots.

## Installation
Clone the repository and navigate to the directory:

```bash
git clone https://github.com/pankajshakya627/ParkingLotSystem.git
cd ParkingLotSystem

python ExecuteParkingLotSystem.py


```
## How it Works
- The application initializes a parking lot with two levels (A and B), each accommodating up to 20 vehicles.
- Users can interact with the system to park/unpark vehicles, retrieve vehicle and parking spot information, and find the nearest available parking spot.
