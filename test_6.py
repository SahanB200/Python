#Author: Sahan Baddegama
#Date: 15th Mar 2025

#to perform some conversion from metrics to imperial and imperial to metrics

import conversion
import validation

centimeters = validation.float_input("Enter the centimeters: ", min_value= 0)
inches = conversion.cm2inch(centimeters)
print("Inches :", inches)

ounce = validation.float_input("Enter the ounces: ", min_value= 0)
kilograms = conversion.ounce2kg(ounce, 3, True)
print("Kilograms :", kilograms)

kilograms = validation.float_input("Enter the weight in kilograms: ", min_value= 0)
ounces = conversion.kg2ounce(kilograms, add_unit = True)
print("Ounces :", ounces)