# Toll Gate Queue Manager
import os


class Vehicle:
    def __init__(self, name, vehicle_type, brand):
        self.name = name
        self.vehicle_type = vehicle_type
        self.brand = brand

    def __str__(self) -> str:
        return self.name


class VehicleNode:
    def __init__(self, vehicle) -> None:
        self.vehicle = vehicle
        self.next_vehicle = None


class TollGate:
    def __init__(self):
        self.toll_queue = None
        self.toll_rear = None
        self.toll_front = None
        self.toll_queue_count = 0

    def is_toll_empty(self):
        return self.toll_queue_count == 0
    
    def enqueue_vehicle(self, vehicle):
        new_vehicle = VehicleNode(vehicle)
        if self.is_toll_empty():
            self.toll_queue = new_vehicle
            self.toll_front = new_vehicle
            self.toll_rear = new_vehicle
            self.toll_queue_count += 1
            return
        
        current_vehicle = self.toll_queue
        while current_vehicle.next_vehicle:
            current_vehicle = current_vehicle.next_vehicle

        current_vehicle.next_vehicle = new_vehicle
        self.toll_rear = new_vehicle
        self.toll_queue_count += 1

    def dequeue_vehicle(self):
        if self.is_toll_empty():
            print("Log: Toll Gate is empty")
            return
        
        dequeued_vehicle = self.get_toll_front()

        self.toll_queue = self.toll_queue.next_vehicle
        self.toll_front = self.toll_queue
        self.toll_queue_count -= 1

        return dequeued_vehicle

    def get_toll_front(self):
        return self.toll_front.vehicle
    
    def get_toll_rear(self):
        return self.toll_rear.vehicle
    
    def get_length_queue(self):
        return self.toll_queue_count
    
    def show_toll_queue(self):
        if self.is_toll_empty():
            print("Log: Toll is empty")
            return
        
        current_vehicle = self.toll_queue
        while current_vehicle.next_vehicle:
            print(current_vehicle.vehicle, end="->")
            current_vehicle = current_vehicle.next_vehicle

        print(current_vehicle.vehicle)


def clr_terminal():
    os.system('cls')

def main():
    operations = ["Add Vehicle to Toll Queue", "Remove Vehicle from Toll Queue", "Show the Front of the Queue", "Show the Last of the Queue", "Show the number of Vehicles inside the Toll Queue", "Quit"]
    running = True
    toll_gate_manager = TollGate()

    while running:
        print("=============== Toll Gate Manager ===============")
        print("Toll Gate Queue:")
        toll_gate_manager.show_toll_queue()

        print("============")
        for num, operation in enumerate(operations, start=1):
            print(f"{num}. {operation}")
        print("============")

        try:
            selected_operation = int(input("Enter a the Number: "))
        except ValueError:
            print("Log: Input must be a Number")

            input("\nPress Enter to continue")

            clr_terminal()
            continue
            
        if selected_operation > 6 or selected_operation < 1:
            print("Log: Number must be 1 - 6")

            input("\nPress Enter to continue")

            clr_terminal()
            continue
            
        if selected_operation == 1:
            vehicle_type = input("Enter the vehicle type (e.g Sedan): ")
            brand = input("Enter the brand of the Vehicle: ")
            
            vehicle = Vehicle(f"Vehicle{toll_gate_manager.toll_queue_count+1} ({brand} - {vehicle_type})", vehicle_type, brand)
            
            toll_gate_manager.enqueue_vehicle(vehicle)
            
            print(f"Log: {vehicle.name} is enqueued")

            input("\nPress Enter to continue")
            
        elif selected_operation == 2:
            print(f"{toll_gate_manager.dequeue_vehicle()} is dequeued from the Toll Queue")

            input("\nPress Enter to continue")

        elif selected_operation == 3:
            print(f"Front of the Toll Queue: {toll_gate_manager.get_toll_front()}")

            input("Press Enter to continue")

        elif selected_operation == 4:
            print(f"Last of the Toll Queue: {toll_gate_manager.get_toll_rear()}")

            input("\nPress Enter to continue")

        elif selected_operation == 5:
            print(f"Number of Vehicles inside the Toll Queue: {toll_gate_manager.get_length_queue()}")

            input("\nPress Enter to continue")

        elif selected_operation == 6:
            running = False
            
        clr_terminal()


if __name__ == "__main__":
    main()