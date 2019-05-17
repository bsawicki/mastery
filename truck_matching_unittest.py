import os
import unittest
from truck_matching import TruckMatcher

class TestTruckMatcher(unittest.TestCase):
	def setUp(self):
		self.matcher = TruckMatcher("test_input/sample_truck_file.csv", "test_input/sample_distance_file.csv")

	# Right now this only tests what is done on set up, could re-parse different data
	def testParseTrucks(self):
		self.assertEqual(self.matcher.truck_dict["Memphis, TN"]["Chicago, IL"]["V"], ["001", "005"])
		self.assertEqual(self.matcher.truck_dict["St. Louis, MO"]["Las Vegas, NV"]["VR"], ["002"])
		self.assertEqual(self.matcher.truck_dict["Bismark, ND"]["Hamburg, PA"]["VR"], ["003"])
		self.assertEqual(self.matcher.truck_dict["Nashville, TN"]["Skokie, IL"]["V"], ["004"])
			
	# Right now this only tests what is done on set up, could re-parse different data
	def testParseDistances(self):
		self.assertEqual(self.matcher.distance_dict["Memphis, TN"]["Chicago, IL"], "531")
		self.assertEqual(self.matcher.distance_dict["St. Louis, MO"]["Las Vegas, NV"], "1597")

	# TODO: input/output directory structure could be cleaned up
	def testMatchLoads(self):
		for input_file in os.listdir("test_input/loads"):
			if input_file.endswith(".csv"):
				self.matcher.match_loads("test_input/loads/" + input_file)
				output_file_name = input_file + ".output"
				output = open("test_input/loads/" + output_file_name, "r")
				content = output.read()
				good_output = open("test_output/" + output_file_name)
				good_content = good_output.read()
				self.assertEqual(content, good_content)
				output.close()
				good_output.close()
		
if __name__ == '__main':
	unittest.main()
