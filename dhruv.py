import csv
filename='dhruv.csv'
with open(filename, mode='r') as file:
csv_reader=csv.reader(file)
for row in csv_reader:
  print(row)
