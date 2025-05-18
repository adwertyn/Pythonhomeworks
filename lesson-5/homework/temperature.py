def convert_cel_to_far(cel):    #function converts from Celsius  to Fahrenheit 
    far = cel * 9/5 + 32
    return round(far,2)

def convert_far_to_cel(far):    #function converts from Fahrenheit  to  Celsius
    cel = (far - 32) * 5/9
    return round(cel,2)

#Asking user Fahrenheit
far_cel = float(input("Enter a temperature in degrees F: "))
print(f"{far_cel} degrees F {convert_far_to_cel(far_cel)} degrees C") 

#Asking user Celsius
cel_far = float(input("Enter a temperature in degrees C: "))
print(f"{cel_far} degrees C = {convert_cel_to_far(cel_far)} degrees F")