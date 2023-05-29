def create_data():
    title = input("Enter title: ")
    author = input("Enter author: ")
    release_year = int(input("Enter release_year: "))
    price = int(input("Enter price: "))
    my_list = [title, author, release_year, price]
    return my_list