#

my_dict = {1 : "a", 2 : "b", 3 : "c", 4 : "d"}
my_dict["alex"] = 42
print(my_dict)
print(my_dict["alex"])
my_dict["alex"] = 55
print(my_dict)
my_dict.pop("alex")
print(my_dict)