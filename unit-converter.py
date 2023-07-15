def convert_temperature():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit: ", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius: ", celsius)
    else:
        print("Invalid choice")


def convert_distance():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        kilometers = float(input("Enter distance in Kilometers: "))
        miles = kilometers * 0.621371
        print("Distance in Miles: ", miles)
    elif choice == 2:
        miles = float(input("Enter distance in Miles: "))
        kilometers = miles / 0.621371
        print("Distance in Kilometers: ", kilometers)
    else:
        print("Invalid choice")


def convert_weight():
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        kilograms = float(input("Enter weight in Kilograms: "))
        pounds = kilograms * 2.20462
        print("Weight in Pounds: ", pounds)
    elif choice == 2:
        pounds = float(input("Enter weight in Pounds: "))
        kilograms = pounds / 2.20462
        print("Weight in Kilograms: ", kilograms)
    else:
        print("Invalid choice")


def main():
    print("Unit Converter")
    print("1. Temperature")
    print("2. Distance")
    print("3. Weight")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_distance()
    elif choice == 3:
        convert_weight()
    else:
        print("Invalid choice")


if _name_ == '_main_':
    main()