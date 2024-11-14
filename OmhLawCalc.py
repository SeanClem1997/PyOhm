'''Several changes been made to the program as of 11/14/2024r

1.Changes the lists to global variables(I'm aware global variables aren't preferred). I kept having issues with the indexes within the elements

2.Add the while loop flags to end the while loop collecting Resistor values

3.Added some breaks into the conditional flow

4.Fixed up some spcaes and formtating


Program is pretty much functional however still has some typos and format needs to be presentable



'''


resistorTotal = []
currentTotal = 0 #Changed into global vairable
voltageTotal = 0 #Changed into global vairable
ohmsLawVal = []
RT = 0 #Changed into global variable
VT = []

# First Function checks The values and does the equations if we have 2/3 values needed
def check_Value():
    while len(ohmsLawVal) == 2:  # Checking to see if we have 2/3 values, end the program and output the final value!
        if 'r' in ohmsLawVal and 'i' in ohmsLawVal:  # If we have I and R entered in, then use V=I*R 
            ohmV = currentTotal * RT  # Since these are in a list with only one number, we use index[0] to grab the first and only value.
            print(f"VT: {ohmV}")  # V=I*R 
            break
        elif 'i' in ohmsLawVal and 'v' in ohmsLawVal:
            ohmR = voltageTotal / currentTotal
            print(f"RT: {ohmR}")
            break
        elif 'v' in ohmsLawVal and 'r' in ohmsLawVal:
            ohmI = [voltageTotal /  RT]
            print(f"IT: {ohmI}")
            break
    #if len(ohmsLawVal) == 2:  # Have this here to print out RT. NEEDS TO BE OPTIMIZED
       #print(f"RT: {RT}")


def series_calc():
    #Added some global variables due to some isseus with lists(Aware that globals are not  prefered)
    global voltageTotal
    global currentTotal
    global RT
    seriesValue = input("--Please Enter Known Value-- \n[r] \n[i] \n[v] \nChoice: ")
    
    if seriesValue.lower() == 'r':
        rFlag = True #Added flag
        while rFlag == True: # while flag was true it kept going
            resistor = float(input(f"Resistor Value: "))
            resistorTotal.append(resistor)
            print(f"RT: {resistor}")
            
            stopFunc = input("Done: Y/N: ")
            if stopFunc.lower() == 'y':# When we choose yes for done we we stop loop at end
                ohmsLawVal.append('r')
                RT = sum(resistorTotal)
                print(f'RT: {RT}')
                resistorSeriesCounter = 0
                for r in resistorTotal:
                    resistorSeriesCounter += 1
                    print(f'R{resistorSeriesCounter}: {r}')
                    rFlag = False# Added end of flag to end switch statment
        
   

    if seriesValue.lower() == 'i':
        current = float(input("Please Enter I: "))
        currentTotal += current
        print(f"IT: {currentTotal}")
        ohmsLawVal.append('i')
        check_Value()

    # This is for Voltage
    
    elif seriesValue.lower() == 'v':
        voltage = float(input("Vt: "))
        voltageTotal += voltage
        print(f"VT {voltageTotal}")
        ohmsLawVal.append('v')
        check_Value()

print("Welcome To series Calculator")

while len(ohmsLawVal) < 2:  # NEEDS TO BE OPTIMIZED
    check_Value()
    series_calc()
