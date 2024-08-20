immutable_var = ([567,323,432,'god'],'dog', True)
print(immutable_var)
immutable_var[0][3] = 10
print(immutable_var)
# элементы кортежа не изменны, но мы можем достать элемент и изменить его благодаря []
mutable_list = ['nissan','opel','bmw']
print(mutable_list)
mutable_list[0] = 'toyota'
mutable_list[1] = 'LADA'
print(mutable_list)
