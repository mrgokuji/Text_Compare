f = open("file1.txt")
f1 = open("file2.txt")
i = 0
n = []
for i in range(100):
	p = f1.readline().strip().split(' ')
	p = ''.join(p)
	n.append(p)

for i in range(100):
	st = f.readline().strip().split(' ')
	st = ''.join(st)
	if st in n :
		continue 
	else :
		print(st)
