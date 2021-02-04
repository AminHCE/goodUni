import csv


def stuSearch(stu):
    odd = []

    with open("database.csv", 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = dict(row)

            if data['stu'] == stu:
                odd.append(data)
    return odd

