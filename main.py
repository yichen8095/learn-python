# Convert temperature:
# Celsius to Fahrenheit or Fahrenheit to Celsius
degree = input("Please input temperature: ")

if degree[-1] in ['c', 'C']:
    print(f"Fahrenheit is {float(degree[0:-1]) * 1.8 + 32:.2f}F")
elif degree[-1] in ['f', 'F']:
    print(f"Celsius is {(float(degree[0:-1]) - 32) / 1.8:.2f}C")
else:
    print("Invalid format usage: 30C or 58F")
