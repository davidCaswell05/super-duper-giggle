import csv

with open('names.csv', mode='w') as csvfile:
    fieldNames = ['firstName', 'lastName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerow({"firstName": "David", "lastName": "Caswell"})
    writer.writerow({"firstName": "David", "lastName": "Caswell"})
    writer.writerow({"firstName": "David", "lastName": "Caswell"})
