age = 20

age_group = 'minot' if age < 18 else 'adult'
print(age_group)

# LIST COMPREHENSION
def list_comp_exp(number):
    return number * 10

list1 = [2, 5, 9, 3]
modify_list = [ list_comp_exp(i) for i in list1]
modify_list2 = [ i * 2 for i in list1]
print(modify_list)

# DICT COMPREHENSION

dict1 = {'name': 'Mahatab', 'city': 'Bengaluru'}

square_dict = { i: i*2 for i in range(10)}
modify_dict = {value: key for key, value in dict1.items()}
print(square_dict)
print(modify_dict)

a = 1,
print(a)

