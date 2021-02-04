import os

import getTime
import error
import listGenrator
import login

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + " " * 24 + "GoodUniversity" + " " * 24 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "╠" + "═" * 62 + "╣")
    print('\t' + "║" + " " * 2 + listGenrator.lenFit(str(getTime.persianDate() + " | " + getTime.time()), 60) + "║")
    print('\t' + "╠" + "═" * 62 + "╣")
    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + "    L : Login" + " " * 49 + "║")
    print('\t' + "║" + "    R : Register" + " " * 46 + "║")
    print('\t' + "║" + "    E : Exit" + " " * 50 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "╚" + "═" * 62 + "╝")

    request = str(input("             Your request:"))
    if request == 'R' or request == 'r':
        typeof = str(input("             Your type:"))
        username = str(input("             Your username:"))
        passcode = str(input("             Your password:"))
        login.register(typeof, username, passcode)
    elif request == 'L' or request == 'l':
        username = str(input("             Username:"))
        passcode = str(input("             Password:"))
        print(login.loginChecker(username, passcode))
    elif request == 'E' or request == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print(error.errorsList("005"))
