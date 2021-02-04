import csv

import os

import database
import error
import getTime
import listGenrator
import stu
import tea


def show(typeofUser, user):
    order = '*'
    while True:
        newLastLogin = getTime.persianDate()
        odd = []
        newLast = {'lastLogin': newLastLogin}
        with open("students.csv", 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                data = dict(row)

                if data['username'] == user:
                    data.update(newLast)
                odd.append(data)

        with open('students.csv', 'w') as csvFile:
            fields = ['username', 'pass', 'lastLogin', 'name']
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(odd)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print('\t' + "╔" + "═" * 62 + "╗")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "║" + " " * 24 + "Welcome Admin" + " " * 25 + "║")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "╠" + "═" * 62 + "╣")
        print(
            '\t' + "║" + listGenrator.lenFit(str("  " + getTime.persianDate() + " | " + getTime.time()),
                                             39) + listGenrator.lenFit(str("Last Login: " + getTime.lastLogin(
                's', user)), 22) + " ║")
        print('\t' + "╠" + "═" * 62 + "╣")
        print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "║" + listGenrator.lenFit('    L: Lessons', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    LP: Pick Lessons', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    ED: Edit', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    EP: Edit Password', 62) + "║")
        print('\t' + "║" + listGenrator.lenFit('    E: Exit', 62) + "║")
        print('\t' + "║" + " " * 62 + "║")
        print('\t' + "╚" + "═" * 62 + "╝")

        request = str(input("             Your request:"))
        if request == 'L' or request == 'l':
            print(listGenrator.lesListStu(database.stuSearch(user)))
            order = str(input("             Enter code:"))
        elif request == 'LP' or request == 'lp':
            stu.lp(user)
        elif request == 'P' or request == 'p':
            return
        elif request == 'ED' or request == 'ed':
            stu.e(user)
        elif request == 'EP' or request == 'ep':
            stu.ep(user)
        elif request == 'E' or request == 'e':
            break
        else:
            print(error.errorsList("005"))

        if order == 'B' or order == 'b':
            continue

        order = '*'
