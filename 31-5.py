import csv

with open('31-5.csv','w') as csvfile:
    writer=csv.writer(csvfile,delimiter=' ')
    writer.writerow(['id','name','age'])
    writer.writerow(['1','赵','18'])
    writer.writerow(['2','理','19'])
    writer.writerow(['3','想','20'])
    writer.writerows([['4','face','21'],['5','love','1314']])