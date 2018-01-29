import os
# set the directory 
# sys.path.insert(THE_PATH_TO_THE_DIRECTORY_OF_THE_FILE)

FILE_NAME1 = 'file1.txt'
FILE_NAME2 = 'file2.txt'
NEW_FILE = 'target.txt'
s = []
m = {}

# store lines in two files into a single sequence s
with open(FILE_NAME1) as f1:
	line = f1.readline()
	s.append(line)
	while line:
		line = f1.readline()
		s.append(line)
	s.pop()
f1.close()

with open(FILE_NAME2) as f2:
	line = f2.readline()
	s.append(line)
	while line:
		line = f2.readline()
		s.append(line)
	s.pop()
f2.close()
s.sort()
s = [line.rstrip('\n') for line in s]
n = len(s)

# check if two names belong to a single quantifier,
# if so, merge them
for i in xrange(n):
	c = s[i].split(' ')
	if i > 0:
		prev = s[i-1].split(' ')
		if prev[0] == c[0]:
			m[c[0]].append(c[1:])
		else:
			m[c[0]] = [c[1:]]
	else:
		m[c[0]] = [c[1:]]

tf = open(NEW_FILE,'w')
for x in m.keys():
	line = ""
	if len(m[x]) == 2:
		line = x + " " + m[x][0][0]+ " " + m[x][0][1] + " "+ m[x][1][0] + " "+ m[x][1][1] 
		tf.write(line)
		tf.write('\n')
	else:
		line = x+ " "+ m[x][0][0] + " "+ m[x][0][1]
		tf.write(line)
		tf.write('\n')

tf.close()



