import csv
import sys
from collections import defaultdict

# The structure of this class assumes truck routes and distances will be static for the lifetime of the class, while loads might vary.
# This class also assumes input is properly formatted.
class TruckMatcher:
	# Parse the CSV file for trucks provided on the command line into truck_dict
	def parse_trucks(self, truck_file):
		self.truck_dict = defaultdict(lambda: defaultdict(dict))
		with open(truck_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if row["Equipment"] in self.truck_dict[row["Origin"]][row["Destination"]]:
					self.truck_dict[row["Origin"]][row["Destination"]][row["Equipment"]].append(row["Truck"])
				else:
					self.truck_dict[row["Origin"]][row["Destination"]][row["Equipment"]] = [row["Truck"]]

	# Parse the CSV file for distances provided on the command line into distance_dict
	# We assume each origin-destination combination is unique
	def parse_distances(self, distance_file):
		self.distance_dict = defaultdict(defaultdict)
		with open(distance_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.distance_dict[row["Origin"]][row["Destination"]] = row["Distance"]

	# Match loads from the given CSV file with known trucks and print the match in the format "Load,[Truck(s)],Distance"
	# Right now this outputs as a file and to the command line, we could return the values from the function if we wanted
	def match_loads(self, load_file):
		with open(load_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			# Open a file to output the results to and trucate it
			output_file = load_file + ".output"
			writer = open(output_file, "a")
			writer.truncate(0)
			for row in reader:
				try:
					trucks = self.truck_dict[row["Origin"]][row["Destination"]][row["Equipment"]]
				except KeyError:
					# This could be improved by saying whether a truck on the given route or the given equipment was not found
					trucks = ["Not Found"]
				try:
					distance = self.distance_dict[row["Origin"]][row["Destination"]]
				except KeyError:
					distance = "Not Found"
				result = row["Load"] + "," + str(trucks) + "," + distance
				print(result)
				writer.write(result + "\n")
			writer.close()

	def __init__(self, truck_file, distance_file):
		self.parse_trucks(truck_file)
		self.parse_distances(distance_file)

if __name__ == "__main__":
	# Read command line arguments
	truck_file = sys.argv[1]
	distance_file = sys.argv[2]
	load_file = sys.argv[3]

	# Create a matcher and try one load file
	truck_matcher = TruckMatcher(truck_file, distance_file)
	truck_matcher.match_loads(load_file)
