'''
solution extracted from https://www.pythonforbeginners.com/code-snippets-source-code/python-code-celsius-and-fahrenheit-converter/
'''


Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")