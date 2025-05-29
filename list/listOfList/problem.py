a = [[3,4], [5,6]]
b = [[]]

for i in range(0, len(a[0])):
	for j in range(0, len(a[0])):
		b[j][i] = a[i][j]

print(b)
