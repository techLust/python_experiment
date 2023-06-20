file = open('./car-sales.csv', 'a+')
file.seek(0)
print(file.read())

# file.write('\nSuzuki, Orange, 631225, 6, "$6598720"')
file.close()