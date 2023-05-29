from my_sqlalchemy.library.b_l import create, read, update, delete, filter_by_author


def main():
    dict_func = {"1": create, "2": read, "3": update, "4": delete, "5": filter_by_author}
    while True:
        user_choice = input("Select function and enter its number:"
                            "1. create"
                            "2. read"
                            "3. update"
                            "4. delete"
                            "5. filter by author")
        if user_choice in dict_func.keys():
            dict_func[user_choice]()
        else:
            print("Select something else")

if __name__ == "__main__":
    main()
