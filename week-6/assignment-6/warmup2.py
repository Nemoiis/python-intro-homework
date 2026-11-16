def celcius_to_fahrenheit(c): 
    fahrenheit = round((c * 9/5) + 32, 1)
    return f"{c}°C = {fahrenheit}°F"

def fahrenheit_to_celcius(f):
    celcius = round((f - 32) * 5/9, 1)
    return f"{f}°F = {celcius}°C"

print(celcius_to_fahrenheit(19))
print(celcius_to_fahrenheit(0))
print(fahrenheit_to_celcius(32))
print(fahrenheit_to_celcius(75))