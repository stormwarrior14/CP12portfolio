UNITS = {
    "Meters (m)": ("length", 1.0),
    "Kilometers (km)": ("length", 1000.0),
    "Centimeters (cm)": ("length", 0.01),
    "Millimeters (mm)": ("length", 0.001),
    "Miles (mi)": ("length", 1609.344),
    "Yards (yd)": ("length", 0.9144),
    "Feet (ft)": ("length", 0.3048),
    "Inches (in)": ("length", 0.0254),

    "Kilograms (kg)": ("mass", 1.0),
    "Grams (g)": ("mass", 0.001),
    "Milligrams (mg)": ("mass", 0.000001),
    "Metric Tons (t)": ("mass", 1000.0),
    "Pounds (lb)": ("mass", 0.45359237),
    "Ounces (oz)": ("mass", 0.028349523125),

    "Celsius (°C)": ("temperature", 1.0),
    "Fahrenheit (°F)": ("temperature", 1.0),
    "Kelvin (K)": ("temperature", 1.0),

    "Liters (L)": ("volume", 1.0),
    "Milliliters (mL)": ("volume", 0.001),
    "Cubic Meters (m³)": ("volume", 1000.0),
    "US Gallons (gal)": ("volume", 3.785411784),
    "US Cups (cup)": ("volume", 0.2365882365),
    "US Fluid Ounces (fl oz)": ("volume", 0.0295735295625),

    "Seconds (s)": ("time", 1.0),
    "Minutes (min)": ("time", 60.0),
    "Hours (h)": ("time", 3600.0),
    "Days (d)": ("time", 86400.0),
}

def to_base(value, unit):  # converts value to its category's base unit
    category, factor = UNITS[unit]

    if category == "temperature":  # converts temperature to Celsius
        if unit == "Fahrenheit (°F)":
            return (value - 32) * 5 / 9
        if unit == "Kelvin (K)":
            return value - 273.15
        return value

    return value * factor  # applies the unit conversion factor


def from_base(value, unit):  # converts base value to target unit
    category, factor = UNITS[unit]

    if category == "temperature":  # converts Celsius to target
        if unit == "Fahrenheit (°F)":
            return (value * 9 / 5) + 32
        if unit == "Kelvin (K)":
            return value + 273.15
        return value

    return value / factor  # reverses the conversion factor


def convert_units(value, from_unit, to_unit):  # converts between units

    base_value = to_base(value, from_unit)  # converts to base unit
    result = from_base(base_value, to_unit)  # converts to target unit

    print(result)
    return result  # returns the final result

value = float(input("value: "))
from_unit = input("unit: ")
to_unit = input("target: ")

convert_units(value, from_unit, to_unit)