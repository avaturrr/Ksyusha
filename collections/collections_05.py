#

my_set_1 = {1, 2, 3, 4, 5, 6, "lslsslsl"}
my_set_2 = {7, 8, 9, 10, 3, 4, 5}
print(my_set_2)
common_set = my_set_1 | my_set_2
print(common_set)
identical_set = my_set_1 & my_set_2
print(identical_set)
dif_set_1 = my_set_1 - my_set_2
dif_set_2 = my_set_2 - my_set_1
print(dif_set_1, dif_set_2)
set_05 = my_set_1 ^ my_set_2
print(set_05)

