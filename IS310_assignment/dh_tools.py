import csv


'''with open('tools_dh_proceedings.csv', newline='') as f:
    fieldnames = ['Total']
    reader = csv.reader(f)
    writer = csv.writer(f,  fieldnames=fieldnames)
    for row in reader:
        writer.writeheader()
        #rows = {'Total': int(row[1]) + int(row[5])}
        #total = int(row[1]) + int(row[5])
        
        writer.writerow({'Total': int(row[1]) + int(row[5])})
       # print(row[0],row[1],row[5])
     #   print(total)'''

import pandas as pd
df = pd.read_csv('tools_dh_proceedings.csv')
clean = df.iloc[:, [0,1,5]]
num2015 = df['2015'] 
num2019 = df['2019']
#print(clean)
sum_column = num2015 + num2019
clean['Total'] = sum_column
print(clean)

import pandas as pd
df = pd.read_csv('tools_dh_proceedings.csv')
def function(a):
    tool = df[df['Tool'] == a] 
    print(tool)

function(input())