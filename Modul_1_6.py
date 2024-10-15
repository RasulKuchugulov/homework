my_dict = {'Andrey': 2005, 'Erick': 2007, 'Maxim':2003}
print("По имени:", *my_dict.items())
print("Год рождения Andrey:", my_dict.get("Andrey"))
print("Год рождения:", my_dict.get("Alex", "Не найдено"))
my_dict["Mary"] = 2007
my_dict["Georgy"] = 2007
print("Обновленный список my_dict:", *my_dict.items())
remov_value = my_dict.pop("Erick", "Не найдено")
print("Удалено значение для Andrey:", remov_value)
print("Обновлённый список my_dict:", *my_dict.items())

my_set = {9, 8, 7, 9, 8, 7, 6, 5, 4, "Andrey", True, 8, "Alex", "Andrey"}
print("Варианты:", *my_set)
my_set.add(9)
my_set.add("Aleksis")
my_set.remove(4)
print("Измененный список:", *my_set)