import csv

import error
import listGenrator


def lp(user):
    print(listGenrator.lessonList())
    order = str(input("             Enter code: "))
    words = order.split()
    if words[0] == 'B' or words[0] == 'b':
        return
    row = [words[0], words[1], user, 'N/A']
    # print(row)
    with open('database.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


def ep(user):
    newPasscode = str(input("             please enter new pas:"))
    odd = []
    newPass = {'pass': newPasscode}
    with open("students.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['username'] == user:
                data.update(newPass)
            odd.append(data)
            # del data[2]

    with open('students.csv', 'w') as csvFile:
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
    with open("students.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['username'] == user:
                data.update(newUser)
                data.update(newName)
            odd.append(data)
            # del data[2]

    with open('students.csv', 'w') as csvFile:
        fields = ['username', 'pass', 'lastLogin', 'name']
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(odd)

    print("writing completed")

    csvFile.close()

