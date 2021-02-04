import csv
import os

import admin
import error
import getTime
import listGenrator


def show(typeofUser, user):
    order = '*'
    while True:
        #Last Login
        newLastLogin = getTime.persianDate()
        odd = []
        newLast = {'lastLogin': newLastLogin}
        with open("admins.csv", 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                data = dict(row)

                if data['username'] == user:
                    data.update(newLast)
                odd.append(data)

        with open('admins.csv', 'w') as csvFile:
            fields = ['username', 'pass', 'lastLogin', 'name']
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(odd)
        # End of Last Login
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print('\t' + "╔" + "═" * 62 + "╗")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "║" + " " * 24 + "Welcome Admin" + " " * 25 + "║")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "╠" + "═" * 62 + "╣")
        print(
            '\t' + "║" + listGenrator.lenFit(str("  " + getTime.persianDate() + " | " + getTime.time()), 39) + listGenrator.lenFit(str("Last Login: " + getTime.lastLogin(
                'a', user)), 22) + " ║")
        print('\t' + "╠" + "═" * 62 + "╣")
        print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "║" + listGenrator.lenFit('    T: Teachers List', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    S: Students List', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    L: Lessons List', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    AU: Add User', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    AL: Add Lesson', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    ED: Edit', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    EP: Edit Password', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    E: Exit', 62) + "║")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "╚" + "═" * 62 + "╝")

        request = str(input("             Your request:"))
        if request == 'T' or request == 't':
            print(listGenrator.teaList())
            order = str(input("             Enter code:"))
        elif request == 'S' or request == 's':
            print(listGenrator.stuList())
            order = str(input("             Enter code:"))
        elif request == 'L' or request == 'l':
            print(listGenrator.lessonList())
            order = str(input("             Enter code:"))
        elif request == 'AU' or request == 'au':
            admin.au()
        elif request == 'AL' or request == 'al':
            admin.al()
        elif request == 'ED' or request == 'ed':
            admin.e(user)
        elif request == 'EP' or request == 'ep':
            admin.ep(user)
        elif request == 'E' or request == 'e':
            break
        else:
            print(error.errorsList("005"))

        if order == 'B' or order == 'b':
            continue

        order = '*'