from operator import itemgetter

users_info = []

def start_sorting_name():
    while True:
        user_info = input("Enter your user info: ")
        split_string = user_info.split(",")
        if len(split_string) != 3:
            break

        users_info.append(tuple(split_string))

    users_info.sort(key=itemgetter(0, 1, 2))
    print(users_info)
