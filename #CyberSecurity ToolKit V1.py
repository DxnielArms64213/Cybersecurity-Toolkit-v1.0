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
import hashlib


#Password generator function
def password_generator():
    valid_length=False
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="1234567890"
    special_characters="!#$%&'()*+,-./:;<=>?@[]^_"
    choices={
            "yes":True
            ,
            "y":True
            ,
            "no":False
            ,
            "n":False
     }

    while True:
        lowercase_choice=input("do you want lowercase letters? y/n ").lower().strip()
        uppercase_choice=input("do you want uppercase letters? y/n ").lower().strip()
        numbers_choice=input("do you want numbers? y/n ").lower().strip()
        special_characters_choice=input("do you want special characters? y/n ").lower().strip()
        while lowercase_choice not in choices:
                print("please pick a choice, try again!")
                lowercase_choice=input("do you want lowercase letters? y/n ").lower().strip()
        while uppercase_choice not in choices:
                print("please pick a choice, try again!")
                uppercase_choice=input("do you want uppercase letters? y/n ").lower().strip()
        while numbers_choice not in choices:
                print("please pick a choice, try again")
                numbers_choice=input("do you want numbers? y/n ").lower().strip()
        while special_characters_choice not in choices:
                 print("please pick a choice, try again")
                 special_characters_choice=input("do you want special characters? y/n ").lower().strip()
        lowercase_enabled=choices[lowercase_choice]
        uppercase_enabled=choices[uppercase_choice]
        numbers_enabled=choices[numbers_choice]
        special_characters_enabled=choices[special_characters_choice]
        if lowercase_enabled or uppercase_enabled or numbers_enabled or special_characters_enabled:
            break

    character_pool=""
    if lowercase_enabled:
        character_pool+=lowercase
    if uppercase_enabled:
        character_pool+=uppercase
    if numbers_enabled:
        character_pool+=numbers
    if special_characters_enabled:
        character_pool+=special_characters

    number_of_types=lowercase_enabled+uppercase_enabled+numbers_enabled+special_characters_enabled

    while valid_length==False:
        try:
            length=int(input("how long do you want your password to be? ").lower().strip())
            if length<=0 or length>20 or length<number_of_types:
                print("invalid length try again")
            else:
                valid_length=True
        except ValueError:
            print("please enter a number")
            valid_length=False

    password=[]
    
    if lowercase_enabled:
        random_index=secrets.randbelow(len(lowercase))
        random_character=lowercase[random_index]
        password.append(random_character)
    if uppercase_enabled:
        random_index=secrets.randbelow(len(uppercase))
        random_character=uppercase[random_index]
        password.append(random_character)
    if numbers_enabled:
        random_index=secrets.randbelow(len(numbers))
        random_character=numbers[random_index]
        password.append(random_character)
    if special_characters_enabled:
        random_index=secrets.randbelow(len(special_characters))
        random_character=special_characters[random_index]
        password.append(random_character)
    
    while (len(password))<length:
            random_index=secrets.randbelow(len(character_pool))
            random_character=character_pool[random_index]
            password.append(random_character)
    secrets.SystemRandom().shuffle(password)
    password="".join(password)
    print(password)


def strength_checker():
    password=input("please enter your password: ")
    score=0
    special_characters="!#$%&'()*+,-./:;<=>?@[]^_"
    length=(len(password))
    lowercase_found=False
    uppercase_found=False
    numbers_found=False
    special_found=False
    for character in password:
        if character.islower() and not lowercase_found:
            score+=1
            lowercase_found=True
        if character.isupper() and not uppercase_found:
            score+=1
            uppercase_found=True
        if character.isdigit() and not numbers_found:
            score+=1
            numbers_found=True
        if character in special_characters and not special_found:
            score+=1
            special_found=True
    if length>=8:
        score+=2
    if length>=12:
        score+=2
    if length>=16:
        score+=2

    if score<=3:
        print(f"{score} is your score, this is a weak password")
    elif score<=6:
        print(f"{score} is your score, this is an okay password")
    elif score<=10:
        print(f"{score} is your score, this is a strong password")

def hash_generator():
    hash_options ={
        "sha256":hashlib.sha256
        ,
        "sha512":hashlib.sha512
        ,
        "sha1":hashlib.sha1

    }
    data=input("please enter the data you want to be hashed: ").lower().strip().encode()
    hash_choice=input("please enter the hash you want to use: (sha256/sha512/sha1)   ").lower().strip()
    hashed_data=hash_options[hash_choice](data)
    hashed_data=hashed_data.hexdigest()
    print(hashed_data)


    return  
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
    return


#dictionary to make if/elif statements not as long and to tidy up code
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
            options[menu]()
        elif menu in exit_program:
            running=False
        else:
            print("invalid option, please try again!")




menu_main()
