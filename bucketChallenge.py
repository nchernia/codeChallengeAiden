# input1 = input()
# input1 = input1.split(' ')

# since size of 0 or negative number do noes not make sense
# assume bucket size can only be positive integers

line1= input()
bucket_sizes = input1.split()
for i in len(bucket_sizes):
	bucket_sizes[i] = int(bucket_sizes[i])
line2 = input()
target_value = int(line2)
def targetIsReachable(bucket_sizes, target_value):
	i = 0
	m = len(bucket_sizes)
	if target_value > 0:
		while i < m:
			if targetIsReachable(bucket_sizes, target_value - bucket_sizes[i]) == 0 :
				i += 1	
			else:
				return 1
	elif target_value == 0:
		return 1
	return 0
print targetIsReachable(bucket_sizes, targetIsReachable)