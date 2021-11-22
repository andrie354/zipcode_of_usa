import csv
import time


nomor = []
with open('postalcode_2.csv', 'r') as n:
    csv_reader = csv.reader(n)
    for row in csv_reader:
        nomor.append(row[0])
        time.sleep(1)
        print(nomor)
