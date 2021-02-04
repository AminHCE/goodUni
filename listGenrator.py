import csv
import os


def lenFit(carry, lenth):
    return str(carry + " " * (lenth - len(carry)))


def stuList():
    with open('students.csv') as myFile:
        reader = csv.DictReader(myFile)
        data = [r for r in reader]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 24 + "Students List" + " " * 25 + "║")
    print('\t' + "╠" + "═" * 3 + "╤" + "═" * 16 + "╤" + "═" * 28 + "╤" + "═" * 12 + "╣")
    print('\t' + "║" + " # │ Student Number │            Name            │ Last Login " + "║")
    print('\t' + "╟" + "─" * 3 + "┼" + "─" * 16 + "┼" + "─" * 28 + "┼" + "─" * 12 + "╢")

    x = 0
    while data:
        if len(data) <= x:
            break
        print('\t' + "║ " + lenFit(str(x + 1), 2) + "│ " + lenFit(data[x]['username'], 15) + "│ " + lenFit(
            data[x]['name'], 27) + "│ " + lenFit(
            data[x]['lastLogin'], 11) + "║")
        if len(data) == x + 1:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 16 + "╧" + "═" * 28 + "╧" + "═" * 12 + "╣")
        elif len(data) != x:
            print('\t' + "╟" + "─" * 3 + "┼" + "─" * 16 + "┼" + "─" * 28 + "┼" + "─" * 12 + "╢")
        x += 1

    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + lenFit('    B: Back', 62) + "║")
    print('\t' + "╚" + "═" * 62 + "╝")
    return ' '


def teaList():
    with open('teachers.csv') as myFile:
        reader = csv.DictReader(myFile)
        data = [r for r in reader]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 24 + "Teachers List" + " " * 25 + "║")
    print('\t' + "╠" + "═" * 3 + "╤" + "═" * 16 + "╤" + "═" * 28 + "╤" + "═" * 12 + "╣")
    print('\t' + "║" + " # │ Teacher Number │            Name            │ Last Login " + "║")
    print('\t' + "╟" + "─" * 3 + "┼" + "─" * 16 + "┼" + "─" * 28 + "┼" + "─" * 12 + "╢")

    x = 0
    while data:
        if len(data) <= x:
            break
        print('\t' + "║ " + lenFit(str(x+1), 2) + "│ " + lenFit(data[x]['username'], 15) + "│ " + lenFit(data[x]['name'], 27) + "│ " + lenFit(
            data[x]['lastLogin'], 11) + "║")
        if len(data) == x + 1:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 16 + "╧" + "═" * 28 + "╧" + "═" * 12 + "╣")
        elif len(data) != x:
            print('\t' + "╟" + "─" * 3 + "┼" + "─" * 16 + "┼" + "─" * 28 + "┼" + "─" * 12 + "╢")
        x += 1

    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + lenFit('    B: Back', 62) + "║")
    print('\t' + "╚" + "═" * 62 + "╝")
    return ' '


def addUserList():
    with open('addUser.csv') as myFile:
        reader = csv.DictReader(myFile)
        data = [r for r in reader]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 24 + "Add User List" + " " * 25 + "║")
    print('\t' + "╠" + "═" * 3 + "╤" + "═" * 11 + "╤" + "═" * 34 + "╤" + "═" * 11 + "╣")
    print('\t' + "║" + " # │ User Type │             Username             │ Condition " + "║")
    print('\t' + "╟" + "─" * 3 + "┼" + "─" * 11 + "┼" + "─" * 34 + "┼" + "─" * 11 + "╢")

    x = 0
    while True:
        if len(data) == 0:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 11 + "╧" + "═" * 34 + "╧" + "═" * 11 + "╣")
        if len(data) <= x:
            break
        print('\t' + "║ " + lenFit(str(x + 1), 2) + "│ " + lenFit(data[x]['type'], 10) + "│ " + lenFit(
            data[x]['user'], 33) + "│ " + lenFit(
            data[x]['condition'], 10) + "║")
        if len(data) == x + 1:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 11 + "╧" + "═" * 34 + "╧" + "═" * 11 + "╣")
        elif len(data) != x:
            print('\t' + "╟" + "─" * 3 + "┼" + "─" * 11 + "┼" + "─" * 34 + "┼" + "─" * 11 + "╢")

        x += 1

    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + lenFit('    B: Back', 62) + "║")
    print('\t' + "║" + lenFit('    <Username> <A/D> (ex:s123 a)', 62) + "║")
    print('\t' + "╚" + "═" * 62 + "╝")
    return ''


def lessonList():
    with open('lessons.csv') as myFile:
        reader = csv.DictReader(myFile)
        data = [r for r in reader]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 25 + "Lessons List" + " " * 25 + "║")
    print('\t' + "╠" + "═" * 3 + "╤" + "═" * 21 + "╤" + "═" * 36 + "╣")
    print('\t' + "║" + " # │     Lesson Name     │  " + lenFit('Teacher Number', 34) + "║")
    print('\t' + "╟" + "─" * 3 + "┼" + "─" * 21 + "┼" + "─" * 36 + "╢")

    x = 0
    while data:
        if len(data) <= x:
            break
        print('\t' + "║ " + lenFit(str(x + 1), 2) + "│ " + lenFit(data[x]['lesson'], 20) + "│ " + lenFit(
            data[x]['tea'], 35) + "║")
        if len(data) == x + 1:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 21 + "╧" + "═" * 36 + "╣")
        elif len(data) != x:
            print('\t' + "╟" + "─" * 3 + "┼" + "─" * 21 + "┼" + "─" * 36 + "╢")
        x += 1

    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + lenFit('    B: Back', 62) + "║")
    print('\t' + "║" + lenFit('    <Lesson Name> <Teacher Number> (ex:math s123)', 62) + "║")
    print('\t' + "╚" + "═" * 62 + "╝")

    return ' '


def addLesList():
    with open('addLesson.csv') as myFile:
        reader = csv.DictReader(myFile)
        data = [r for r in reader]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 24 + "Add Lesson List" + " " * 23 + "║")
    print('\t' + "╠" + "═" * 3 + "╤" + "═" * 16 + "╤" + "═" * 28 + "╤" + "═" * 12 + "╣")
    print('\t' + "║" + " # │ Teacher Number │         Lesson Name        │ Condition  " + "║")
    print('\t' + "╟" + "─" * 3 + "┼" + "─" * 16 + "┼" + "─" * 28 + "┼" + "─" * 12 + "╢")

    x = 0
    while True:
        if len(data) == 0:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 16 + "╧" + "═" * 28 + "╧" + "═" * 12 + "╣")
        if len(data) <= x:
            break
        print('\t' + "║ " + lenFit(str(x+1), 2) + "│ " + lenFit(data[x]['tea'], 15) + "│ " + lenFit(data[x]['lesson'], 27) + "│ " + lenFit(
            data[x]['condition'], 11) + "║")
        if len(data) == x + 1:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 16 + "╧" + "═" * 28 + "╧" + "═" * 12 + "╣")
        elif len(data) != x:
            print('\t' + "╟" + "─" * 3 + "┼" + "─" * 16 + "┼" + "─" * 28 + "┼" + "─" * 12 + "╢")

        x += 1

    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + lenFit('    B: Back', 62) + "║")
    print('\t' + "║" + lenFit('    <Lesson Name> <A/D> (ex:math a)', 62) + "║")
    print('\t' + "╚" + "═" * 62 + "╝")
    return ' '


def lesListStu(odd):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print('\t' + "╔" + "═" * 62 + "╗")
    print('\t' + "║" + " " * 24 + "Add Lesson List" + " " * 23 + "║")
    print('\t' + "╠" + "═" * 3 + "╤" + "═" * 20 + "╤" + "═" * 25 + "╤" + "═" * 11 + "╣")
    print('\t' + "║" + " # │    Lesson Name     │      Teacher Number     │   Grade   " + "║")
    print('\t' + "╟" + "─" * 3 + "┼" + "─" * 20 + "┼" + "─" * 25 + "┼" + "─" * 11 + "╢")

    x = 0
    while odd:
        if len(odd) <= x:
            break
        print('\t' + "║ " + lenFit(str(x + 1), 2) + "│ " + lenFit(odd[x]['lesson'], 19) + "│ " + lenFit(odd[x]['tea'],
            24) + "│ " + lenFit(odd[x]['grade'], 10) + "║")
        if len(odd) == x + 1:
            print('\t' + "╠" + "═" * 3 + "╧" + "═" * 20 + "╧" + "═" * 25 + "╧" + "═" * 11 + "╣")
        elif len(odd) != x:
            print('\t' + "╟" + "─" * 3 + "┼" + "─" * 20 + "┼" + "─" * 25 + "┼" + "─" * 11 + "╢")

        x += 1

    print('\t' + "║" + "  Please choose from the menu:" + " " * 32 + "║")
    print('\t' + "║" + " " * 62 + "║")
    print('\t' + "║" + lenFit('    B: Back', 62) + "║")
    print('\t' + "╚" + "═" * 62 + "╝")

    return ' '