def generator_fun():
    yield 1
    yield 2
    yield 3

print('___________FOR_____________')
for value in generator_fun():
    print(value)

print('____________Next____________')

x = generator_fun()
print(list(x))
print(x)

# for i in range(3):
#     print(next(x))


