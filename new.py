def choose_created_list_type():
    """This function allows the user to choose the type of list"""
    list_type = input("What type of of list are you sorting (nums/alpha): ")
    list_type = list_type.lower()
    if list_type == 'nums':
        create_nums_list()
    elif list_type == 'alpha':
        create_alpha_list()
    else:
        print(f"'{list_type}' was not an option.")
        choose_created_list_type()


def create_nums_list():
    """This function allows the user to create a number list"""
    created_list = []
    print("\nType !quit to end list creation.")
    print("Type !pop to remove the last item you entered from the list.")
    while True:
        items = input("Add an item to the list: ")
        if items == "!quit":
            return created_list
            break
        elif items == "!pop":
            created_list.pop()
        elif items != float:
            print(f"'{items}' is not a number.")
        else:
            created_list.append(float(items))


def create_alpha_list():
    """This function allows the user to create an alphanumeric list"""
    created_list = []
    print("\nType !quit to end list creation.")
    print("Type !pop to remove the last item you entered from the list.")
    while True:
        items = input("Add an item to the list: ")
        if items == "!quit":
            return created_list
            break
        elif items == "!pop":
            created_list.pop()
        elif items!= str:
            print(f"'{items}' is not alphanumeric.")
        else:
            created_list.append(str(items))


def choose_premade_list_type():
    """This function allows the user to choose the type of list"""
    list_type = input("What type of of list are you sorting (nums/alpha): ")
    list_type = list_type.lower()
    if list_type == 'nums':
        use_nums_list()
    elif list_type == 'alpha':
        use_alpha_list()
    else:
        print(f"'{list_type}' was not an option.")
        choose_premade_list_type()


def select_list():
    """This functions allows the user to select a list"""
    filename = input("Enter the filename to be sorted: ")
    with open(filename) as f:
        lines = f.readlines()
        return lines


def use_nums_list():
    """"""
    select_list()
    while True:
        if lines != float:
            print(f"'{lines}' is not a number.")
        else:
            created_list.append(float(lines))


def use_alpha_list():
    """"""
    select_list()
    while True:
        if lines != float:
            print(f"'{lines}' is not alphanumeric.")
        else:
            created_list.append(str(lines))


def the_list():
    """This function allows the user to choose a list"""
    choose_list = input("Create or select a list (c/s): ")
    choose_list = choose_list.lower()
    if choose_list == 'c':
        choose_created_list_type()
        return choose_created_list_type()
    elif choose_list == 's':
        choose_premade_list_type()
        return choose_premade_list_type()
    else:
        print(f"{choose_list} was not an option.")
        the_list()


def selection_sort(result):
    for i in range(len(result)):
        cur_min = i
        for j in range(i, len(result)):
            if result[j] < result[cur_min]:
                cur_min = j
        result[i], result[cur_min] = result[cur_min], result[i]


result = the_list()
#copy = result[:]  # slice operator
#result.sort()
#selection_sort(result)
print(result)
