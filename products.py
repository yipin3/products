# read file
product = []
with open('product.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		product.append([name, price])
print(product)

# user input
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	product.append([name,price])
print(product)

# print all products record
for p in product:
	print(p[0], '的價格是', p[1])

# write file
with open('product.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')

