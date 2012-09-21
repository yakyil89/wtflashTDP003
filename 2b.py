def shopping_list():
    """Shows the list items as a numbered list"""
    print('\n')
    for i, a in enumerate(the_list):	# Use enumerate to be able to use index
        print(str(i + 1) + '. ' + a)
    print('\n')

def shopping_add():
    """prompts the user to input an item to the shopping list"""
    the_list.append(input("What do you wish to add? "))
    return mode

def shopping_remove():
    #TODO: fixa
    shopping_list()
    input_int()
    list.pop(int(element) - 1)
    
def input_int():
    #TODO: fixa
    """Prompts the user to input a value, if value isn't an integer... ask the 
    user to try again"""
    element = input('Write the index number of the item to remove: ')
    while element.isdigit() == False:
        element = input("The value you entered wasn't and integer, try again: ")
    return element
    
element = ''
# The one list... TO RULE THEM ALL!
the_list = []
# Decides which function to run
mode = input('Type a command. Type help for information: ') 
while mode != 'q':
    if mode == 'help':
        print('\n*Write the letter in parantheses\n*Show List (show)\n*Add object to list(add)\n*Delete object from list (del)\n*Edit object in list (edit)\n*quit program (q)\n')
        mode = input('Type a command.Type help for information: ')
    elif mode == 'show':
        shopping_list()
        mode = input('Type a command.Type help for information: ')
    elif mode == 'add':
        shopping_add()
        mode = input('Type a command.Type help for information: ')
    elif mode == 'del':
        shopping_remove()
        mode = input('Type a command.Type help for information: ')
    elif mode == 'edit':
        shopping_edit()
        mode = input('Type a command.Type help for information: ')
    else:
        input('Input a proper command: ')
