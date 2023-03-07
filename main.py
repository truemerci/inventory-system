inventory = []


def search():
    print("Enter 1 if you want to search by name")
    print("Enter 2 if you want to search by description")
    my_search = int(input())
    if my_search == 1:
        my_name1 = input("Enter your name: ")
        for i in inventory:
            if i['name'] == my_name1:
                print(i['name'])
            else:
                print(f"No such name '{my_name1}'")
    elif my_search == 2:
        my_name2 = input("Enter a description: ")
        for i in inventory:
            if i['descriptions'] == my_name2:
                print(i['name'])
            else:
                print(f'According to this description "{my_name2}" product not found')


def update():
    my_name = input("Enter the name you want to update quantity : ")
    for i in range(len(inventory)):
        if inventory[i]['name'] == my_name:
            update_quantity = int(input("Enter new quantity: "))
            inventory[i]['quantity'] = update_quantity
            break
    else:
        print(f"No such name '{my_name}'")


def delete():
    del_name = input("Enter the name you want to delete: ")
    for i in inventory:
        if del_name in i.values():
            inventory.remove(i)
            break
        else:
            print(f"There is no such '{del_name}' product")


def add_inventory():
    name = input("Enter name: ")
    descriptions = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    inv = {
        "name": name,
        "descriptions": descriptions,
        "quantity": quantity
    }
    inventory.append(inv)


def menu():
    print("1.View Inventory")
    print("2.Add Item")
    print("3.Remove Item")
    print("4.Update Quantity")
    print("5.Search Inventory")
    print("6.Quit")

    option = input("Enter your choice: ")

    return option


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == "2":
            add_inventory()
        elif choice == "1":
            print(inventory)
        elif choice == "3":
            delete()
        elif choice == "4":
            update()
        elif choice == "5":
            search()
        elif choice == "6":
            break
        else:
            print("No such operation exists.")
