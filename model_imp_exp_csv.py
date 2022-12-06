import csv

def pars_csv(file:str, id:str) ->dict:
    with open(file, 'r', newline='', encoding = "utf-8") as csv_file:
        data_read = csv.reader(csv_file, delimiter='#')
        id = int(id)
        new_dict = {}
        for row in data_read:
            if row != []:
                new_dict[id] = (','.join(row)).split(',')
                id += 1
        return new_dict


def count_id(csv_file: str):
    with open(csv_file, 'r', newline='', encoding = "utf-8") as file:
        data_read = csv.reader(file, delimiter='#')
        id = 0        
        for row in data_read:
            if row != []:
                id += 1
    return id - 1

    
def import_csv(file: str, new_dict: dict) ->None:
    with open(file, mode = "a", encoding = "utf-8") as txt_file:       
        for key, value in new_dict.items():
            data = ','.join(value)                   
            txt_file.write(f'{key},{data},\n')     


def pars_csv_id(file:str, id:str) ->dict:
    with open(file, 'r', newline='', encoding = "utf-8") as csv_file:
        data_read = csv.reader(csv_file, delimiter='#')
        id = int(id)
        new_dict = {}
        new_list = []
        for row in data_read:
            if row != []:
                new_list = (','.join(row)).split(',')
                new_list.pop(0)
                new_dict[id] = new_list
                id += 1
        return new_dict       








