def temp_c_to_f(temperature_celsius):
    temp_fahrenheit = temperature_celsius * 1.8 + 32
    return temp_fahrenheit

temperature_fahrenheit = temp_c_to_f(20)
print(temperature_fahrenheit)