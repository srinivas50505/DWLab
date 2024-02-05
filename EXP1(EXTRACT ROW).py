import csv
with open(r'C:\Users\acer\Desktop\Srinivas-09\departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=',', quotechar='|')
 for row in data:
     for value in row:
         print(value) 

