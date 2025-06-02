def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        elif to_unit == "K":
            return celsius_to_kelvin(value)
    elif from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        elif to_unit == "K":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        elif to_unit == "F":
            return kelvin_to_fahrenheit(value)

    return None


def main():
    print("Temperature Converter")
    print("Available units: C (Celsius), F (Fahrenheit), K (Kelvin)")

    from_unit = input("Enter the source unit (C/F/K): ").strip().upper()
    to_unit = input("Enter the target unit (C/F/K): ").strip().upper()
    value = float(input(f"Enter the temperature value in {from_unit}: "))

    result = convert_temperature(value, from_unit, to_unit)
    if result is not None:
        print(f"\n{value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        print("Invalid conversion requested.")


if __name__ == "__main__":
    main()
