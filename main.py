# James Lo
# Student ID: 001305175
# C950 WGUPS Routing Program
# Step C: original program with comments
from package import Package
from hashtable import HashTable
from datetime import datetime, time, timedelta
import math

# Initialize hash table
hash_table = HashTable()
# Read package csv data
with open('simulation_data/package_file.csv', 'r') as f:
    lines = f.readlines()
# Take each line of package data and create a new instance of Package with every data field then insert into hash table
for line in lines[1:]:
    row = line.strip().split(',')
    package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    hash_table.insert(package)
# Mark delayed packages
hash_table.mark_delayed([6, 25, 28, 32])

# Distance Data
addresses = {}
distances = []
# Read distance csv data
with open('simulation_data/distance_table.csv', 'r') as f:
    lines = f.readlines()
# CI Prof. Amy Antonucci said in C950 PA Plan Step 2 that a dictionary for mapping string addresses to location indexes is acceptable
index = 0
for line in lines:
    row = line.strip().split(',')
    # Map each address to the running index count
    addresses[row[0]] = index
    index+=1
    # Add the distance values to the list of lists
    distances.append(row[1:])

# Use the index of current location and destination to obtain the distance
def find_distance(curr, dest):
    primary = addresses[curr]
    secondary = addresses[dest]
    if primary >= secondary:
        return float(distances[primary][secondary])
    else:
        return float(distances[secondary][primary])

# Initialize trucks holding a combined 40 packages with maximum 16 packages in a single truck
truck1 = []
truck2 = []
truck3 = []
# Manually sort packages into three sets which are used to load each truck
set1 = {1, 4, 7, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 37, 39}
set2 = {3, 5, 6, 9, 10, 18, 22, 24, 25, 26, 28, 31, 32, 36, 38, 40}
set3 = {2, 11, 12, 17, 23, 27, 33, 35}
for packages in hash_table.table:
    for package in packages:
        if package.package_id in set1:
            package.loading_time = datetime.combine(datetime.today(), time(8, 0))
            truck1.append(package)
        elif package.package_id in set2:
            package.loading_time = datetime.combine(datetime.today(), time(9, 5))
            truck2.append(package)
        else:
            truck3.append(package)

# Execute deliveries with a single truck at specified start time
def delivery(truck, start_time):
    # mark status in progress
    for package in truck:
        package.delivery_status = "En Route"
    # current location
    truck_address = "Hub"
    # 0.3 miles per minute
    truck_speed = 18 / 60
    total_miles = 0
    # continue while there are still undelivered packages
    while len(truck) > 0:
        current_package = None
        shortest_distance = float("inf")
        # iterate through packages to find shortest next delivery
        for package in truck:
            distance = find_distance(truck_address, package.address)
            if distance < shortest_distance:
                shortest_distance = distance
                current_package = package
        truck_address = current_package.address
        # calculate delivery time using math.ceil to provide a conservative time estimation
        total_miles+=shortest_distance
        delivery_time = timedelta(minutes=math.ceil(total_miles / truck_speed))
        # update hash table with package delivery, loading times and delivery status
        package = hash_table.lookup(current_package.package_id)
        package.loading_time = start_time.time().strftime("%H:%M")
        package.delivery_time = (delivery_time + start_time).time().strftime("%H:%M")
        package.delivery_status = "Delivered"
        truck.remove(current_package)

    # calculate return distance
    total_miles+=find_distance(truck_address, "Hub")
    delivery_time = timedelta(minutes=math.ceil(total_miles / truck_speed))
    total_time = delivery_time + start_time
    return {"miles":round(total_miles, 2), "end_hour":total_time.time().hour, "end_minute":total_time.time().minute}

truck1_end = delivery(truck1, datetime.combine(datetime.today(), time(8, 0)))
truck2_end = delivery(truck2, datetime.combine(datetime.today(), time(9, 5)))
truck3_end = delivery(truck3, datetime.combine(datetime.today(), time(truck1_end["end_hour"], truck1_end["end_minute"])))
# calculate total miles
# print(f'{round(truck1_end["miles"] + truck2_end["miles"] + truck3_end["miles"], 2)} total miles')

user_hour = 10
user_minute = 29
hash_table.table[0][0].update_status(time(8, 38))
print(hash_table.table[0][0])