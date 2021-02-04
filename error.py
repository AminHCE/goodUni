import csv


def errorsList(code):
    with open('errorList.csv') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            if row['code'] == code:
                return row['error']
