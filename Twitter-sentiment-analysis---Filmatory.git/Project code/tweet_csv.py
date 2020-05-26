import csv

with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/tweets.csv','r') as read_file:
        csv_reader=csv.reader(read_file)
        list1=[]
        next(csv_reader)
        for line in csv_reader:
            list1.append(line)

for line in list1:
	print(line)
