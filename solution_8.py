#convert.py
# A program to convert Farenheit temperature to Celsius
# by Christopher Berry

def main():
    farenheit = eval(input("What is the Farenheit temperature? "))
    celsius = (farenheit - 32)/1.8
    print("The temperature is",celsius,"degrees Celsius.")
    print("or",(celsius + 273.15),"degrees Kelvin. ")
main()
    
