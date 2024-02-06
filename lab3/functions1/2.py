'''Read in a Fahrenheit temperature.Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F - 32)'''
def to_C(f):
    C=(5/9)*(float(f)-32)
    return C
Fahrenheit=input()
result=to_C(Fahrenheit)
print(f"{result:.2f}")