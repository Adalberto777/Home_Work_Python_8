import view
import model_new_record
import model_id
import model_new_id
import model_read_records
import model_del
import model_imp_exp_csv


def gete_menu_item() -> str:
    result_menu = view.menu()
    if result_menu == '1':
        model_new_record.create_new_record(view.get_last_name(), view.get_first_name(), view.get_group(), model_id.read_id('id.txt'), 'data_base.txt')        
        model_new_id.write_id(model_id.read_id('id.txt'), 'id.txt')
    elif result_menu == '2':
        print(model_read_records.create_new_data(model_read_records.read_import_text('data_base.txt'), 'data_base.txt'))
    elif result_menu == '3':
        id = int(view.get_id())
        data_dict = model_read_records.create_new_data(model_read_records.read_import_text('data_base.txt'), 'data_base.txt')
        if id in data_dict:
            data_del = model_del.del_record(data_dict, id)
            model_del.create_new_data(data_del, 'data_base.txt')
            print(f'record with id - {id} deleted')   
        else: print('check the id')
    elif result_menu == '4': 
        id = int(view.get_id())
        data_dict = model_read_records.create_new_data(model_read_records.read_import_text('data_base.txt'), 'data_base.txt')
        if id in data_dict:
            data_update = model_del.update_record(data_dict, id, view.get_last_name(), view.get_first_name(), view.get_group())
            model_del.create_new_data(data_update, 'data_base.txt')
            print(f'record with id - {id} updated')   
        else: print('check the id')
    elif result_menu == '5': 
        id = int(view.get_id())
        data_dict = model_read_records.create_new_data(model_read_records.read_import_text('data_base.txt'), 'data_base.txt')
        if id in data_dict:
            model_read_records.show_data(model_read_records.create_new_data(model_read_records.read_import_text('data_base.txt'), 'data_base.txt'), id)                                    
        else: print('check the id')
    elif result_menu == '6':
        model_imp_exp_csv.import_csv('data_base.txt', model_imp_exp_csv.pars_csv('data_base.csv', model_id.read_id('id.txt')))
        old_id = int(model_id.read_id('id.txt'))
        count_id = model_imp_exp_csv.count_id('data_base.csv')
        new_id = str(old_id + count_id)                  
        model_new_id.write_id(new_id, 'id.txt')
    elif result_menu == '7':
        model_imp_exp_csv.import_csv('data_base.txt', model_imp_exp_csv.pars_csv_id('data_base_id.csv', model_id.read_id('id.txt')))
        old_id = int(model_id.read_id('id.txt'))
        count_id = model_imp_exp_csv.count_id('data_base.csv')
        new_id = str(old_id + count_id)                  
        model_new_id.write_id(new_id, 'id.txt')
    elif result_menu == '8': 
        print("Good Bye!") 
    else: 
        print("введен несуществующий пункт, выберите пункт меню от 1 до 8")
        gete_menu_item()  

