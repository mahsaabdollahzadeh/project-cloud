import csv


file = open("airports.csv")
file = open("airports.csv", "r")
data = csv.reader(file)
print (data)