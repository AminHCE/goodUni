import csv

import error
import listGenrator


def al(user, lesson):
    row = [lesson, user, 'N/A']

    with open('addLesson.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()


def ep(user):
    newPasscode = str(input("             please enter new pas:"))
    odd = []
    newPass = {'pass': newPasscode}
    with open("teachers.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['username'] == user:
                data.update(newPass)
            odd.append(data)
            # del data[2]

    with open('teachers.csv', 'w') as csvFile:
        fields = ['username', 'pass', 'lastLogin', 'name']
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(odd)

    print("writing completed")

    csvFile.close()


def e(user):
    newUsername = str(input("             please enter new Username:"))
    newNames = str(input("             please enter new Name:"))
    odd = []
    newUser = {'username': newUsername}
    newName = {'name': newNames}
    with open("teachers.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['username'] == user:
                data.update(newUser)
                data.update(newName)
            odd.append(data)
            # del data[2]

    with open('teachers.csv', 'w') as csvFile:
        fields = ['username', 'pass', 'lastLogin', 'name']
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(odd)

    print("writing completed")

    csvFile.close()


def ex():
    return
