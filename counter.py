def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    try : 
        fhand = open(file_name)
    except: 
        print("Please enter valid file name.")
        quit
    
    days = dict()

    for line in fhand :
        line = line.rstrip()
        if line.startswith("From:") :
            continue
        if line.startswith("From") :
            line =line.split()
            if line[2] not in days :
                days[line[2]] = 1
            else : 
                days[line[2]] = days[line[2]] + 1 

    print(days)      
            
        









## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
