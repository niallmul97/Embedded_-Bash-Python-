#!bin/usr/python3

#Write the complete python program that allows a user choose whether
#they want to calculate voltage, current or resistance. Call the class Digital.

#Create necessary setter and getter methods and private member variables called res, volt and curr.
#Allow user to repeatedly run the program until they decide to exit.

#Digital class which contains the getters, setters and private member variables
class Digital:

    def __init__(self, voltage, current, resistance):
        self.__volt = voltage
        self.__curr = current
        self.__res = resistance

    def setVoltage(self, voltage):
        self.__volt = voltage

    def getVoltage(self):
        return self.__volt

    def setCurrent(self, current):
        self.__curr = current

    def getCurrent(self):
        return self.__curr

    def setResistance(self, resistance):
        self.__res = resistance

    def getResistance(self):
        return self.__res

#Main method that runs the main menu allowing the user to choose which option they want to calculate.
def main():
    print("What would you like to calculate?")
    print("1. Voltage")
    print("2. Current")
    print("3. Resistance")
    print("")
    selection = input("Choice: ")

    if selection == "1":
        voltage()
        main()
    elif selection == "2":
        current()
        main()
    elif selection == "3":
        resistance()
        main()

#Voltage method, user inputs the values of current and resistance, and the voltage is calculated based on these.
def voltage():
    setCurrent = int(input("Enter the current: "))
    setResistance = int(input("Enter the resistance: "))
    curr = setCurrent
    res = setResistance
    setVoltage = curr * res                                                               
    print("Voltage = " +str(curr)+ " x " +str(res)+" = "+str(setVoltage))
    print("")

#Currnet method, user inputs the values of voltage and resistance, and the current is calculated based on these.
def current():
    setResistance = int(input("Enter the resistance: "))
    setVoltage = int(input("Enter the voltage: "))
    res = setResistance
    volt = setVoltage
    setCurrent = volt / res
    print("Current = " +str(volt)+ " / " +str(res)+" = "+str(setCurrent)) 

#Resistance method, user inputs the values of current and voltage, and the resistance is calculated based on these.
def resistance():
    setCurrent = int(input("Enter the current: "))
    setVoltage = int(input("Enter the voltage: "))
    curr = setCurrent
    volt = setVoltage
    setResistance = volt / curr
    print("Resistance =" +str(volt)+ "/" +str(curr)+ " = "+str(setResistance))
    
main()