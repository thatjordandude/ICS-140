

# options display
def display_menu():
    print('Chose from the following options: ')
    print('1. Add item\n2. Remove item\n3. View list\n4. Exit')

# Add item to list
def add_item(item_list):
    item = input('Enter item you wish to add: ')
    item_list.append(item)
    print('Success! {} was added to your list'.format(item))
    return item_list  

# Remove item
def remove_item(item_list):
    item = input('Enter item to be removed from list: ')
    try:
        item_list.remove(item)
        print('Success! {} was removed from your list'.format(item))
    except ValueError:
        print('Item was not found in list')
        print('Would you like to try again?')
        choice = input('Y/N: ').upper()
        if choice == 'Y':
            remove_item(item_list)
        else:
            pass
    return item_list                    

# View the list
def view_list(item_list):
    print('Items in your shopping list are:')
    print('Currently you have {} items in your shipping list'.format(len(item_list)))
    for item in item_list:
        print(item)

def main():
    item_list=[]
    quit = True
    while quit:
        display_menu()
        choice = input('Your choice: ')
        if choice == '1':
            add_item(item_list)
        if choice == '2':
            remove_item(item_list)
        if choice == '3':
            view_list(item_list)
        if choice == '4':
            quit = False

main()