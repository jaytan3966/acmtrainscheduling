def inputSched():
    working = True
    f = open("trainSchedule.txt", "a")
    while working:
        trainNum = input("What is the train number? ")
        sameTrain = True
        while sameTrain:
            station = input("What is the train station? ")
            time = input("What is the time? ")
            query = input(f"Train number: {trainNum} \nStation: {station} \nTime: {time} \nIs this information correct? Type Y for yes, N for no. ")
            if query == "Y":
                f.write(trainNum + ", " + station + ", " + time + "\n")
            else:
                print("Going back to start. ")
                break
            cont = input(f"Would you like to continue inputting data for train {trainNum}?  Type Y for yes, N for no. ")
            if cont == "Y":
                continue
            else:
                cont = input("Would you like to continue inputting data? Type Y for yes, N for no. ")
                if cont == "Y":
                    sameTrain = False
                    continue
                else:
                    working = False
                    break

def checkSched():
    f = open("trainschedule.txt")
    read = f.readlines()
    print(read)
    while True:
        found = False
        trainNum = input("Enter the train number you are looking for (Type Q to quit): ")
        if trainNum == "Q":
            break
        for line in read:
            if line.startswith(trainNum):
                found = True
                print(line)
        if found == False:
            print("Enter a valid train number! ")

def runProgram():
    while True:
        user = input("What would you like to do today? Type I to input train schedules, C to check schedules, Q to quit: ")
        if user == "I":
            inputSched()
        elif user == "C":
            checkSched()
        elif user == "Q":
            break
        else:
            print("Enter a valid command! ")

