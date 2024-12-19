from source import session, engine, TABLE, DATE
from source.db_config import Format_SQL
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font
import pandas
import openpyxl
import os


def open_file(filename):
    try:
        with open(filename, 'r') as f:
            parameters = f.read()
            return parameters.split('\n')
    except FileNotFoundError:
        print('File not found')
    except FileExistsError:
        print('File corrupted')


def user_input():
    while True:
        pages = input('Input total page to scrape (empty = all): ') or 2949

        if pages.isdigit():
            total_pages = int(pages)
        else:
            print('Page must be a number')
            continue

        save_as_file_confirm = input('Save as csv and xlsx (y/n): ').lower()

        if save_as_file_confirm not in ['y', 'n']:
            print('Choose only y or n')
            continue

        if save_as_file_confirm == 'y':
            while True:
                filename = input('Input filename: ')
                if not filename:
                    print('Filename cannot empty')
                    continue

                if file_checker(f'{filename}_{DATE}.xlsx'):
                    verif = input(f'File {filename}_{DATE}.xlsx already exist. Overwrite? (y/n):  ').lower()
                    if verif != 'y':
                        continue
                break

            sheet_title = input('Input title for excel sheet (optional): ') or 'Wordpress Plugin Scraping Result'
            sheet_desc = input('Input desc for excel sheet (optional): ') or f'This file contain {total_pages*20} plugin from wordpress'
            return total_pages, filename, sheet_title, sheet_desc
        else:
            return total_pages, None, None, None


def insert_to_db(result):
    session.add(result)
    session.commit()
    print('Insert to db success')


def check_db(data):
    exist = session.query(Format_SQL).filter_by(Name=data.Name).first()
    return exist is not None


def save_to_file(filename: str, sheet_title: str, sheet_desc: str):
    query = f'SELECT * FROM {TABLE}'
    df = pandas.read_sql_query(query, engine)

    with pandas.ExcelWriter(f'{filename}_{DATE}.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, startrow=3, sheet_name='Sheet_1')
        worksheet = writer.sheets['Sheet_1']

        worksheet.merge_cells('A1:E1')
        worksheet.merge_cells('A2:E2')
        worksheet['A1'] = sheet_title
        worksheet['A2'] = sheet_desc

        worksheet['A1'].font = Font(name='Times New Roman', size=16, bold=True)
        worksheet['A1'].alignment = Alignment(horizontal='center', vertical='center')
        worksheet['A2'].alignment = Alignment(horizontal='left', vertical='center')
        print(f'Saved to file as: {filename}')

    df.to_csv(fr'D:\Github\aprinur\scraping_wordpress_plugin\{filename}_{DATE}.csv', index=False)


def file_checker(filename):
    exist = os.path.exists(filename)
    return exist


def del_db(db_name):
    try:
        os.remove(db_name)
    except FileNotFoundError:
        print(f"{db_name} not found")