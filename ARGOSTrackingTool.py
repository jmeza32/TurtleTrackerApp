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
lineString = file_object.readline()

#Extracting one data line into a variable
while lineString !="":
    
    #Check to see if the lineString is a data line
    if lineString[0] in ('#','u'):  #Could also use "if lineString[0] == "#" or lineString[0] == 'u'"
        lineString = file_object.readline()
        continue

    #Spliting lineString into a list of items
    lineData = lineString.split()

    # Assign variables to each item on the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude

    # Print information to the use
    print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
    
    #Move to the next line in the file
    lineString = file_object.readline()


#Close file for safety
file_object.close()
