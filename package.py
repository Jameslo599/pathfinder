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

    def update_status(self, input_time):
        parsed_time = datetime.strptime(self.delivery_time, "%H:%M").time()
        if input_time < time(8, 0):
            self.delivery_status = "At Hub"
        elif input_time < parsed_time:
            self.delivery_status = "En Route"
        else:
            self.delivery_status = "Delivered"

    def __str__(self):
        return (
            f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, '
            f'Delivery Deadline: {self.delivery_deadline}, Weight KILO: {self.weight_kilo}, Special Notes: {self.special_notes}, Loading Time: {self.loading_time}, Delivery Time:{self.delivery_time}, Delivery Status:{self.delivery_status}')

    def __repr__(self):
        return (f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, '
                f'Delivery Deadline: {self.delivery_deadline}, Weight KILO: {self.weight_kilo}, Special Notes: {self.special_notes}, Loading Time: {self.loading_time}, Delivery Time:{self.delivery_time}, Delivery Status:{self.delivery_status}')