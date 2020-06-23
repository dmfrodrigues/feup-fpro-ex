def kelvin_to_fahrenheit(temp):
    if temp < 0:
        return AssertionError("Colder than absolute zero!")
    return int(((temp - 273.15)*9/5+32)+0.5)
print(kelvin_to_fahrenheit(273))
print(kelvin_to_fahrenheit(-5))