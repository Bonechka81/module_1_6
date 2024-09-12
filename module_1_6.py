my_dict = {'Alina': 1981, 'Dima': 1982, 'Sofia': 2008, 'Timur': 2014}
print(my_dict['Dima'])
my_dict['Alina'] = 1985
print(my_dict)
my_dict['Alina'] = 1981
print(my_dict)
my_dict['Egor'] = 2015
print(my_dict)
del my_dict ['Sofia']
print(my_dict)
my_dict.update({'Makar': 2013, 'Artur': 2014})
print(my_dict)
del my_dict['Makar']
print(my_dict)

my_set = {2, 4, 6, 8, 2, 4, 6, True, 'Box'}
print(my_set)
my_set.update([12, 'Mom'])
print(my_set)
my_set.remove('Box')
print(my_set)
my_set.discard('Mom')
print(my_set)

