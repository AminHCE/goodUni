import datetime
import jalaliDate
import csv


def lastLogin(typeofUser, user):
    if typeofUser == 'a':
        with open('admins.csv') as myFile:
            reader = csv.DictReader(myFile)
            data = [r for r in reader]
        myFile.close()
        x = 0
        while data:
            if data[x]['username'] == user:
                return str(data[x]['lastLogin'])
            x += 1
    elif typeofUser == 't':
        with open('teachers.csv') as myFile:
            reader = csv.DictReader(myFile)
            data = [r for r in reader]
        myFile.close()
        x = 0
        while data:
            if data[x]['username'] == user:
                return str(data[x]['lastLogin'])
            x += 1
    elif typeofUser == 's':
        with open('students.csv') as myFile:
            reader = csv.DictReader(myFile)
            data = [r for r in reader]
        myFile.close()
        x = 0
        while data:
            if data[x]['username'] == user:
                return str(data[x]['lastLogin'])
            x += 1


def persianDate():
    return jalaliDate.Gregorian(datetime.datetime.date(datetime.datetime.now())).persian_string("{}/{}/{}")


def time():
    return str(datetime.datetime.now().time().hour) + ":" + str(datetime.datetime.now().time().minute)
