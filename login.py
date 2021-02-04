import csv

import adminPage
import error
import stuPage
import teaPage


def loginAdmin(username, passcode):
    with open('admins.csv') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            if row['username'] == username and row['pass'] == passcode:
                return 1
        return 0


def loginStu(username, passcode):
    with open('students.csv') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            if row['username'] == username and row['pass'] == passcode:
                return 1
        return 0


def loginTea(username, passcode):
    with open('teachers.csv') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            if row['username'] == username and row['pass'] == passcode:
                return 1
        return 0


def loginChecker(user, passcode):
    if loginAdmin(user, passcode) == 1:
        adminPage.show('a', user)
    elif loginStu(user, passcode) == 1:
        stuPage.show('s', user)
    elif loginTea(user, passcode) == 1:
        teaPage.show('t', user)
    else:
        print(error.errorsList("003"))


def register(typeofUser, user, passcode):
    row = [typeofUser, user, passcode, 'N/A']

    with open('addUser.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()

