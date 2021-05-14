#####################################################
# APS106 Winter 2021 - Lab 3 - Measurement Parser   #
#####################################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    
    At_Symbol = email.find("@")
    Dot = email.find(".")
    First_name = email[:Dot]
    Last_name = email[Dot + 1:At_Symbol]
    return(Last_name.upper() + "," + First_name.upper())
###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
  
    total = 0
    for i in range (len(s)):
        if (s[i] == ","):
            total +=1
    return total//2    

######################################
# Part 3 - Calculate Control Average #
######################################

def calc_control_average(s):
    
    total = 0
    count = 0
    for i in range(len(s)):
        if (s[i] == "l"):
            count += 1
            number = s[i+2:s.find(",", i+2)]
            total += float(number)
    return round(total/count, 1)

###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info):
    
    At_Symbol = measurement_info.find("@")
    Dot = measurement_info.find(".")
    First_name = measurement_info[:Dot]
    Last_name = measurement_info[Dot + 1:At_Symbol]
    
    total1 = 0
    for i in range (len(measurement_info)):
        if (measurement_info[i] == ","):
            total1 +=1
    total1 = total1//2
    total = 0
    count = 0
    for i in range(len(measurement_info)):
        if (measurement_info[i] == "l"):
            count += 1
            number = measurement_info[i+2:measurement_info.find(",", i+2)]
            total += float(number)    
    
    return(Last_name.upper() + "," + First_name.upper() + "," + str(total1 -1) + "," + str(round(total/count, 1)))    
    