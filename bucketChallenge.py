# since size of 0 or negative number do noes not make sense
# assume bucket size can only be positive integers

line1= input()
bucket_sizes = list(map(int, line1.split(' ')))
line2 = input()
target_value = list(map(int, line2))
target_value = target_value[0]
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
print (targetIsReachable(bucket_sizes, target_value))