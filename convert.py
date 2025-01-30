#!/usr/bin/python3 

import nbtlib

# Path to the .dat file
file_path = "/Users/fiveqoffice/Downloads/playerdata/31cd4bf3-454a-4818-ac64-9e64c2b68216.dat"

# Open the .dat file
data = nbtlib.load(file_path)

# Navigate to the LastDeathLocation tag
try:
    last_death_location = data["Player"]["LastDeathLocation"]
    print("LastDeathLocation:", last_death_location)
except KeyError:
    print("LastDeathLocation not found in the file.")
