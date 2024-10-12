immutable_var = (5, "M", 7)
print(immutable_var)
#immutable_var[0] = 199
#print(immutable_var)
#immutable_var[1] = 2000
#print(immutable_var)
# immutable_var[0] = 199   #Попытка изменить элемент кортежа
# TypeError: 'tuple' object does not item assigmet #Ошибка
#Кортежи являются неизменяемыми типами данных.
# Это значит , что после создания кортежа его нельзя изменять или перезаписывать

immutable_list = [5, 6, 7, "M"]
print(immutable_list)
immutable_list[0] = "Y"
print(immutable_list)

