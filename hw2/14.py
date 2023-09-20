count = 0
sum = 0.0
n = 1

while n != 0:
	n = int(input("Input integer numbers "))
	sum += n
	count += 1
	
print("Average and Sum are: ", sum / (count-1), sum)