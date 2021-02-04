import csv

import error
import listGenrator


def au():
    print(listGenrator.addUserList())
    order = str(input("             Your username:"))
    words = order.split()
    if words[0] == 'B' or words[0] == 'b':
        return
    if words[1] == 'A' or words[1] == 'a':
        with open('addUser.csv') as myFile:
            reader = csv.DictReader(myFile)
            data = [r for r in reader]
        myFile.close()
        x = 0
        while data:
            if data[x]['user'] == words[0]:
                row = [data[x]['user'], data[x]['pass'], '1397/1/1', 'N/A']
                if data[x]['type'] == 's':
                    with open('students.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
                elif data[x]['type'] == 't':
                    with open('teachers.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
                elif data[x]['type'] == 'a':
                    with open('admin.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
                else:
                    print(error.errorsList("003"))

                odd = []
                with open("addUser.csv", 'r') as csvFile:
                    reader = csv.DictReader(csvFile)
                    for row in reader:
                        data = dict(row)

                        if data['user'] != words[0]:
                            odd.append(data)

                with open('addUser.csv', 'w') as csvFile:
                    fields = ['type', 'user', 'pass', 'condition']
                    writer = csv.DictWriter(csvFile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(odd)

                break
            x += 1

        # odd = []
        # newCon = {'condition': 'A'}
        # with open("addUser.csv", 'r') as csvFile:
        #     reader = csv.DictReader(csvFile)
        #     for row in reader:
        #         data = dict(row)
        #
        #         if data['user'] == words[0]:
        #             data.update(newCon)
        #         odd.append(data)
        #
        # with open('addUser.csv', 'w') as csvFile:
        #     fields = ['type', 'user', 'pass', 'condition']
        #     writer = csv.DictWriter(csvFile, fieldnames=fields)
        #     writer.writeheader()
        #     writer.writerows(odd)

    elif words[1] == 'd' or words[1] == 'D':
        odd = []
        newCon = {'condition': 'D'}
        with open("addUser.csv", 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                data = dict(row)

                if data['user'] == words[0]:
                    data.update(newCon)
                odd.append(data)

        with open('addUser.csv', 'w') as csvFile:
            fields = ['type', 'user', 'pass', 'condition']
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(odd)
    else:
        print(error.errorsList("003"))

    return ''


def al():
    print(listGenrator.addLesList())
    order = str(input("             Your username:"))
    words = order.split()
    if words[0] == 'B' or words[0] == 'b':
        return
    if words[1] == 'A' or words[1] == 'a':
        with open('addLesson.csv') as myFile:
            reader = csv.DictReader(myFile)
            data = [r for r in reader]
        myFile.close()
        x = 0
        while data:
            if data[x]['lesson'] == words[0]:
                row = [data[x]['lesson'], data[x]['tea']]
                with open('lessons.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()

                odd = []
                with open("addLesson.csv", 'r') as csvFile:
                    reader = csv.DictReader(csvFile)
                    for row in reader:
                        data = dict(row)

                        if data['lesson'] != words[0]:
                            odd.append(data)

                with open('addLesson.csv', 'w') as csvFile:
                    fields = ['lesson', 'tea', 'condition']
                    writer = csv.DictWriter(csvFile, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(odd)

                break
            x += 1

    elif words[1] == 'd' or words[1] == 'D':
        odd = []
        newCon = {'condition': 'D'}
        with open("addLesson.csv", 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                data = dict(row)

                if data['lesson'] == words[0]:
                    data.update(newCon)
                odd.append(data)

        with open('addLesson.csv', 'w') as csvFile:
            fields = ['lesson', 'tea', 'condition']
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(odd)
    else:
        print(error.errorsList("003"))

    return ''


def ep(user):
    newPasscode = str(input("             please enter new pas:"))
    odd = []
    newPass = {'pass': newPasscode}
    with open("admins.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['username'] == user:
                data.update(newPass)
            odd.append(data)

    with open('admins.csv', 'w') as csvFile:
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
    with open("admins.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['username'] == user:
                data.update(newUser)
                data.update(newName)
            odd.append(data)
            # del data[2]

    with open('admins.csv', 'w') as csvFile:
        fields = ['username', 'pass', 'lastLogin', 'name']
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(odd)

    print("writing completed")

    csvFile.close()

