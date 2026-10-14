
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Kelvin to Celsius")

try:
    choice = int(input("Enter your choice: "))
    temp = float(input("Enter temperature: "))

    if choice == 1:
        if temp < -273.15:
            print("Invalid temperature")
        else:
            print("Result:", round(celsius_to_fahrenheit(temp), 2), "F")

    elif choice == 2:
        if temp < -273.15:
            print("Invalid temperature")
        else:
            print("Result:", round(celsius_to_kelvin(temp), 2), "K")

    elif choice == 3:
        if temp < -459.67:
            print("Invalid temperature")
        else:
            print("Result:", round(fahrenheit_to_celsius(temp), 2), "C")

    elif choice == 4:
        if temp < 0:
            print("Invalid temperature")
        else:
            print("Result:", round(kelvin_to_celsius(temp), 2), "C")

    else:
        print("Invalid choice")

except ValueError:
    print("Please enter a valid number")
