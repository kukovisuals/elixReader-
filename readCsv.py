import csv 
import numpy as np 
import pandas as pd

file = open('symbols.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
	if len(row[10]) > 0:
		rows.append(row[0])
print(rows)
DF = pd.DataFrame(rows)
DF.to_csv("symbolsExport.csv", sep=',')
file.close()