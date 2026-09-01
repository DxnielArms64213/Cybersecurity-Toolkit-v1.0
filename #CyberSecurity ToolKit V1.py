#CyberSecurity ToolKit V1.0

# ============================================================
#              CYBER TOOLKIT v1.0 - MENU PLAN
# ============================================================
# Version 0.1 -> Main Menu
# Version 0.2 -> Password Generator
# Version 0.3 -> Password Strength Checker
# Version 0.4 -> Encode / Decode
# Version 0.5 -> Hash Generator
# Version 0.6 -> File Hash Checker
# Version 0.7 -> IP Information
# Version 0.8 -> Subnet Calculator
# Version 0.9 -> Port Scanner
# Version 1.0 -> Log Analyzer 
#
# MAIN MENU
#
# 1. Password Generator
# 2. Password Strength Checker
# 3. Hash Generator
# 4. IP Information
# 5. Port Scanner
# 6. File Hash Checker
# 7. Encode / Decode
# 8. Subnet Calculator
# 9. Log Analyzer
# 10. Exit

import random
import secrets


#Password generator function
def password_generator():
    generated=0 
    valid_length=False
    while valid_length==False:
        try:
            length=int(input("how long do you want your password to be? ").lower().strip())
            if length<=0 or length>20:
                print("invalid length try again")
            else:
                valid_length=True
        except ValueError:
            print("please enter a number")
            valid_length=False
    password=[]
    while generated!=length:
            letters="abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"1234567890"+"_=+/.,<>#!$%^&*"
            random_index=secrets.randbelow(len(letters))
            random_character=letters[random_index]
            generated=generated+1
            password.append(random_character)
    password="".join(password)
    return password


def strength_checker():
    c=("not ready yet")
    return c 
def hash_generator():
    c=("not ready yet")
    return c 
def ip_information():
    c=("not ready yet")
    return c 
def port_scanner():
    c=("not ready")
    return c
def file_hash_checker():
    c=("G")
    return c 
def encode_decode():
    c=("return")
    return c 
def subnet_calculator():
    c=("G")
    return c 
def log_analyzer():
    c=("B")
    return c



#options list to make if/elif statements not as long and to tidy up code
options={
    "password generator" :password_generator
    ,
    "one":password_generator
    ,
    "1":password_generator
    ,
    "password strength checker":strength_checker
    ,
    "two":strength_checker
    ,
    "2":strength_checker
    ,
    "hash generator":hash_generator
    ,
    "three":hash_generator
    ,
    "3":hash_generator
    ,
    "ip information":ip_information
    ,
    "four":ip_information
    ,
    "4":ip_information
    ,
    "port scanner":port_scanner
    ,
    "5":port_scanner
    ,
    "five":port_scanner
    ,
    "file hash checker":file_hash_checker
    ,
    "6":file_hash_checker
    ,
    "six":file_hash_checker
    ,
    "encode / decode":encode_decode
    ,
    "7":encode_decode
    ,
    "seven":encode_decode
    ,
    "subnet calculator":subnet_calculator
    ,
    "8":subnet_calculator
    ,
    "eight":subnet_calculator
    ,
    "log analyzer":log_analyzer
    ,
    "9":log_analyzer
    ,
    "nine":log_analyzer
    ,

}
exit_program=("exit","10","ten")




def menu_main():
    running=True
    while running==True:
        menu=(input("""    ╔══════════════════════════════════════════╗
    ║              CYBER TOOLKIT               ║
    ╠══════════════════════════════════════════╣
    ║ 1. Password Generator                    ║
    ║ 2. Password Strength Checker             ║
    ║ 3. Hash Generator                        ║
    ║ 4. IP Information                        ║
    ║ 5. Port Scanner                          ║
    ║ 6. File Hash Checker                     ║
    ║ 7. Encode / Decode                       ║
    ║ 8. Subnet Calculator                     ║
    ║ 9. Log Analyzer                          ║
    ║ 10. Exit                                 ║
    ╚══════════════════════════════════════════╝""")).lower().strip().split()
        menu=" ".join(menu)
        if menu in options:
          result=options[menu]()
          print(result)
        elif menu in exit_program:
            running=False
        else:
            print("invalid option, please try again!")




menu_main()
