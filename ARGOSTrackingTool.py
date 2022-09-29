#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Joshua Meza-Fidalgo (jem150@duke.edu)
# Date:   Fall 2022
#----

#Creating a variable pointing to the data
file_name = 'data/raw/sara.txt'

#Creating a file object from the file name
file_object = open(file = file_name, mode = 'r')

#Reading file contents into a list
line_list = file_object.readlines()

#Close file for safety
file_object.close()

#Extracting one data line into a variable
lineString = line_list[101]

#Spliting lineString into a list of items
lineData = lineString.split()

# Assign variables to each item on the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[5]       # Observation Location Class
obs_lat = lineData[6]     # Observation Latitude
obs_lon = lineData[7]     # Observation Longitude

# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

