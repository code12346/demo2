# Pascal's triangle for 10 rows
rows = 10
triangle = []
for i in range(rows):
	row = [1]
	if triangle:
		last_row = triangle[-1]
		for j in range(1, i):
			row.append(last_row[j-1] + last_row[j])
		row.append(1)
	triangle.append(row)

for i in range(rows):
	print(' ' * (rows - i), end='')
	print(' '.join(str(num) for num in triangle[i]))
