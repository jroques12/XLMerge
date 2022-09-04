def file_name_increment(file_name):
    while '.' not in file_name or file_name.index(".") == 0 or file_name[-1] == '.':
        file_name = input(
            'Please ensure you are entering a valid file name with full extension or type "C" to cancel: ')
        if file_name.upper() == 'C':
            print("Exiting file name incrementor program")
            exit()

    # file_name = '/home/scrant/PycharmProjects/Scrap2/SomethingElse99.xlsx'
    list_name = list(file_name)

    # finding the character before the last dot in the string, assigning to var last index
    last_indx = list_name[::-1].index('.') * -1 - 2

    if not list_name[last_indx].isdigit():
        list_name.insert(last_indx + 1, "1")
        new_fn = "".join(list_name)
        return new_fn
    first_indx = last_indx
    # print(f'Full List broken down: {list_name}')
    # print(f'First Index: {first_indx}')
    # print(f'Last Index: {last_indx}')

    while file_name[first_indx].isdigit():
        first_indx -= 1

    first_indx += 1
    # print(f'First index after while loop: {first_indx}')
    # print(f'Last index after while loop: {last_indx}')
    # print(f'Full List after while loop {list_name}')
    # print(f'Value at first index of list : {list_name[first_indx]}')
    # print(f'Value at last index of list : {list_name[last_indx]}')
    # print(f'Those values combined are : {list_name[first_indx:last_indx+1]}')
    # combining into a single list item
    list_name[first_indx:last_indx + 1] = [''.join(list_name[first_indx:last_indx + 1])]
    # print(f"Attempting to combine them into numbers, currently shows: {list_name}")
    # print(f'Attemtping to isolate those numbers from string: {list_name[last_indx]}')
    list_name[last_indx] = str(int(list_name[last_indx]) + 1)
    new_list_name = ''.join(list_name)
    # print(f'The final incremented list name is: {new_list_name}')
    return new_list_name
