from src import inFile
from datetime import datetime

class DriverHistory:
    def Averages(self, input):
        tripsGenerator = inFile.inFile()
        try:
            tripList = tripsGenerator.LoadFile(input)
        except FileNotFoundError as e:
            print(e.args[1])
            exit()
        datetimeFormat = '%H:%M'
        avgs = []

        for driver in tripList.keys():
            totalTime = 0
            totalDistance = 0

            for trip in tripList[driver]['Trips']:
                start = trip[0]
                end = trip[1]
                distance = float(trip[2])
                try:
                    time = ((datetime.strptime(end, datetimeFormat) - datetime.strptime(start, datetimeFormat)).total_seconds())/3600
                except ValueError as e:
                    print("Invalid time(s) for driver {0}".format(driver))
                    continue
                mph = 0
                if time > 0:
                    mph = distance/time
                else:
                    print("Time taken to complete trip by {0} is invalid. Trip discarded".format(driver))
                    continue

                if mph <= 100 and mph >=5:
                    totalDistance += distance
                    totalTime += time
                else:
                    print("MPH is less than 5 or more than 100 for trip by {0}. Trip discarded".format(driver))
                    continue
            avg = 0
            if totalTime > 0:
                avg = totalDistance/totalTime
            avgs.append([driver, int(round(totalDistance)), int(round(avg))])

        return avgs

    def GetAverages(self, file):
        avgList = self.Averages(file)
        avgList.sort(reverse=True, key=lambda x: x[1])

        f = open("driverhistory.txt", "w")
        for name, miles, time in avgList:
            if miles == 0:
                f.write("{0}: {1} miles".format(name,miles)+"\n")
            else:
                f.write("{0}: {1} miles @ {2} mph".format(name,miles,time)+"\n")

        # print('\n')
        # for name, miles, time in avgList:
        #     if miles == 0:
        #         print("{0}: {1} miles".format(name,miles))
        #     else:
        #         print("{0}: {1} miles @ {2} mph".format(name,miles,time))
        # return

if __name__ == '__main__':
    f = DriverHistory()
    f.Averages('test2.txt')