# Step A: hash table with insertion function
class HashTable:
    def __init__(self):
        self.table = [[0]*10 for _ in range(4)]

    def insert(self, package):
        primary = (package.package_id - 1) // 10
        secondary = package.package_id % 10
        self.table[primary][secondary-1] = package

    # Step B: lookup function
    def lookup(self, package_id):
        primary = (package_id - 1) // 10
        secondary = package_id % 10
        return self.table[primary][secondary-1]

    def mark_delayed(self, package_ids):
        for id in package_ids:
            package = self.lookup(id)
            package.delivery_status = "Delayed"

    def __str__(self):
        return (
            f'Package ID: {self.table}')

    def __repr__(self):
        return (
            f'Package ID: {self.table}')