# Question 1: City Infrastructure Management System

# Task 1: Vehicle Registration System
from termcolor import colored

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def list_details(self):
        print(colored(f"\nVehicle Registration Number:  {self.registration_number} \nVehicle Type: {self.type} \nVehicle Owner: {self.owner}", "light_yellow"))


vehicles = {}

def register_vehicle(reg_num, type, owner):
    if reg_num in vehicles:
        print("Vehicle Registration Number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"\nVehicle registration number {reg_num} is now registered.")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"\nVehicle registration number {reg_num}, is now updated with new vehicle owner.")
    else:
        print("Vehicle was not found.")

def list_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.list_details()

while True:
    action = input("\nEnter action (Register , Update, List, Exit) ").title()
    if action == "Exit":
        break

    try:
        if action == "Register":
            reg_num = input("Enter the vehicle registration number: ")
            type = input("Enter vehicle type: ").title()
            owner = input("Enter the name of the vehicle's owner: ").title()
            register_vehicle(reg_num, type, owner)
        elif action == "Update":
            reg_num = input("Enter the vehicle registration number: ")
            new_owner = input("Enter new vehicle owner's name: ").title()
            update_vehicle_owner(reg_num, new_owner)
        elif action == "List":
            list_all_vehicles()
    except Exception as e:
        print(f"An error occurred: {e}")

print("\nVehicle Registration System closed.\n")