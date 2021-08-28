import os # operating system

# read file
def read_file(file_name):
	product = []
	with open(file_name, 'r') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name, price = line.strip().split(',')
				product.append([name, price])
	return product

# user input
def user_input(product):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		product.append([name,price])
	print(product)
	return product

# print all products record
def print_product(product):
	for p in product:
		print(p[0], '的價格是', p[1])

# write file
def write_file(file_name, product):
	with open(file_name, 'w') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	file_name = 'product.csv'
	if os.path.isfile(file_name):  # 檢查檔案在不在
		product = read_file(file_name)
		print('yeah!')
	else:
		print('No File...') 

	product = user_input(product)
	print_product(product)
	write_file('product.csv', product)

main()