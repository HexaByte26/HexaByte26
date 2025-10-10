# Toll Gate Queue Manager
class Vehicle:
    def __init__(self, name, vehicle_type, brand):
        self.name = name
        self.vehicle_type = vehicle_type
        self.brand = brand


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

        self.toll_queue = self.toll_queue.next_vehicle
        self.toll_front = self.toll_queue
        self.toll_queue_count -= 1

    def get_toll_front(self):
        return self.toll_front
    
    def get_toll_rear(self):
        return self.toll_rear
    
    def show_toll_queue(self):
        if self.is_toll_empty():
            print("Log: Toll is empty")
            return
        
        current_vehicle = self.toll_queue
        while current_vehicle.next_vehicle:
            print(current_vehicle.vehicle, end="->")
            current_vehicle = current_vehicle.next_vehicle

        print(current_vehicle.vehicle)
        print(f"First Vehicle of Toll Queue: {self.get_toll_front()}\nDetails:\nName: {self.get_toll_front().vehicle.name}\nVehicle Type: {self.get_toll_front().vehicle.vehicle_type}\nBrand: {self.get_toll_front().vehicle.brand}")
        print(f"Last Vehicle of Toll Queue: {self.get_toll_rear()}\nDetails:\nName: {self.get_toll_rear().vehicle.name}\nVehicle Type: {self.get_toll_rear().vehicle.vehicle_type}\nBrand: {self.get_toll_rear().vehicle.brand}")


def main():
    operations = ["Add Vehicle to Toll Queue", "Remove Vehicle from Toll Queue", "Show the Queue of the Toll", "Quit"]
    running = False
    toll_gate_manager = TollGate()

    while running:
        print("=============== Toll Gate Manager ===============")
        print("Toll Gate Queue:")
        toll_gate_manager.show_toll_queue()

        for num, operation in enumerate(operations, start=1):
            print(f"{num}. {operation}")


if __name__ == "__main__":
    main()