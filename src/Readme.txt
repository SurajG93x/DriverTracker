################################################################################################READ-ME################################################################################################

DRIVING HISTORY TRACKER
The following program takes in an input file consisting of Driver(s) and their trips and returns a list of total distance driven by each driver and their average MPH across the trips sorted in descending order.
It creates a file named 'driverhistory' onto which this output is written.

Program Structure:
The program consists of three python files classified by functionality
Apart from one main, one of the files reads the input from the file and returns a list of valid trips.
The other file calculates the average speed and total distance based on this list and writes the result to the output file.

Assumptions:
1. The drivers never drive past midnight.
2. Times are given in the following format HH:MM.
3. Hypens are included among the special characters that aren't allowed in names.
4. A driver must have been registered before any trip can be added. For example, if a trip is added on line 5 but the driver is registered on line 8, the trip is ignored.
5. Middle and Last CAN be included when adding drivers but only their first name is registered.
6. The following trips are only checked/matched based on their first names.
7. Any Trip commands than include middle/last names or spaces in their names are ignored.
8. There are only 2 valid commands: Trip or Driver. Each line in the input file MUST start with either of these commands.
9. The driver command MUST follow this following syntax: Driver <name>
10. The trip command MUST follow this following syntax: Trip <name> <starttime> <endtime> <distancedriven>
11. Distance driven can ONLY include upto ONE decimal point. And following decimal points will cause the line to be ignored.
12. Any trips that have an average speed of less than 5 mph or greater than 100 mph will be ignored.
13. Any trips that involve unregistered drivers will NOT be a part of the end output.

I. main.py
The main file that needs to be run
Asks the user to input the file name. The input MUST also contain the extension for the file.
If the file is in the same folder as the project (src), just the file name would suffice. If not, the entire path is required.

II. inFile.py:
The primary point of parsing the file to generate list(s) of driver(s) and their respective trips.
Has a method named LoadFile() that takes in a file name as input. Has a list drivers and a dictionary trips.
Parses through each line in the file and appends new drivers found with the command Driver to the drivers list.
Drivers can be added at any point within the file.
It will ignore any duplicate occurences of drivers. Any special characters or numbers within the name of the driver will also be ignored. These include @_!#$%^&*()<>?/\-\|}{~:.,0-9.
It will create a dictionary of trips based on the drivers list. For each driver(key), a list of "Trips" is added as a value.
It follows the format {<name>:{'Trips':[[<start>,<end>,<distance>],[<start>,<end>,<distance>]...]}}
If a driver that is not in the list is found in the trip, the entry will be ignored.
returns only the dictionary of the trips.

III. history.py
This class generates the averages and total distances covered per driver.
Has 2 methods. Firstly, the method Averages() calls the above method LoadFile() and receives the trips dictionary from the above method.
It then parses through each entry calculating the total distance covered per driver and their average speed in the format [<Name>, <TotalDistance>, <AverageSpeed>]
It ignores any zero divisions or invalid timestamps.
Then calls the second method GetAverages() that is responsible for sorting this list of triples based on the TotalDistance in descending order.
It then generates the string in 2 ways. On regular speed and distance, the format is <Name>: <TotalDistance> miles @ <AverageSpeed> mph
OR if the total distance travelled is zero, the format is <Name>: 0 miles. In case of zero distance, the names are printed in the order they are received.

The result is written onto a file named driverhistory.txt. For maintaining simplicity, any subsequent runs will overwrite the same output file.
To change the output to directly print the result, uncomment the piece of code while commenting the part that writes onto the file.

IV. My Thoughts:
I chose to let the user decide the extension of the input file to maintain ease of access.
The extensions can be check for added automatically is needed later on.
I created 3 separate classes classified by functionality and scalability. The major driving force behind this approach is to keep the entire system scalable for future modifications.
Registering drivers before creating any trips for them makes more sense.

This also scales well into the future if/when we want to add more functionality to it. Say, more than 2 commands for example - like deleting a driver.
I used Regular expressions to parse through the files. Using regex made the most sense here since we are looking for a particular format.
This helps keep a consistent format going forward.
While a name could contain hypens, I chose to add it to the list of special characters to maintain simplicity.
This can be changed, however, by removing it from the re.compile for drivers and adding to the pattern for trips.

A dictionary keeping track of all the trips based on each driver is the easiest way in terms of scalability and future optimizations.
Say, we decided to add a new functionality to unregister or remove drivers, a dictionary provides an easy access (by the name) to get rid of all the entries pertaining to that dirver.
This also helps with encapsulating relevant information (trips, in this context) to easily access them in the future.

Calculating the average speed and total distance was a rather easy approach thanks to the dictionaries.
There have been checks in place to ensure the timestamps are valid.
A running sum for total distance and times are kept track of for all the drivers.
The initial averages for each trips are calculated to check if its valid to be added to the running total(s).
While calculating the averages directly and adding them together later makes more sense than calculating the averages twice (once for each trip and again for the total),
the former makes more sense considering that we also need to keep track of the total distance travelled.
While this might have required more memory, this is the better option in terms of scalability.

Finally, I decided to print the final output in the required format(s) is a different method again to keep the system open to changes and scalability.


##################################################################################################END##################################################################################################