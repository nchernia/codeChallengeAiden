import os
with open('file1.txt') as f:
	line = f.readline()
	cnt = 1
	while line:
		print ("Line {}:{}".format(cnt, line.strip()))
		line = f.readline()
		cnt +=1