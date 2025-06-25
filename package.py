from datetime import datetime, time

class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, notes):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        self.delivery_deadline = deadline
        self.weight_kilo = weight
        self.special_notes = notes
        self.loading_time = None
        self.delivery_time = None
        self.delivery_status = "At Hub"
        self.truck_number = None

    def update_status(self, input_time):
        # Mark delayed packages
        delayed_packages = {6, 25, 28, 32}
        if self.package_id in delayed_packages and input_time < time(9, 5):
            self.delivery_status = "Delayed"
            return

        parsed_loading = datetime.strptime(self.loading_time, "%H:%M").time()
        parsed_delivery = datetime.strptime(self.delivery_time, "%H:%M").time()
        if self.package_id == 9 and input_time < time(10, 20):
            self.address = "300 State St"
            self.zip = "84103"
        if input_time < parsed_loading:
            self.delivery_status = "At Hub"
        elif input_time < parsed_delivery:
            self.delivery_status = "En Route"
        else:
            self.delivery_status = "Delivered"

    def __str__(self):
        return (
            f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, '
            f'Delivery Deadline: {self.delivery_deadline}, Weight KILO: {self.weight_kilo}, Special Notes: {self.special_notes}, Loading Time: {self.loading_time}, Delivery Time:{self.delivery_time}, Delivery Status:{self.delivery_status}, Truck Number:{self.truck_number}')

    def __repr__(self):
        return (f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, '
                f'Delivery Deadline: {self.delivery_deadline}, Weight KILO: {self.weight_kilo}, Special Notes: {self.special_notes}, Loading Time: {self.loading_time}, Delivery Time:{self.delivery_time}, Delivery Status:{self.delivery_status}, Truck Number:{self.truck_number}')