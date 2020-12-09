import re

class inFile:
    def LoadFile(self, file):
        file_handler = open(file,'r')
        drivers = []
        trips = {}
        # trips has the format {<name>:{'Trips':[[<start>,<end>,<distance>],[<start>,<end>,<distance>]...]}}

        driverline = re.compile('[@_!#$%^&*()<>?/\-\|}{~:\.\,0-9]')
        tripline = re.compile('[@_!#$%^&*()<>?/\|}{~\,]')
        '''
        A driver can be added at any point. But the driver in question has to be in the list for the trip to be valid. If not it throws an error
        If duplicate entries for drivers are detected, they are ignored 
        '''
        for num, line in enumerate(file_handler, 1):
            line = line.rstrip('\n')
                # only first name should be included. Any line with more than 1 whitespace (having a middle/last name will throw an error)
            if driverline.search(line) == None and re.findall(r'^Driver\s[a-zA-Z]*\S',line):
                currd = line.split(' ')
                if currd[1] not in drivers:
                    drivers.append(currd[1])
                    trips[currd[1]] = {'Trips': []}
                else:
                    print("Duplicate driver entry for {0}".format(currd[1]))

                #HAS to be in the format - Trip Lauren 12:01 13:16 42.0. Anything else will throw an error
            elif tripline.search(line) == None and re.findall(r'^Trip\s[a-zA-Z]*\s\d\d:\d\d\s\d\d:\d\d\s[0-9]*\.[0-9]*', line):
                currt = line.split(' ')
                if(currt[1] in drivers):
                    name = currt[1]        #CONTINUE FROM HERE
                    trip = [currt[2],currt[3],currt[4]]
                    trips[name]['Trips'].append(trip)

                else:
                    print("Invalid trip detected. Ignoring..")
                    continue
            else:
                print("Invalid entry in line {0}".format(num))
                continue

        # print(trips)

        return trips


if __name__ == '__main__':
    f = inFile()
    f.LoadFile('test2.txt')