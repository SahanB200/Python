#Author : Sahan Baddegama
#Date: 15 Mar 2025



def cm2inch (centimeters, rounding = 2, add_unit = False):
    if add_unit:
        inches = str(round(centimeters * 0.3937, rounding))+" inches"
    else:
        inches = round(centimeters * 0.3937, rounding)
    return inches

def inch2cm (inches, rounding = 2, add_unit = False):
    if add_unit:
        centimeters = str(round(inches * 2.54, rounding))+" cm"
    else:
        centimeters = round(inches * 2.54, rounding)
    return centimeters

def kg2ounce (kilograms, rounding = 2, add_unit = False):
    if add_unit:
        ounces = str(round(kilograms * 35.2739, rounding))+" ounces"
    else:
        ounces = round(kilograms * 35.2739, rounding)
    return ounces

def ounce2kg (ounces, rounding = 2, add_unit = False):
    if add_unit:
        kilograms = str(round(ounces * 0.0283, rounding))+" kg"
    else:
        kilograms = round(ounces * 0.0283, rounding)
    return kilograms