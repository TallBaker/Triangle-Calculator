# Import functions etc ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import math
from fractions import Fraction
from colorama import Fore, Back, Style, init
init(autoreset=True)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

global proceed
proceed = False
verified_colour = Fore.GREEN
invalid_colour = Fore.RED
possibility_colour = Fore.CYAN

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Asking degrees or radians and decimal points wanted and validation

def radians_or_degrees_and_dp():
    global angle_type
    global decimal_points
    rad_answered = False
    dec_answered = False
    while not rad_answered:
        angle_type = input("Enter radians/degrees: ")
        if angle_type == "radians":
            rad_answered = True
            print(verified_colour + "Radians accepted \n")
        elif angle_type == "degrees":
            rad_answered = True
            print(verified_colour + "Degrees accepted \n")
        else:
            rad_answered = False
            print(invalid_colour + "Angle type invalid! \n")
    while not dec_answered:
        decimal_points = input("Enter number of decimal points: ")
        try:
            decimal_points = int(decimal_points)
            if decimal_points >= 0:
                dec_answered = True
                print(verified_colour + "d.p accepted \n")
            else:
                print(invalid_colour + "d.p invalid! \n")
        except:
            dec_answered = False
            print(invalid_colour + "d.p invalid! \n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Inputting sides and angles for later calculation ~~~~~~~~~~

def side_angle_inputs():
    global side_list   
    global angle_list 
    print("Enter three values (Enter to skip) \n")
    side_a = input("Side A: ")
    angle_A = input("Angle A: ")
    side_b = input("Side B: ")
    angle_B = input("Angle B: ")
    side_c = input("Side C: ")
    angle_C = input("Angle C: ")
    print("")
    side_list = [
        [side_a,"Side A"],
        [side_b,"Side B"],
        [side_c,"Side C"]
    ]
    angle_list = [
        [angle_A,"Angle A"],
        [angle_B,"Angle B"],
        [angle_C,"Angle C"]
    ]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Turns an inputted fraction of pi into its radians equivalent

def fractions_to_radians(angle):
    if "/" in angle:
        if angle_type == "radians":
            if "pi" in angle or "π" in angle:
                if "pi" in angle:
                    angle = angle.replace("pi","")
                elif "π" in angle:
                    angle = angle.replace("π","")  
            position_of_fraction = angle.find("/")            
            if position_of_fraction == 0:
                numerator = math.pi
                denominator = float(angle[1:])
                angle = numerator/denominator
            else:
                numerator = math.pi * float(angle[:position_of_fraction])
                denominator = float(angle[position_of_fraction+1:])
                angle = numerator / denominator
        else:
            position_of_fraction = angle.find("/")
            numerator = float(angle[:position_of_fraction])
            denominator = float(angle[position_of_fraction+1:])
            angle = math.radians(numerator / denominator)
    else:
        if angle_type == "degrees":
            angle = math.radians(float(angle))
        else:
            angle = float(angle)
    return(angle)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~           

# Validating the inputs and turning them into float variables, stored in a list

def float_validator_and_list_maker():
    global proceed 
    global float_side_list 
    global float_angle_list 
    global num_true_count_sides 
    global num_true_count_angles
    num_true_count_sides = 0
    num_true_count_angles = 0
    count = 0
    float_side_list = [
        [0,"side_a",False],
        [0,"side_b",False],
        [0,"side_c",False]
    ]
    float_angle_list =[
        [0,"angle_A",False],
        [0,"angle_B",False],
        [0,"angle_C",False]
    ]
    for count in range(0,3,1):
        if "-" in side_list[count][0]:
            print(invalid_colour + f"{angle_list[count][1]} invalid")
        else:
            try:
                float_side_list[count][0] = float(side_list[count][0])
                if float_side_list[count][0] != 0:
                    float_side_list[count][2] = True
                    print(verified_colour + f"{side_list[count][1]} verified")
                    num_true_count_sides += 1
                else:
                    print(invalid_colour + f"{angle_list[count][1]} invalid")
            except:
                float_side_list[count][0] = side_list[count][0]
                print(invalid_colour + f"{side_list[count][1]} invalid")
    for count in range(0,3,1):
        if "-" in angle_list[count][0]:
            print(invalid_colour + f"{angle_list[count][1]} invalid")
        else:
            try:
                float_angle_list[count][0] = float(fractions_to_radians(angle_list[count][0]))
                if float_angle_list[count][0] != 0 and float_angle_list[count][0] != math.pi:
                    num_true_count_angles += 1
                    float_angle_list[count][2] = True
                    print(verified_colour + f"{angle_list[count][1]} verified")
                else:
                    print(invalid_colour + f"{angle_list[count][1]} invalid")
            except:
                print(invalid_colour + f"{angle_list[count][1]} invalid")
    if (num_true_count_sides + num_true_count_angles) < 3:
        proceed = False
        print(Style.BRIGHT + invalid_colour + "\nToo few valid inputs! \n")
    elif (num_true_count_sides + num_true_count_angles) > 3:
        proceed = False
        print(Style.BRIGHT + invalid_colour + "\nToo many inputs! \n")
    elif num_true_count_angles == 3:
        proceed = False
        print(Style.BRIGHT + invalid_colour + "\nNeed at least 1 side! \n")
    else:
        proceed = True
        print(Style.BRIGHT + verified_colour + "\nValid inputs! \n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# All the mathematical operations needed for the triangle ~~~

def cosine_rule_side(side_1,side_2,angle_3): # cosine rule to work out a side
    side_3_squared = (side_1**2)+(side_2**2)-(2*(side_1*side_2*math.cos(angle_3)))
    side_3 = math.sqrt(side_3_squared)
    return(side_3)

def cosine_rule_angle(side_1,side_2,side_3): # cosine rule to work out an angle
    numerator = (side_1**2 - side_2**2 - side_3**2)
    denominator = (-2 * side_2 * side_3)
    angle_1 = math.acos(numerator/denominator)
    return (angle_1)

def sine_rule_side(side_2,angle_2,angle_1): # sine rule to work out another side
    numerator = (side_2 * math.sin(angle_1))
    denominator = (math.sin(angle_2))
    side_1 = (numerator/denominator)
    return (side_1)

def sine_rule_angle(side_1,side_2,angle_2): # sine rule to work out another angle
    numerator = side_1 * math.sin(angle_2)
    denominator = side_2
    angle_1 = math.asin(numerator/denominator)
    return(angle_1)

def angles_in_a_triangle(angle_1,angle_2): # angles in a triangle = 180 or pi
    angle_3 = math.pi-angle_1-angle_2
    return (angle_3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The main function that has preprogrammed calculations to work out the sides and angles of the triangle

def calculations():
    global possibility_side_list 
    global possibility_angle_list 
    global possibilities 
    global float_angle_list 
    global float_side_list
    possibility_side_list = [
        [float_side_list[0][0],"possible side_a"],
        [float_side_list[1][0],"possible side_b"],
        [float_side_list[2][0],"possible side_c"]
    ]
    possibility_angle_list = [
        [float_angle_list[0][0],"possible angle_A"],
        [float_angle_list[1][0],"possible angle_B"],
        [float_angle_list[2][0],"possible angle_C"]
    ]
    possibilities = 1
    if num_true_count_sides == 3: # if 3 sides are given ~~~~~~~
        for count in range(0,3,1):
            side_1 = float_side_list[count][0]
            side_2 = float_side_list[count-1][0]
            side_3 = float_side_list[count-2][0]
            float_angle_list[count][0] = cosine_rule_angle(side_1,side_2,side_3)
    elif num_true_count_sides == 2 and num_true_count_angles == 1: # if 2 sides and 1 angle are given ~~~~~~~~
        for count in range(0,3,1):
            if float_side_list[count][2] and float_angle_list[count][2]: # if the angle is not inbetween the two given sides
                possibilities = 2
                side_1 = float_side_list[count][0]
                angle_1 = float_angle_list[count][0]

                if float_side_list[count-1][2]: # if the other side given is the one before the side with a corresponding angle in the lists
                    side_2 = float_side_list[count-1][0]
                    float_angle_list[count-1][0] = sine_rule_angle(side_2,side_1,angle_1)
                    float_angle_list[count-2][0] = angles_in_a_triangle(float_angle_list[count-1][0],angle_1)
                    float_side_list[count-2][0] = cosine_rule_side(side_1,side_2,float_angle_list[count-2][0])

                    possibility_angle_list[count-1][0] = math.pi - sine_rule_angle(side_2,side_1,angle_1)
                    possibility_angle_list[count-2][0] = angles_in_a_triangle(possibility_angle_list[count-1][0],angle_1)
                    possibility_side_list[count-2][0] = cosine_rule_side(side_1,side_2,possibility_angle_list[count-2][0])

                elif float_side_list[count-2][2]: # if the other side is the one that is 2x before the side with a corresponding angle in the lists
                    side_2 = float_side_list[count-2][0]
                    float_angle_list[count-2][0] = sine_rule_angle(side_2,side_1,angle_1)
                    float_angle_list[count-1][0] = angles_in_a_triangle(float_angle_list[count-2][0],angle_1)
                    float_side_list[count-1][0] = cosine_rule_side(side_1,side_2,float_angle_list[count-1][0])

                    possibility_angle_list[count-2][0] = math.pi - sine_rule_angle(side_2,side_1,angle_1)
                    possibility_angle_list[count-1][0] = angles_in_a_triangle(possibility_angle_list[count-2][0],angle_1)
                    possibility_side_list[count-1][0] = cosine_rule_side(side_1,side_2,possibility_angle_list[count-1][0])

            elif not float_side_list[count][2] and float_angle_list[count][2]: # if the angle is inbetween the two given sides
                side_1 = float_side_list[count-1][0]
                side_2 = float_side_list[count-2][0]
                angle_3 = float_angle_list[count][0]
                float_side_list[count][0] = cosine_rule_side(side_1,side_2,angle_3)
                float_angle_list[count-1][0] = cosine_rule_angle(side_1,side_2,float_side_list[count][0])
                float_angle_list[count-2][0] = angles_in_a_triangle(angle_3,float_angle_list[count-1][0])

    elif num_true_count_sides == 1 and num_true_count_angles == 2: # if 1 side and 2 angles are given ~~~~~~
        for count in range(0,3,1):
            side_1 = float_side_list[count][0]

            if float_side_list[count][2] and float_angle_list[count][2]: # if the side given has a corresponding angle
                angle_1 = float_angle_list[count][0]

                if float_angle_list[count-1][0]: # if the other angle given is the one before the side with a corresponding angle in the lists
                    angle_2 = float_angle_list[count-1][0]
                    float_angle_list[count-2][0] = angles_in_a_triangle(angle_1,angle_2)
                    float_side_list[count-1][0] = sine_rule_side(side_1,angle_2,angle_1)
                    float_side_list[count-2][0] = sine_rule_side(side_1,float_angle_list[count-2][0],angle_1)

                elif float_angle_list[count-2][0]: # if the other angle given is the one that is 2x before the side with a corresponding angle in the lists
                    angle_2 = float_angle_list[count-2][0]
                    float_angle_list[count-1][0] = angles_in_a_triangle(angle_1,angle_2)
                    float_side_list[count-2][0] = sine_rule_side(side_1,angle_2,angle_1)
                    float_side_list[count-1][0] = sine_rule_side(side_1,float_angle_list[count-1][0],angle_1)

            elif float_side_list[count][2] and float_angle_list[count-1][2] and float_angle_list[count-2][2]: # if the side does not have a corresponding angle
                angle_2 = float_angle_list[count-1][0]
                angle_3 = float_angle_list[count-2][0]
                float_angle_list[count][0] = angles_in_a_triangle(angle_2,angle_3)
                float_side_list[count-1][0] = sine_rule_side(side_1,float_angle_list[count][0],angle_2)
                float_side_list[count-2][0] = sine_rule_side(side_1,float_angle_list[count][0],angle_3)
    
    # 3 angles has been rejected before hand in float_validator_and_list_maker

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Turns a radians angle into a fraction of pi if the denominator is less than or equal to 12

def radians_to_pi_fraction(radians_value):
    coefficient = radians_value / math.pi
    fraction = Fraction(coefficient).limit_denominator()
    if fraction.numerator == 0:
        return("0")
    elif fraction.numerator == 1:
        return(f"π/{fraction.denominator}") if fraction.denominator != 1 else "π"
    elif fraction.denominator > 12:
        return(f"{round(radians_value,decimal_points)}")
    else:
        return(f"{fraction.numerator}π/{fraction.denominator}") if fraction.denominator != 1 else f"{fraction.numerator}π"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Rounds the values and stores them to a seperate list for later use

def lists_rounder():
    global rounded_side_list
    global rounded_angle_list
    global possible_rounded_side_list
    global possible_rounded_angle_list
    global possibilities
    sides_same = 0
    rounded_side_list = [
        ["","rounded side_a"],
        ["","rounded side_b"],
        ["","rounded side_c"]
    ]
    rounded_angle_list = [
        ["","rounded angle_A"],
        ["","rounded angle_B"],
        ["","rounded angle_C"]
    ]
    possible_rounded_side_list = [
        ["","possible rounded angle_A"],
        ["","possible rounded angle_B"],
        ["","possible rounded angle_C"]
    ]
    possible_rounded_angle_list = [
        ["","possible rounded angle_A"],
        ["","possible rounded angle_B"],
        ["","possible rounded angle_C"]
    ]
    for count in range(0,3,1):
        rounded_side_list[count][0] = round(float_side_list[count][0],decimal_points)
        if angle_type == "degrees":
            rounded_angle_list[count][0] = round(math.degrees(float_angle_list[count][0]),decimal_points)
            if possibilities == 2:
                possible_rounded_side_list[count][0] = round(possibility_side_list[count][0],decimal_points)
                possible_rounded_angle_list[count][0] = round(math.degrees(possibility_angle_list[count][0]),decimal_points)
        else:
            rounded_angle_list[count][0] = radians_to_pi_fraction(float_angle_list[count][0])
            if possibilities == 2:
                possible_rounded_side_list[count][0] = round(possibility_side_list[count][0],decimal_points)
                possible_rounded_angle_list[count][0] = radians_to_pi_fraction(possibility_angle_list[count][0])
        if round(rounded_side_list[count][0],5) == round(possible_rounded_side_list[count][0],5):
            sides_same += 1
    if sides_same == 3:
        possibilities = 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Prints the finsihed answers in a nice fashion

def printer():
    print(Style.BRIGHT + Fore.GREEN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
    if possibilities == 2:
        print(possibility_colour + "Possibility 1: \n")
        for count in range(0,3,1):
            print(f"{side_list[count][1]} = {rounded_side_list[count][0]}")
        print("")
        for count in range(0,3,1):
            print(f"{angle_list[count][1]} = {rounded_angle_list[count][0]}")
        print(possibility_colour + "\nPossibility 2: \n")
        for count in range(0,3,1):
            print(f"{side_list[count][1]} = {possible_rounded_side_list[count][0]}")
        print("")
        for count in range(0,3,1):
            print(f"{angle_list[count][1]} = {possible_rounded_angle_list[count][0]}")
    else:
        for count in range(0,3,1):
            print(f"{side_list[count][1]} = {rounded_side_list[count][0]}")
        print("")
        for count in range(0,3,1):
            print(f"{angle_list[count][1]} = {rounded_angle_list[count][0]}")
    print(Style.BRIGHT + Fore.GREEN + "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The main spine of the program, the sequence of all the functions to call

def main_body_for_calculations():
    global proceed
    global possibilities
    count = 0
    faults = 0
    radians_or_degrees_and_dp()
    while not proceed or count == 0:
        side_angle_inputs()
        float_validator_and_list_maker()
        count += 1
        if proceed:
            try:
                calculations()
            except:
                proceed = False
                faults += 1
            for count in range(0,3,1):
                if float_angle_list[count][0] <= 0 or float_side_list[count][0] <= 0:
                    proceed = False
                    faults += 1
                if possibilities == 2:
                    if possibility_angle_list[count][0] <= 0 or possibility_side_list[count][0] <= 0:
                        possibilities = 1
            if faults != 0 and not proceed:
                print(Style.BRIGHT + invalid_colour + "Invalid triangle! \n")
            faults = 0
    lists_rounder()
    printer()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

main_body_for_calculations()