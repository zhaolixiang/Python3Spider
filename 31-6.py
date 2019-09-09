import csv

with open('31-6.csv','w') as csvfile:
    file_names=['id','name','age']
    writer=csv.DictWriter(csvfile,fieldnames=file_names)
    writer.writeheader()
    writer.writerow({'id':1,'name':'理想','age':18})

with open('31-6.csv','r') as csvfile:
    render=csv.reader(csvfile)
    for row in render:
        print(row)

import pandas as pd
df =pd.read_csv('31-6.csv')
print(df)