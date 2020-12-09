from src import history

def main():
    file = input("Enter file name if the file in the same directory or the entire path :")
    dh = history.DriverHistory()
    dh.GetAverages(file)


if __name__ == "__main__":
    main()