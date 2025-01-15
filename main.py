from source.util import input_pages, insert_to_db, check_db, save_to_file, save_as_file_input, user_input_del_table, delete_table_by_name
from source.scrape import scrape_api
import logging


def scrape():
    """ Merged function to scrape data and store it to database and export as xlsx and csv"""
    total_pages, tablename, table_class = input_pages()

    for i in range(0, total_pages * 20, 20):
        results = scrape_api(i)
        if not results:
            print('No data available')
            break

        for result in results:
            if not check_db(result, table_class):
                insert_to_db(result, table_class)
                print(f'Plugin inserted to database: {result["Name"]}')
            else:
                print(f'Record already exist: {result["Name"]}')
    while True:
        export = input('Export as Excel and CSV (y/n):').lower()
        if export not in ['y', 'n']:
            continue

        if export == 'y':
            confirm = False
            filename, sheet_title, sheet_desc, table_name = save_as_file_input(confirm, tablename)
            save_to_file(filename=filename, sheet_title=sheet_title, sheet_desc=sheet_desc, table_name=tablename)
            return

        else:
            return


def export_to_file():
    """ Merged function to export table from database"""
    try:
        save_to_file(*save_as_file_input())
    except Exception as e:
        print(f'Error {e}')


def delete_table():
    """ Merged function to delete table from database"""
    delete_table_by_name(user_input_del_table())


def main_menu():
    """ Main function """
    while True:
        options = input("""
1. Scrape Plugins
2. Export database into Excel and CSV
3. Delete database table
4. Quit

Enter option: """)

        if not options.isdigit():
            print('Enter only number')
            continue
        if options == '1':
            scrape()
        elif options == '2':
            export_to_file()
        elif options == '3':
            delete_table()
        elif options == '4':
            print('Exiting program')
            return
        else:
            print('Out of option')


if __name__ == '__main__':
    main_menu()


"""
test run
"""