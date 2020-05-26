import csv
list1=[]
with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/reviews.csv','r') as read_file:
	csv_reader=csv.reader(read_file)
	for line in csv_reader:
		list1.append(line)
	goodlist=list1[0]
	good=""
	for i in goodlist:
		good+=i
	good=int(good)
	badlist=list1[1]
	avglist=list1[2]
	print(type(good))
	print(good)
