def create_list():
    """This function allows the user to create a list"""
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
        else:
            created_list.append(items)


def the_list():
    """This function allows the user to choose a list"""
    choose_list = input("Create or select a list (c/s): ")
    choose_list = choose_list.lower()
    if choose_list == 'c':
        return create_list()
        # result = create_list()
    elif choose_list == 's':
        print("select")  # continue later
    else:
        print(f"{choose_list} was not an option.")
        the_list()


result = the_list()
result.sort(reverse=True)
print(result)

'''
filename = input("List name: ")
with open(filename) as f:
'''
