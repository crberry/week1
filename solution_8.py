#convert.py
# A program to convert Farenheit temperature to Celsius
# by Christopher Berry

def main():
    farenheit = eval(input("What is the Farenheit temperature? "))
    celsius = (farenheit - 32)/1.8
    print("The temperature is",round(celsius,2),"degrees Celsius.")
    print("or",round((celsius + 273.15),2),"degrees Kelvin. ")
main()
    
