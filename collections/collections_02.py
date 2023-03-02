#создать список
#после каждой операции выводить список на экран

my_list = [1, 2, 3, 4, 5, "lasdkfj"]
my_list.append("Hello")
print(my_list)
my_list.pop(0)
print(my_list)
my_list[1] = "world"
print(my_list)
my_list.remove("world")
print(my_list)
my_list = my_list[::-1]
print(my_list)


