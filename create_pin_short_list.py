import csv

def check_for_duplicates(list_to_check: list) -> bool:
    for elem in list_to_check:
        if list_to_check.count(elem) > 1:
            return True
        else:
            False

def read_file(file_name: str) -> list:
    with open(file_name) as csv_f:
        csv_file_reader_object = csv.DictReader(csv_f)
        return list(csv_file_reader_object)

def create_pin_list(csv_list: list) ->list:
    pin_list = list()
    for i in csv_list:
        pin = i.get('pin')
        pin_list.append(pin)
    return pin_list

def split_number_to_list(number: str) -> list():
    li = list(filter(lambda i:(i in number),number))
    return li

def create_unique_pin_list(pin_list: list) -> list:
    unique_pin_list = list()
    for i in pin_list:
        # check = i in unique_pin_list
        # print(check)
        if i not in unique_pin_list:
            if not check_for_duplicates(split_number_to_list(i)):
                unique_pin_list.append(i)
    return unique_pin_list

# def save_to_file(file_name: str, list_to_save) -> bool:


if __name__ == "__main__":
    file_name = 'four-digit-pin-codes-sorted-by-frequency-withcount.csv'
    
    csv_l = read_file(file_name)
    pin_list = create_pin_list(csv_l)
    
    print(f'pin_list len: {len(pin_list)}')

    """Create unique 4 digit with unique numbers list"""
    unique_pin_list = create_unique_pin_list(pin_list)
    print(f'unique_pin_list len: {len(unique_pin_list)}')
    # '''Save unique list to csv file'''

    # save_to_file('unique_4_digit_pin_list.csv', unique_pin_list)

