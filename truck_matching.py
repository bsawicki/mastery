import csv
import sys
from collections import defaultdict

truck_dict = defaultdict(lambda: defaultdict(dict))
distance_dict = defaultdict(defaultdict)

# Parse the CSV file for trucks provided on the command line into truck_dict
def parse_trucks(truck_csv):
	with open(truck_csv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row["Equipment"] in truck_dict[row["Origin"]][row["Destination"]]:
				truck_dict[row["Origin"]][row["Destination"]][row["Equipment"]].append(row["Truck"])
			else:
				truck_dict[row["Origin"]][row["Destination"]][row["Equipment"]] = [row["Truck"]]

# Parse the CSV file for distances provided on the command line into distance_dict
# We assume each origin-destination combination is unique
def parse_distances(distance_csv):
	with open(distance_csv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			distance_dict[row["Origin"]][row["Destination"]] = row["Distance"]

# Match loads from the given CSV file with known trucks and print the match in the format "Load,[Truck(s)],Distance"
def match_loads(load_csv):
	with open(load_csv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			try:
				trucks = truck_dict[row["Origin"]][row["Destination"]][row["Equipment"]]
			except KeyError:
				# This could be improved by saying whether a truck on the given route or the given equipment was not found
				trucks = ["Not Found"]
			try:
				distance = distance_dict[row["Origin"]][row["Destination"]]
			except KeyError:
				distance = "Not Found"
			print(row["Load"] + "," + str(trucks) + "," + distance)

# Read command line args
truck_file = sys.argv[1]
distance_file = sys.argv[2]
load_file = sys.argv[3]

# Parse CSVs and match loads
parse_trucks(truck_file)
parse_distances(distance_file)
match_loads(load_file)
