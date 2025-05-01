TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

"""
main.py: první projekt do Engeto Online Python Akademie
author: Tomáš Jasný
email: tomas.jasny@seznam.cz
"""

registration_dict = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = "----------------------------------------"
user_name = input("username:\n")
user_password = input("password:\n")
print(oddelovac)

if user_name in registration_dict.keys():
    if user_password == registration_dict[user_name]:
        print(f"Welcome to the app, {user_name}.\nWe have {len(TEXTS)} texts to be analysed.")
        print(oddelovac)
        user_text = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select:\n")) - 1
        print(oddelovac)
        if user_text not in range(0, len(TEXTS)):
            print("Text not available.")
        else:
            analyse_text = TEXTS[user_text]
            analyse_text_list = analyse_text.split()
            analyse_text_list_numbers = []
            analyse_text_dict = {}

            number_word = 0
            number_titlecase = 0
            number_uppercase = 0
            number_lowercase = 0
            number_numeric = 0

            for word in analyse_text_list:
                word = word.strip(",.")
                number_word += 1
                analyse_text_dict[len(word)] = analyse_text_dict.get(len(word),0) +1

                if word.istitle() == True:
                    number_titlecase += 1
                if word.isupper() == True:
                    number_uppercase += 1
                if word.islower() == True:
                    number_lowercase += 1
                if word.isnumeric() == True:
                    number_numeric += 1
                    analyse_text_list_numbers.append(int(word))

            print(f'''There are {number_word} words in the selected text.\nThere are {number_titlecase} titlecase words.\nThere are {number_uppercase} uppercase words.\nThere are {number_lowercase} lowercase words.\nThere are {number_numeric} numeric strings.\nThe sum of all the numbers {sum(analyse_text_list_numbers)}\n{oddelovac}\n{"LEN|": >3}{"OCCURENCES": ^18}{"|NR.":<3}\n{oddelovac}''')
            for key in sorted(analyse_text_dict):
                print(f"{key: >3}|{'*' * analyse_text_dict.get(key): <18}|{analyse_text_dict.get(key):<3}")

    else:
        print("Unregistered user, terminating the program..")
else:
    print("Unregistered user, terminating the program!")