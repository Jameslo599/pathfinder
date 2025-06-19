import csv

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
        # self.loading_time
        # self.delivery_time

    def __str__(self):
        return (
            f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, '
            f'Delivery Deadline: {self.delivery_deadline}, Weight KILO: {self.weight_kilo}, Special Notes: {self.special_notes}, Loading Time:, Delivery Time:')

    def __repr__(self):
        return (f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, '
                f'Delivery Deadline: {self.delivery_deadline}, Weight KILO: {self.weight_kilo}, Special Notes: {self.special_notes}, Loading Time:, Delivery Time:')

class HashTable:
    def __init__(self):
        self.table = [[0]*10 for _ in range(10)]

    def __str__(self):
        return (
            f'Package ID: {self.table}')

    def __repr__(self):
        return (
            f'Package ID: {self.table}')

    def insert(self, package):
        primary = package.package_id // 10
        secondary = package.package_id % 10
        self.table[primary][secondary-1] = package

    def lookup(self, package_id):
        primary = package_id // 10
        secondary = package_id % 10
        return self.table[primary][secondary-1]

hash_table = HashTable()

with open('simulation_data/package_file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        hash_table.insert(package)

print(hash_table.lookup(23))
